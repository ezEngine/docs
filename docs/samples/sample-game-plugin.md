# Sample Game Plugin

The **SampleGamePlugin** demonstrates the basics of how to build a [custom plugin (TODO)](../custom-code/custom-code-overview.md) for game code that can run both in a stand-alone application (such as [ezPlayer](../tools/player.md)) as well as inside the editor.

## Prerequisites

> **Note:** The project is only available when the solution is built with **EZ_BUILD_SAMPLES** activated.

## GameState

The *SampleGameState* class shows how to implement a simple [game state (TODO)](../runtime/application/game-state.md) that adds high-level game logic, such as handling a game UI. See `ezGameState` and `ezGameApplication` for further details.

## Components

* The `DemoComponent` shows how to modify the transform of an object dynamically.

* The `DebugRenderComponent` shows how to use [debug rendering](../debugging/debug-rendering.md).

For further details also see `ezComponent`.

## Project

Under *Data/Samples/SampleGame* you will find an [editor project](../projects/projects-overview.md) which uses the `SampleGamePlugin`. Note that the project references the plugin as a [runtime plugin](../custom-code/cpp/engine-plugins.md) (under *Editor > [Project Settings](../projects/project-settings.md) > Engine Plugins*). This makes the custom components available to the editor.

When you press 'Play' in the editor, the scene will be simulated and the custom components, such as the `DemoComponent`, will take effect.

When you press 'Play the Game' a full game window is launched and now even the custom [game state (TODO)](../runtime/application/game-state.md) is instantiated and executed. Consequently, the UI will appear and you can interact with it. Note that this still runs inside the editor process.

You can also [export and run the scene](../editor/run-scene.md) externally in the stand-alone [ezPlayer](../tools/player.md) application.

## See Also

* [Back to Index](../index.md)
* [Testing a Scene](../editor/run-scene.md)
* [Game States (TODO)](../runtime/application/game-state.md)
* [Custom Code (TODO)](../custom-code/custom-code-overview.md)
* [Videos](../appendix/videos.md)
