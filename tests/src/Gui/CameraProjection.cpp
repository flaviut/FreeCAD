// SPDX-License-Identifier: LGPL-2.1-or-later

#include <gtest/gtest.h>

#include <Inventor/SbVec2f.h>
#include <Inventor/SbViewportRegion.h>
#include <Inventor/SoDB.h>
#include <Inventor/actions/SoCallbackAction.h>
#include <Inventor/nodes/SoInfo.h>
#include <Inventor/nodes/SoOrthographicCamera.h>
#include <Inventor/nodes/SoPerspectiveCamera.h>
#include <Inventor/nodes/SoSeparator.h>

#include <Gui/Camera.h>

TEST(CameraProjection, MatchesCoinState)
{
    SoDB::init();

    for (SoCamera* camera :
         {static_cast<SoCamera*>(new SoOrthographicCamera),
          static_cast<SoCamera*>(new SoPerspectiveCamera)}) {
        auto* root = new SoSeparator;
        root->ref();
        root->addChild(camera);
        root->addChild(new SoInfo);
        camera->position.setValue(0.0F, 0.0F, 100.0F);
        camera->farDistance.setValue(1000.0F);
        if (auto* ortho = dynamic_cast<SoOrthographicCamera*>(camera)) {
            ortho->height.setValue(100.0F);
        }

        for (const auto mapping :
             {SoCamera::ADJUST_CAMERA, SoCamera::LEAVE_ALONE, SoCamera::CROP_VIEWPORT_NO_FRAME}) {
            camera->viewportMapping.setValue(mapping);

            // Reuse the camera across resizes, including a return to the original aspect ratio.
            for (const SbVec2s size :
                 {SbVec2s(600, 600), SbVec2s(400, 900), SbVec2s(900, 400), SbVec2s(600, 600)}) {
                for (const SbVec2s origin : {SbVec2s(0, 0), SbVec2s(31, 47)}) {
                    SCOPED_TRACE(camera->getTypeId().getName().getString());
                    SCOPED_TRACE(mapping);
                    SCOPED_TRACE(
                        ::testing::Message()
                        << size[0] << 'x' << size[1] << " origin=" << origin[0] << ',' << origin[1]
                    );
                    SbViewportRegion viewport(1000, 1000);
                    viewport.setViewportPixels(origin, size);
                    SbVec2f expected;

                    // Read Coin's traversal state independently of the projection helper.
                    SoCallbackAction action(viewport);
                    action.addPreCallback(
                        SoInfo::getClassTypeId(),
                        [](void* data, SoCallbackAction* action, const SoNode*) {
                            SbVec3f projected;
                            action->getViewVolume().projectToScreen(
                                SbVec3f(20.0F, 20.0F, 0.0F),
                                projected
                            );
                            const auto& viewport = action->getViewportRegion();
                            const auto origin = viewport.getViewportOriginPixels();
                            const auto size = viewport.getViewportSizePixels();
                            *static_cast<SbVec2f*>(data) = {
                                projected[0] * size[0] + origin[0],
                                projected[1] * size[1] + origin[1]
                            };
                            return SoCallbackAction::CONTINUE;
                        },
                        &expected
                    );
                    action.apply(root);

                    const auto actual
                        = Gui::Camera::projectPoint(*camera, viewport, SbVec3f(20.0F, 20.0F, 0.0F));
                    EXPECT_NEAR(actual[0], expected[0], 1e-3F);
                    EXPECT_NEAR(actual[1], expected[1], 1e-3F);
                }
            }
        }

        root->unref();
    }
}
