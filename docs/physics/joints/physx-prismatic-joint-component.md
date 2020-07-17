# PhysX Prismatic Joint Component

The *PhysX prismatic joint component* is a [joint](physx-joints.md) that links two actors such that they can only slide along one axis relative to each other.

<video src="media/prismatic-joint.webm" width="600" height="600" autoplay loop></video>

Optionally, how for the joined actors can slide can be limited. 

## Component Properties

* [Shared Joint Component Properties](physx-joints.md#shared-joint-component-properties)

* `LimitMode`: Specifies whether the distance of sliding is limited and how.
  * `NoLimit`: The actors can slide unlimited far. Since they will still collide with other objects, there may be no need to limit the slide distance through the joint.
  * `HardLimit`: When the actors reach the end of the joint range, they will be stopped. In this mode `SpringStiffness` is a restitution value that defines how much the actor will bounce back. `SpringDamping` is a force theshold, if the actor hits the limit with less force than this, it will not bounce back, making it a bit sticky.
  * `SoftLimit`: When the actors pass the joint limits, they will not be stopped. Instead, a spring will start pulling them back together.
* `LowerLimit`, `UpperLimit`: How far the joined actors can move apart before being stopped or pulled back.
* `SpringStiffness`: In soft limit mode, this value (`[0; inf]` range) defines how strongly the spring will pull the actors. In hard limit mode, this is a restitution value (`[0; 1]` range) that affects how strongly the actor will bounce back when hitting the limit.
* `SpringDamping`: In soft limit mode, this dampens the spring, to prevent oscilation. In hard limit mode, this is a force threshold. If the actor hits the limit with less force than this, it will not bounce back.

## See Also

* [Back to Index](../../index.md)
