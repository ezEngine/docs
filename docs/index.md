# ezEngine Documentation


## Getting Started

* [API Docs](getting-started/api-docs.md)
* [Contact](getting-started/contact.md)
* [ezEditor Overview](getting-started/editor-overview.md)
* [Frequently Asked Questions](getting-started/faq.md)
* [How to Contribute](getting-started/how-to-contribute.md)
* [Videos](getting-started/videos.md)

## Releases

* [Releases](releases/releases.md)

## Build

* [Building ezEngine](build/building-ez.md)
* [Supported Platforms](build/supported-platforms.md)
* [Build Prerequisites](build/build-prerequisites.md)
* [CMake Setup](build/cmake-config.md)
* [ezEngine as a Submodule](build/submodule.md)
* [SDK Root Folder](build/sdk-root.md)
* [Building with Clang on Windows](build/clang-on-windows.md)
* [UWP Builds](build/build-uwp.md)
* [Android Builds](build/build-android.md)
* [Linux Builds](build/build-linux.md)
* [MacOS Builds](build/build-macos.md)

## Samples

* [Samples](samples/samples-overview.md)
* [Asteroids Sample](samples/asteroids.md)
* [Compute Shader Histogram Sample](samples/cs-histogram.md)
* [LineCount Sample](samples/line-count.md)
* [RTS Sample](samples/rts.md)
* [Sample Game Plugin](samples/sample-game-plugin.md)
* [Shader Explorer Sample](samples/shader-explorer.md)
* [Testing Chambers](samples/testing-chambers.md)
* [Texture Sample](samples/texture-sample.md)

---

## Editor

* [Editor Background Operations](editor/editor-bg-operations.md)
* [Editor Documents](editor/editor-documents.md)
* [Editor Plugins (TODO)](editor/editor-plugins.md)
* [Editor Settings](editor/editor-settings.md)
* [Template Documents (TODO)](editor/editor-template-documents.md)
* [Editing Views](editor/editor-views.md)
* [Running a Scene](editor/run-scene.md)

## Projects

* [Data Directories](projects/data-directories.md)
* [Project Settings](projects/project-settings.md)
* [Projects](projects/projects-overview.md)
* [Tags](projects/tags.md)

## Scenes

* [Advanced Object Transforms](scenes/advanced-object-transform.md)
* [Editor Camera](scenes/editor-camera.md)
* [Exposed Parameters](scenes/exposed-parameters.md)
* [Editing Gizmos](scenes/gizmos.md)
* [Greyboxing](scenes/greyboxing.md)
* [Object References](scenes/object-references.md)
* [Procedural Object Placement (TODO)](scenes/procedural-generation.md)
* [Scene Editing](scenes/scene-editing.md)
* [Selecting Objects](scenes/selection.md)

## Assets

* [Asset Browser](assets/asset-browser.md)
* [Asset Curator](assets/asset-curator.md)
* [Asset Profiles (TODO)](assets/asset-profiles.md)
* [Assets](assets/assets-overview.md)
* [Asset Import](assets/import-assets.md)

## Prefabs

* [Prefabs](prefabs/prefabs-overview.md)

## Graphics

* [Always Visible Component](graphics/always-visible-component.md)
* [Camera Component](graphics/camera-component.md)
* __Lighting__
  * [Lighting](graphics/lighting/lighting-overview.md)
  * [Directional Light Component](graphics/lighting/directional-light-component.md)
  * [Point Light Component](graphics/lighting/point-light-component.md)
  * [Spot Light Component](graphics/lighting/spot-light-component.md)
  * [Dynamic Shadows](graphics/lighting/dynamic-shadows.md)
  * [Ambient Light Component](graphics/lighting/ambient-light-component.md)
  * [Skylight Component](graphics/lighting/sky-light-component.md)
* __Meshes__
  * [Meshes](graphics/meshes/meshes-overview.md)
  * [Mesh Asset](graphics/meshes/mesh-asset.md)
  * [Mesh Component](graphics/meshes/mesh-component.md)
  * [Instanced Mesh Component](graphics/meshes/instanced-mesh-component.md)
* [Render Pipeline (TODO)](graphics/render-pipeline-overview.md)
* __Shaders__
  * [Shader Debugging](graphics/shaders/shader-debugging.md)
  * [Shader Permutation Variables](graphics/shaders/shader-permutation-variables.md)
  * [Shader Render State](graphics/shaders/shader-render-state.md)
  * [Shaders (TODO)](graphics/shaders/shaders-overview.md)
