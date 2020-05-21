# Custom Components with C++

To write a custom C++ component, the first thing you need is a custom [engine plugins (TODO)](engine-plugins.md). Once you have that, and have it enabled in your [project settings](../../projects/project-settings.md), any custom component that you define in that plugin will show up in the editor and can be attached to [game objects (TODO)](../../runtime/world/game-objects.md).

The [Sample Game Plugin](../../samples/sample-game-plugin.md) shows all the pieces that you need, including multiple components to get inspiration from. This article will describe one of those components in more detail.

## Component Managers

For every type of C++ component there is a corresponding *component manager*. The component manager is responsible for allocating and deallocating components and for updating them. Each component manager is tied to a single `ezWorld`, so if you have multiple worlds, each world will hold its own instance of each component manager. 

A component manager is a [world module (TODO)](../../runtime/world/world-modules.md), so it can register functions to be called during specific update phases of the world. That is 



<!-- PAGE IS TODO -->

## See Also

* [Back to Index](../../index.md)
