// SPDX-License-Identifier: LGPL-2.1-or-later

#include <gtest/gtest.h>

#if defined(__unix__) && !defined(OCC_CONVERT_SIGNALS)
# define OCC_CONVERT_SIGNALS
#endif
#include <Standard_ErrorHandler.hxx>
#include <Standard_Failure.hxx>
#include <Standard_Version.hxx>
#include <Standard_NumericError.hxx>
#include <OSD.hxx>

#include <atomic>
#include <csignal>
#include <cstdlib>
#include <future>
#include <string>
#include <thread>
#include <vector>

#if defined(OCC_CONVERT_SIGNALS)
namespace
{
class Cleanup: public Standard_ErrorHandler::Callback
{
public:
    void DestroyCallback() override
    {
        ++calls;
        UnregisterCallback();
    }

    int calls = 0;
};

bool catchJump(const std::string& message)
{
    Cleanup cleanup;
# if OCC_VERSION_HEX < 0x080000
    Handle(Standard_Failure) failure = new Standard_Failure(message.c_str());
# else
    Standard_NumericError failure(message.c_str());
# endif
    bool caught = false;
    try {
        OCC_CATCH_SIGNALS
        cleanup.RegisterCallback();
# if OCC_VERSION_HEX < 0x080000
        failure->Jump();
# else
        Standard_ErrorHandler::Abort(failure);
# endif
    }
    catch (const Standard_Failure& error) {
        caught = message == error.GetMessageString();
    }
    return caught && cleanup.calls == 1;
}
}  // namespace

TEST(SignalExceptionTest, NestedHandlersPreserveOuterCallback)
{
    Cleanup outer;
    {
        OCC_CATCH_SIGNALS
        outer.RegisterCallback();
        EXPECT_TRUE(catchJump("inner"));
        EXPECT_TRUE(Standard_ErrorHandler::IsInTryBlock());
        EXPECT_EQ(outer.calls, 0);
    }
    EXPECT_EQ(outer.calls, 1);
    EXPECT_FALSE(Standard_ErrorHandler::IsInTryBlock());
}

TEST(SignalExceptionTest, ConcurrentHandlersRemainIsolated)
{
    constexpr int threadCount = 8;
    std::promise<void> start;
    const auto ready = start.get_future().share();
    std::atomic<int> entered {0};
    std::atomic<int> failures {0};
    std::vector<std::thread> threads;
    for (int index = 0; index < threadCount; ++index) {
        threads.emplace_back([&, index] {
            Cleanup outer;
            {
                OCC_CATCH_SIGNALS
                outer.RegisterCallback();
                ++entered;
                ready.wait();
                for (int repeat = 0; repeat < 100; ++repeat) {
                    if (!catchJump(std::to_string(index)) || outer.calls != 0
                        || !Standard_ErrorHandler::IsInTryBlock()) {
                        ++failures;
                    }
                }
            }
            if (outer.calls != 1 || Standard_ErrorHandler::IsInTryBlock()) {
                ++failures;
            }
        });
    }
    while (entered != threadCount) {
        std::this_thread::yield();
    }
    start.set_value();
    for (auto& thread : threads) {
        thread.join();
    }
    EXPECT_EQ(failures, 0);
}

TEST(SignalExceptionTest, FloatingPointSignalConvertsToException)
{
    EXPECT_EXIT(
        {
            OSD::SetSignal();
            try {
                OCC_CATCH_SIGNALS
                std::raise(SIGFPE);
            }
            catch (const Standard_Failure&) {
                std::_Exit(0);
            }
            std::_Exit(1);
        },
        ::testing::ExitedWithCode(0),
        ""
    );
}
#endif