* [Sprite Component](graphics/sprite-component.md)
* [Textures](graphics/textures-overview.md)

## Materials

* [Materials](materials/materials-overview.md)
* [Surfaces](materials/surfaces.md)
* [Visual Shaders (TODO)](materials/visual-shaders.md)

## Input

* [Input System](input/input-overview.md)
* [Input Set Configuration](input/input-config.md)
* [Input Component](input/input-component.md)

## Physics

* [PhysX Integration](physics/physx-overview.md)
* [PhysX Settings Component](physics/physx-settings-component.md)
* [PhysX Visual Debugger](physics/physx-visual-debugger.md)
* __Actors__
  * [PhysX Actors](physics/actors/physx-actors.md)
  * [PhysX Static Actor Component](physics/actors/physx-static-actor-component.md)
  * [PhysX Dynamic Actor Component](physics/actors/physx-dynamic-actor-component.md)
  * [PhysX Trigger Component](physics/actors/physx-trigger-component.md)
  * [PhysX Breakable Sheet Component (TODO)](physics/actors/physx-breakable-sheet-component.md)
* __Collision Shapes__
  * [PhysX Shapes](physics/collision-shapes/physx-shapes.md)
  * [PhysX Sphere Shape Component](physics/collision-shapes/physx-sphere-shape-component.md)
  * [PhysX Box Shape Component](physics/collision-shapes/physx-box-shape-component.md)
  * [PhysX Capsule Shape Component](physics/collision-shapes/physx-capsule-shape-component.md)
  * [PhysX Convex Shape Component](physics/collision-shapes/physx-convex-shape-component.md)
  * [PhysX Center of Mass Component](physics/collision-shapes/physx-center-of-mass-component.md)
  * [Collision Meshes](physics/collision-shapes/collision-meshes.md)
  * [Collision Layers](physics/collision-shapes/collision-layers.md)
* __Joints__
  * [Physics Joints](physics/joints/physx-joints.md)
  * [PhysX Revolute Joint Component](physics/joints/physx-revolute-joint-component.md)
  * [PhysX Spherical Joint Component](physics/joints/physx-spherical-joint-component.md)
  * [PhysX Fixed Joint Component](physics/joints/physx-fixed-joint-component.md)
  * [PhysX Prismatic Joint Component](physics/joints/physx-prismatic-joint-component.md)
  * [PhysX Distance Joint Component](physics/joints/physx-distance-joint-component.md)
  * [PhysX 6DOF Joint Component](physics/joints/physx-6dof-joint-component.md)
* __Special__
  * [Character Controller](physics/special/physx-character-controller.md)
  * [PhysX Grab Object Component](physics/special/physx-grab-object-component.md)

## Effects

* [Beam Component](effects/beam-component.md)
* [Decals](effects/decals.md)
* [Fog](effects/fog.md)
* __Particle Effects__
  * [Particle Effects](effects/particle-effects/particle-effects-overview.md)
  * [How Particle Effects Work](effects/particle-effects/how-particle-effects-work.md)
  * [Particle Emitters](effects/particle-effects/particle-emitters.md)
  * [Particle Initializers](effects/particle-effects/particle-initializers.md)
  * [Particle Behaviors](effects/particle-effects/particle-behaviors.md)
  * [Particle Renderers](effects/particle-effects/particle-renderers.md)
  * [Particle Effect Component](effects/particle-effects/particle-effect-component.md)
* [Render Target Activator Component (TODO)](effects/render-target-activator-component.md)
* [Render to Texture (TODO)](effects/render-to-texture.md)
* [Simple Wind Component (TODO)](effects/simple-wind-component.md)
* [Sky](effects/sky.md)
* [Wind (TODO)](effects/wind.md)

## Animation

* __Common__
  * [Color Gradients](animation/common/color-gradients.md)
  * [Curves](animation/common/curves.md)
* __Property Animation__
  * [Color Animation Component](animation/property-animation/color-animation-component.md)
  * [MoveTo Component (TODO)](animation/property-animation/move-to-component.md)
  * [Property Animation Asset (TODO)](animation/property-animation/property-animation-asset.md)
  * [Property Animation Component (TODO)](animation/property-animation/property-animation-component.md)
  * [Property Animations (TODO)](animation/property-animation/property-animation-overview.md)
  * [Rotor Component](animation/property-animation/rotor-component.md)
  * [Slider Component](animation/property-animation/slider-component.md)
