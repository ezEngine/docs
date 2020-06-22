# ezEngine

Welcome to ezEngine !

The latest source code can be cloned from [GitHub](https://github.com/ezEngine/ezEngine). Prefer to use the 'dev' branch, it contains the latest changes and bugfixes. 

Precompiled binary packages are provided under [Releases](https://github.com/ezEngine/ezEngine/releases). See the [Release Notes](releases/release-notes.md) for details.

This website is the main documentation for ezEngine. Additional source code API documentation [can be found here](https://ezengine.github.io/api-docs/). 

For topics not (yet) covered by the documentation, [contact us](getting-started/contact.md).

## Table of Contents

### Getting Started

* [API Docs](getting-started/api-docs.md)
* [Contact](getting-started/contact.md)
* [ezEditor Overview](getting-started/editor-overview.md)
* [Frequently Asked Questions](getting-started/faq.md)
* [How to Contribute](getting-started/how-to-contribute.md)
* [Videos](getting-started/videos.md)

### Releases

* [Release Notes](releases/release-notes.md)

### Build

* [Building ezEngine](build/building-ez.md)
* [Supported Platforms](build/supported-platforms.md)
* [Build Prerequisites](build/build-prerequisites.md)
* [CMake Setup](build/cmake-config.md)
* [ezEngine as a Submodule](build/submodule.md)
* [Building with Clang on Windows](build/clang-on-windows.md)
* [UWP Builds](build/build-uwp.md)
* [Android Builds](build/build-android.md)
* [Linux Builds](build/build-linux.md)
* [MacOS Builds](build/build-macos.md)

### Samples

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

### Editor

* [Editor Background Operations](editor/editor-bg-operations.md)
* [Editor Documents](editor/editor-documents.md)
* [Editor Plugins (TODO)](editor/editor-plugins.md)
* [Editor Settings](editor/editor-settings.md)
* [Template Documents (TODO)](editor/editor-template-documents.md)
* [Editing Views](editor/editor-views.md)
* [Running a Scene](editor/run-scene.md)

### Projects

* [Data Directories](projects/data-directories.md)
* [Project Settings](projects/project-settings.md)
* [Projects](projects/projects-overview.md)
* [Tags](projects/tags.md)

### Scenes

* [Advanced Object Transforms](scenes/advanced-object-transform.md)
* [Editor Camera](scenes/editor-camera.md)
* [Exposed Parameters (TODO)](scenes/exposed-parameters.md)
* [Editing Gizmos](scenes/gizmos.md)
* [Greyboxing](scenes/greyboxing.md)
* [Object References (TODO)](scenes/object-references.md)
* [Procedural Object Placement (TODO)](scenes/procedural-generation.md)
* [Scene Editing](scenes/scene-editing.md)
* [Selecting Objects](scenes/selection.md)

### Assets

* [Asset Browser](assets/asset-browser.md)
* [Asset Curator](assets/asset-curator.md)
* [Asset Profiles (TODO)](assets/asset-profiles.md)
* [Assets](assets/assets-overview.md)
* [Asset Import](assets/import-assets.md)

### Prefabs

* [Prefabs](prefabs/prefabs-overview.md)

### Graphics

* [Always Visible Component](graphics/always-visible-component.md)
* [Camera Component (TODO)](graphics/camera-component.md)
* [Instanced Mesh Component (TODO)](graphics/instanced-mesh-component.md)
* __Lighting__
  * [Ambient Light Component](graphics/lighting/ambient-light-component.md)
  * [Directional Light Component](graphics/lighting/directional-light-component.md)
  * [Dynamic Shadows](graphics/lighting/dynamic-shadows.md)
  * [Lighting (TODO)](graphics/lighting/lighting-overview.md)
  * [Point Light Component](graphics/lighting/point-light-component.md)
  * [Sky Light Component (TODO)](graphics/lighting/sky-light-component.md)
  * [Spot Light Component](graphics/lighting/spot-light-component.md)
* [Meshes (TODO)](graphics/meshes-overview.md)
* [Render Pipeline (TODO)](graphics/render-pipeline-overview.md)
* __Shaders__
  * [Shader Debugging](graphics/shaders/shader-debugging.md)
  * [Shader Permutation Variables](graphics/shaders/shader-permutation-variables.md)
  * [Shader Render State](graphics/shaders/shader-render-state.md)
  * [Shaders (TODO)](graphics/shaders/shaders-overview.md)
* [Sprite Component](graphics/sprite-component.md)
* [Textures](graphics/textures-overview.md)

### Materials

* [Materials](materials/materials-overview.md)
* [Surfaces](materials/surfaces.md)
* [Visual Shaders (TODO)](materials/visual-shaders.md)

### Input

* [Input Component (TODO)](input/input-component.md)
* [Input (TODO)](input/input-overview.md)

### Physics

* __Actors__
  * [Physics Actors (TODO)](physics/actors/actors.md)
  * [Breakable Sheet Component (TODO)](physics/actors/breakable-sheet-component.md)
  * [Character Controller (TODO)](physics/actors/character-controller.md)
  * [Character Proxy Component (TODO)](physics/actors/character-proxy-component.md)
  * [Dynamic Actor Component (TODO)](physics/actors/dynamic-actor-component.md)
  * [Static Actor Component (TODO)](physics/actors/static-actor-component.md)
  * [Trigger Component (TODO)](physics/actors/trigger-component.md)
* __Collision Shapes__
  * [Center of Mass Component (TODO)](physics/collision-shapes/center-of-mass-component.md)
  * [Collision Layers](physics/collision-shapes/collision-layers.md)
  * [Collision Meshes](physics/collision-shapes/collision-meshes.md)
  * [Physics Shapes (TODO)](physics/collision-shapes/shapes.md)
* __Joints__
  * [6DOF Joint Component (TODO)](physics/joints/6dof-joint-component.md)
  * [Distance Joint Component (TODO)](physics/joints/distance-joint-component.md)
  * [Fixed Joint Component (TODO)](physics/joints/fixed-joint-component.md)
  * [Physics Joints (TODO)](physics/joints/joints.md)
  * [Prismatic Joint Component (TODO)](physics/joints/prismatic-joint-component.md)
  * [Revolute Joint Component (TODO)](physics/joints/revolute-joint-component.md)
  * [Spherical Joint Component (TODO)](physics/joints/spherical-joint-component.md)
* [PhysX Integration (TODO)](physics/physx-overview.md)
* [PhysX Settings Component (TODO)](physics/physx-settings-component.md)
* [PhysX Visual Debugger](physics/visual-debugger.md)

### Effects

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

### Animation

* [Color Animation Component (TODO)](animation/color-animation-component.md)
* [Color Gradients](animation/color-gradients.md)
* [Curves](animation/curves.md)
* [MoveTo Component (TODO)](animation/move-to-component.md)
* [Property Animation Component (TODO)](animation/property-animation-component.md)
* [Property Animation (TODO)](animation/property-animation.md)
* [Rotor Component (TODO)](animation/rotor-component.md)
* [Slider Component (TODO)](animation/slider-component.md)

### Sound

* [Fmod Event Component (TODO)](sound/fmod-event-component.md)
* [Fmod Listener Component (TODO)](sound/fmod-listener-component.md)
* [FMOD Integration (TODO)](sound/fmod-overview.md)
* [Sound (TODO)](sound/sound-overview.md)

### Ai

* [Recast Navmesh Component (TODO)](ai/navmesh-component.md)
* [Recast Integration (TODO)](ai/recast.md)

### Gameplay

* [Area Damage Component (TODO)](gameplay/area-damage-component.md)
* [Marker Component](gameplay/marker-component.md)
* [Player Start Point](gameplay/player-start-point.md)
* [Projectile Component](gameplay/projectile-component.md)
* [Raycast Interaction Component (TODO)](gameplay/raycast-interaction-component.md)
* [Raycast Placement Component (TODO)](gameplay/raycast-placement-component.md)
* [Spawn Component](gameplay/spawn-component.md)
* [Timed Death Component](gameplay/timed-death-component.md)

---

### Custom Code

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

### Runtime

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

### Debugging

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

### Performance

* [Asset Collections (TODO)](performance/asset-collections.md)
* [Collection Component (TODO)](performance/collection-component.md)
* [Profiling (TODO)](performance/profiling.md)

### Tools

* [ArchiveTool](tools/archivetool.md)
* [FileServe (TODO)](tools/fileserve.md)
* [HeaderCheck Tool](tools/headercheck.md)
* [ezInspector](tools/inspector.md)
* [MiniDump Tool](tools/minidumptool.md)
* [ezPlayer](tools/player.md)
* [ShaderCompiler (TODO)](tools/shadercompiler.md)
* [StaticLinkUtil](tools/staticlinkutil.md)
* [ezTexConv (TODO)](tools/texconv.md)

---

### Tests

* [Test Framework (TODO)](tests/test-framework.md)
* [Unit Tests (TODO)](tests/unit-tests.md)

### Appendix

* [Contact](getting-started/contact.md)
* [Videos](getting-started/videos.md)
* [Library Structure](appendix/library-structure.md)
* [Coding Guidelines (TODO)](appendix/coding-guidelines.md)
* [Container Usage Guidelines](appendix/container-usage.md)
* [String Usage Guidelines](appendix/string-usage.md)
* [String Formatting](appendix/string-formatting.md)
* [Color Spaces (TODO)](appendix/color-spaces.md)
* [ThirdParty Code and Data](appendix/third-party-code.md)
