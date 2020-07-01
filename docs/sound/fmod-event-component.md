# Fmod Event Component

The *Fmod event component* creates an instance of an Fmod event. An event is usually a 2D or 3D sound, but can also be an environmental effect that changes how other sounds are perceived. Fmod events are very powerful, which is why ezEngine doesn't need to have a large feature set of audio features. No matter what you want to do, pretty much anything is available through Fmod events.

A description of Fmod events is out of scope for this documentation. Please see [Using Fmod Studio](fmod-overview.md#using-fmod-studio) for learning resources.

Fmod event components reference [sound event assets](fmod-soundevent-asset.md). The component plays the referenced sound. If the Fmod event has looping regions, the sound will play indefinitely, until it is stopped programmatically, or the component is deleted. There is no looping option on the component, since this feature controlled through Fmod Studio.

Advanced Fmod features, like *sound cues* and adjusting *event parameters* are only accessible programmatically (C++ or TypeScript). For details please see the [API Docs](../getting-started/api-docs.md) about `ezFmodEventComponent`.

## Sound Occlusion

By default sounds are only attenuated by distance. Fmod doesn't have a representation of the 3D geometry and therefore can't muffle or disable sounds when they are (visually) occluded.

The event component allows you to enable a simple physics raycast based heuristic to determine whether a sound source is occluded by a wall or larger obstacle. If enabled, the occlusion factor is computed and the Fmod event parameter `Occlusion` is passed into the event. It is your responsibility to set up the Fmod event such that this parameter exists and is used to adjust the event's volume.

## Component Properties

* `Paused`: If set, the referenced sound won't start playing at start. Toggling this value programmatically will pause/resume a playing sound.
* `Volume`: Adjusts the volume for this sound.
* `Pitch`: Higher pitch means the sound plays faster, a lower pitch makes it play slower (and at lower frequency).
* `SoundEvent`: The [sound event asset](fmod-soundevent-asset.md) that will be played by this component.
* `UseOcclusion`: If enabled, the component will use physics raycasts to determine whether the sound source is occluded by geometry. The occlusion factor is passed to the Fmod event as the event parameter `Occlusion`.
* `OcclusionThreshold`: How strongly the sound source must be occluded, before the occlusion value will be larger than zero.
* `OcclusionCollisionLayer`: The physics [collision layer](../physics/collision-shapes/collision-layers.md) to use for the occlusion raycasts.
* `OnFinishedAction`: For sounds that end by themselves, this option allows you to specify whether the component should delete itself or its entire object afterwards.
* `ShowDebugInfo`: If enabled, the component displays some statistics about its state.

## See Also

* [Back to Index](../index.md)