* __Skeletal Animation__
  * [Skeletal Animations](animation/skeletal-animation/skeletal-animation-overview.md)
  * [Animated Mesh Asset](animation/skeletal-animation/animated-mesh-asset.md)
  * [Animated Mesh Component](animation/skeletal-animation/animated-mesh-component.md)
  * [Skeleton Asset](animation/skeletal-animation/skeleton-asset.md)
  * [Skeleton Component](animation/skeletal-animation/skeleton-component.md)
  * [Animation Clip Asset](animation/skeletal-animation/animation-clip-asset.md)
  * [Simple Animation Component](animation/skeletal-animation/simple-animation-component.md)
  * __Animation Controller__
    * [Animation Controller (TODO)](animation/skeletal-animation/animation-controller/animation-controller-overview.md)
    * [Animation Controller Asset (TODO)](animation/skeletal-animation/animation-controller/animation-controller-asset.md)
    * [Animation Controller Component](animation/skeletal-animation/animation-controller/animation-controller-component.md)
    * [Blackboard Nodes](animation/skeletal-animation/animation-controller/anim-nodes-blackboard.md)
    * [Bone Weight Nodes](animation/skeletal-animation/animation-controller/anim-nodes-bone-weights.md)
    * [Combine Poses Nodes](animation/skeletal-animation/animation-controller/anim-nodes-combine-poses.md)
    * [Debug Nodes](animation/skeletal-animation/animation-controller/anim-nodes-debug.md)
    * [Event Nodes](animation/skeletal-animation/animation-controller/anim-nodes-events.md)
    * [Input Nodes](animation/skeletal-animation/animation-controller/anim-nodes-input.md)
    * [Logic and Math Nodes](animation/skeletal-animation/animation-controller/anim-nodes-logic-math.md)
    * [Mix Clips 1D Node](animation/skeletal-animation/animation-controller/anim-nodes-mix1d.md)
    * [Mix Clips 2D Node](animation/skeletal-animation/animation-controller/anim-nodes-mix2d.md)
    * [Local To Model Pose Node](animation/skeletal-animation/animation-controller/anim-nodes-modelspace.md)
    * [Output Nodes](animation/skeletal-animation/animation-controller/anim-nodes-output.md)
    * [Play Single Clip Nodes](animation/skeletal-animation/animation-controller/anim-nodes-playclip.md)
    * [Play Clip Sequence Node](animation/skeletal-animation/animation-controller/anim-nodes-sequence.md)
  * [Animation Events](animation/skeletal-animation/animation-events.md)
  * [Root Motion](animation/skeletal-animation/root-motion.md)
  * [Joint Attachment Component](animation/skeletal-animation/joint-attachment-component.md)
  * [Joint Override Component](animation/skeletal-animation/joint-override-component.md)
  * [Authoring and Exporting Animations with Blender](animation/skeletal-animation/blender-export.md)

## Sound

* [Sound](sound/sound-overview.md)
* [Fmod Integration](sound/fmod-overview.md)
* [Fmod Sound Bank Asset](sound/fmod-soundbank-asset.md)
* [Fmod Sound Event Asset](sound/fmod-soundevent-asset.md)
* [Fmod Listener Component](sound/fmod-listener-component.md)
* [Fmod Event Component](sound/fmod-event-component.md)

## Terrain and Vegetation

* [Terrain and Vegetation](terrain/terrain-overview.md)
* [Heightfield Component](terrain/heightfield-component.md)
* [Kraut](terrain/kraut-overview.md)

## Ai

* [Recast Navmesh Component](ai/recast-navmesh-component.md)
* [Recast Navmesh](ai/recast-navmesh.md)
* [Recast Integration (TODO)](ai/recast.md)

## Ui

* [Ingame UI](ui/ui.md)
* [ImGui](ui/imgui.md)
* [RmlUi](ui/rmlui.md)

## Gameplay

* [Area Damage Component](gameplay/area-damage-component.md)
* [Grabbable Item Component](gameplay/grabbable-item-component.md)
* [Marker Component](gameplay/marker-component.md)
* [Player Start Point](gameplay/player-start-point.md)
* [Projectile Component](gameplay/projectile-component.md)
* [Raycast Placement Component](gameplay/raycast-placement-component.md)
* [Spawn Component](gameplay/spawn-component.md)
* [Timed Death Component](gameplay/timed-death-component.md)

