# PhysX Static Actor Component

The *PhysX static actor component* is used to represent static collision geomtry. Most geometry in a scene should be *static*, meaning that it never moves, rotates, scales or is animated in any way. Static geometry is generally faster to process, and in the case of physics simulations, only static actors may use **concave** collision geometry. 

All [PhysX shapes](../collision-shapes/physx-shapes.md) that can be found in the hierarchy below the static actor are combined to form the compound shape of the actor. However, if any other actor (static or dynamic) is part of the hierarchy below the static actor, the shapes below that object are ignored for this actor. Additionally, if the static actor itself references a [collision mesh](../collision-shapes/collision-meshes.md), it will also become part of the actor compound shape. Only static actors are able to reference concave triangle collision meshes.

If you need your geometry to be able to move, use a [dynamic actor](physx-dynamic-actor-component.md) instead.

## Component Properties

* `CollisionMesh`: An optional convex or concave [collision mesh](../collision-shapes/collision-meshes.md) representing the static actor geometry. This will be combined with all [shapes](../collision-shapes/physx-shapes.md) found in the hierarchy below the owner object.
* `CollisionLayer`: The [collision layer](../collision-shapes/collision-layers.md) defines which objects will collide with this actor.
* `IncludeInNavmesh`: If set, this object will be considered an obstacle for AI and [navmeshes (TODO)](../../ai/recast-navmesh.md) are generated around it.

## See Also

* [Back to Index](../../index.md)
* [PhysX Dynamic Actor Component](physx-dynamic-actor-component.md)
* [PhysX Shapes](../collision-shapes/physx-shapes.md)
* [Collision Meshes](../collision-shapes/collision-meshes.md)
* [Collision Layers](../collision-shapes/collision-layers.md)
