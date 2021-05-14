# Blackboard Component

The *blackboard component* contains a [blackboard](blackboards.md). The component itself doesn't have any notable functionality. Instead it is used as the central storage, through which other systems can share their data and communicate.

If a system requires a blackboard, it will typically search for a blackboard component by traversing its own object structure upwards (in C++ you can use `ezBlackboardComponent::FindBlackboard()` to do so).

For example the [animation controller](../animation/skeletal-animation/animation-controller/animation-controller-overview.md) is controlled by modifying blackboard entries, which the controller reads. You can modify the entries through [custom code](../custom-code/custom-code-overview.md). For this, the blackboard component has to be attached either to the same object, or a parent object.

## Properties

* `BlackboardName`:

* `ShowDebugInfo`:

* `SendEntryChangedMessage`:

* `Entries`:

## See Also

* [Back to Index](../index.md)
* [Blackboards](blackboards.md)
* [Animation Controller](../animation/skeletal-animation/animation-controller/animation-controller-overview.md)