## Miscellaneous

* [Blackboard Component](Miscellaneous/blackboard-component.md)
* [Blackboards](Miscellaneous/blackboards.md)
* [ImageData Asset](Miscellaneous/imagedata-asset.md)

---

## Custom Code

* [Custom Code](custom-code/custom-code-overview.md)
* __C++__
  * [Custom Code with C++](custom-code/cpp/cpp-overview.md)
  * [Engine Plugins](custom-code/cpp/engine-plugins.md)
  * [Custom Components with C++](custom-code/cpp/custom-cpp-component.md)
  * [Hot Reloading C++ Game Plugins in the Editor](custom-code/cpp/cpp-code-reload.md)
* __TypeScript__
  * [Custom Code with TypeScript](custom-code/typescript/typescript-overview.md)
  * [TypeScript Asset](custom-code/typescript/ts-asset.md)
  * [Custom Components with TypeScript](custom-code/typescript/custom-ts-components.md)
  * [TypeScript API](custom-code/typescript/ts-api.md)
  * [Messaging in TypeScript Code](custom-code/typescript/ts-messaging.md)
  * [TypeScript Component](custom-code/typescript/ts-component.md)
* __Visual Script__
  * [Custom Code with Visual Scripts](custom-code/visual-script/visual-script-overview.md)

## Runtime

* __Application__
  * [Application (TODO)](runtime/application/application.md)
  * [Common Application Features](runtime/application/common-application-features.md)
  * [Game States](runtime/application/game-state.md)
* __Configuration__
  * [Actor System (TODO)](runtime/configuration/actor-system.md)
  * [Singleton Interfaces](runtime/configuration/interfaces.md)
  * [Startup System](runtime/configuration/startup.md)
* [FileSystem](runtime/filesystem.md)
* [Reflection System](runtime/reflection-system.md)
* [Resource Management (TODO)](runtime/resource-management.md)
* __World__
  * [The World / Scenegraph System](runtime/world/world-overview.md)
  * [Game Objects](runtime/world/game-objects.md)
  * [Components](runtime/world/components.md)
  * [Worlds](runtime/world/worlds.md)
  * [Object Lifetime](runtime/world/object-lifetime.md)
  * [Messaging](runtime/world/world-messaging.md)
  * [World Modules](runtime/world/world-modules.md)
  * [Component Managers](runtime/world/component-managers.md)
  * [Spatial System](runtime/world/spatial-system.md)

---

## Debugging

* __Components__
  * [Debug Text Component](debugging/components/debug-text-component.md)
  * [DrawLineToObject Component](debugging/components/draw-line-component.md)
* [Console](debugging/console.md)
* [CVars](debugging/cvars.md)
* [Debugging C++ Code](debugging/debug-cpp.md)
* [Debug Rendering](debugging/debug-rendering.md)
* [Logging](debugging/logging.md)
* [RenderDoc Integration](debugging/renderdoc.md)
* [Stats](debugging/stats.md)

## Performance

* [Asset Collections](performance/asset-collections.md)
* [Collection Component](performance/collection-component.md)
* [Profiling](performance/profiling.md)

## Tools

* [ArchiveTool](tools/archivetool.md)
* [FileServe (TODO)](tools/fileserve.md)
* [HeaderCheck Tool](tools/headercheck.md)
* [ezInspector](tools/inspector.md)
* [MiniDump Tool](tools/minidumptool.md)
* [ezPlayer](tools/player.md)
* [ShaderCompiler (TODO)](tools/shadercompiler.md)
* [StaticLinkUtil](tools/staticlinkutil.md)
* [ezTexConv](tools/texconv.md)
* [Unit Tests](tools/unit-tests.md)

---

## Appendix

* [Library Structure](appendix/library-structure.md)
* [Coding Guidelines (TODO)](appendix/coding-guidelines.md)
* [Container Usage Guidelines](appendix/container-usage.md)
* [String Usage Guidelines](appendix/string-usage.md)
* [String Formatting](appendix/string-formatting.md)
* [Color Spaces (TODO)](appendix/color-spaces.md)
* [ThirdParty Code and Data](appendix/third-party-code.md)
