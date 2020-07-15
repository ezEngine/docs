# PhysX Spherical Joint Component

The *PhysX spherical joint component* is a [joint](physx-joints.md) that links two actors with a *ball and socket constraint*, meaning the actors can rotate around the joint pivot point, but cannot move apart.

<video src="media/spherical-joint.webm" width="600" height="600" autoplay loop></video>

Optionally the amount of rotation that is possible can be limited along the X and Y axis.

## Component Properties

* [Shared Joint Component Properties](physx-joints.md#shared-joint-component-properties)

* `LimitRotation`: If enabled, the cone limit values are used, otherwise they have no effect.
* `ConeLimitY`, `ConeLimitZ`: These two angles make the joint limit how for the child actor may tilt relative to the parent actor. This sets up a (squashed) cone shape within which the child actor may be located. This can be used to prevent unrealistic rotations for stiff objects. Note that the cone limit makes the joint more prone to instability during simulation, so only use it when really needed.

## See Also

* [Back to Index](../../index.md)
* [Physics Joints](physx-joints.md)
