# Root Motion

<!-- PAGE IS TODO -->

## Root Motion Modes

* `Ignore`: No root motion is applied, the game object will not be moved by the animation.

* `ApplyToOwner`: Any available root motion is directly applied to the game object and thus moves it without restriction. This mode is useful for objects that have to follow a fixed path. For example moving platforms (which are *kinematic* [physics actors](../../physics/actors/physx-dynamic-actor-component.md)), or objects that don't physically interact with the player. This mode is not suited for characters that should obey physical restrictions.

* `SendMoveCharacterMsg`: If this mode is used, root motion is not applied to any object, instead the [message](../../runtime/world/world-messaging.md) `ezMsgMoveCharacterController` is sent to the *top most game object* in the hierarchy. This way, if there is also a [character controller](../../physics/special/physx-character-controller.md) or other component that accepts this type of message, it can apply the root motion.

## See Also

* [Back to Index](../../index.md)
* [Skeletal Animations](skeletal-animation-overview.md)
