# Authoring and Exporting Animations with Blender

This page contains various pieces of information that are good to know when one uses Blender to build and export animated meshes. It is assumed that you know Blender well enough to create animated meshes.

## Exporting Animated Meshes

1. To get animated meshes out of Blender and into ezEngine, export the animated mesh to a binary GLTF file (`.glb`).
1. You can enable `+Y up` or not. In both cases you need to adjust the transformation on the skeleton asset.
1. Make sure that the GLTF export contains *Animations* and *Skinning* information.
1. Don't disable animation sampling on export.
1. Be aware that GLTF uses 1000 frames per second for all exported animation clips. Blender, by default, uses 24 frames per second. If you want to only use a sub-range of an animation in EZ, you will need to re-calculate the frame indices accordingly. You can set Blender to use 25 or 50 frames per second to make this calculation easier.

## Authoring Meshes

1. Make sure all triangles face into the same direction. Use Blender's `Show Face Normals` viewport option to see whether there are flipped triangles. If there are flipped triangles, they will show up incorrectly in EZ.
1. Blender uses the convention that `+Z` is up, `X` is left/right and `Y` is forward/backward. EZ uses the convention that `+X` is forward, `+Y` is right and `+Z` is up. No matter whether you export the GLTF with Y up or Z up, the necessary transformation can easily be applied either in the [mesh asset](../../graphics/meshes/mesh-asset.md) for static meshes or in the skeleton asset for animated meshes.

## Authoring Animations

1. EZ only supports skeletal animations via skinned meshes. That means every vertex in the mesh needs to have a bone assigned via vertex weights. Blender can move entire objects through bone animations, but if they are only parented to a bone, and don't use vertex skinning (vertex weights), EZ will not show those objects as animated. Use the *vertex weight* visualization in Blender to inspect which vertices are set up properly and which aren't.

1. Be aware that Blender exports ALL keyframes of an animation. The preview window of an animation has no effect on the exported animation data.

1. Blender always sets the first keyframe of all animations to index `1` and that is also how the data is exported. EZ expects the first keyframe to be at index `0`, though. So set the animation range in Blender to start at index `0` and put the first keyframe there.

### Animation Cycles

1. To create an animation that can be repeated, such as walk cycles, the first and the last keyframe must be identical.
1. Furthermore, Blender will typically use cubic interpolation between the keyframes. For the first and last keyframe this will result in an interpolation that slows down and speeds up and is therefore not smooth. The simplest solution is to set these (or all) keyframes to use *linear interpolation* instead.
1. Another option is to insert duplicated dummy keyframes before the first and after the last keyframe, to force the desired interpolation, but then you need to configure the animation clip in EZ to only use the proper sub-range of keyframes, which can be tricky to figure out.

## See Also

* [Back to Index](../../index.md)
* [Skeletal Animations](skeletal-animation-overview.md)