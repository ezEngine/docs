# Selecting Objects

This page describes everything related to object selection.

## Common

* Pressing `ESC` will clear the selection.

## Selection Outline

Selected objects are highlighted with a yellow outline, which is visible through walls. This outline can be toggled with the `S` key or the respective toolbar button.

![Selection Outline](media/selection-outline.jpg)

## Shape Icons

Some component types use a *shape icon* as their graphical representation. This makes it possible to select these types of objects in the viewport. Shape icons can be toggle with the `I` key.

![Shape Icon](media/visualizer-shapeicon.jpg)

## Selection Bounding Box

When [visualizers](gizmos.md#visualizers) are enabled, the editor display a yellow bounding box around each selected object. Visualizers can be toggled with the `V` key.

## Viewport - Single Selection

* *Left-click* on an object to select it.
* Hold `CTRL` to add or remove objects from the selection.
* Hold `CTRL` and *middle-click* an object to open its material document. This does not work for [prefab instances (TODO)](../prefabs/prefabs-overview.md).

## Viewport - Marquee Selection

* Hold `SPACE` to enable marquee selection
* Then *left-click* and drag to *add* items to the selection
* Additionally hold `CTRL` before the left-click to instead *remove* items from the selection
* Press `ESC` to cancel the marquee selection

## Scene Tree

You can filter the scene tree with the search box at the top:

![Scene Tree Filter](media/scene-tree-filter.png)

## See Also

* [Back to Index](../index.md)
* [Editing Gizmos](gizmos.md)
* [Greyboxing (TODO)](greyboxing.md)
* [Scene Editing (TODO)](scene-editing.md)

