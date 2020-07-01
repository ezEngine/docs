# Sound

The engine doesn't have sound support directly built-in, instead all sound functionality is provided through [plugins](../custom-code/cpp/engine-plugins.md).

## Fmod Plugin

ezEngine comes with support [Fmod](https://www.fmod.com/).

For details, please checkout the [page about Fmod](fmod-overview.md).

## Sound Interface

The class `ezSoundInterface` is an abstract interface that allows you to set some very basic options, like the volume, or the current listener position. These features are mainly needed by the editor such that it can mute sounds and have the editor camera be the listener position, independent of which sound plugin ends up being used.

A game can use this interface to adjust the volume of the entire game or specific channels. For more specific actions you need to query the interface of the actual implementation.

## See Also

* [Back to Index](../index.md)
* [Fmod Integration](fmod-overview.md)
