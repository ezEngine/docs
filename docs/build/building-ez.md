# Building ezEngine

To try out ezEngine, you can download a [precompiled binary package](https://github.com/ezEngine/ezEngine/releases). This article describes how you can build the engine yourself, which enables you to extend the engine with custom functionality.

## Getting the Code and Data

1. Clone a branch from [the GitHub repository](https://github.com/ezEngine/ezEngine).
    * If you need a good git GUI, have a look at [Fork](https://git-fork.com/).
    * If you want a stable release, clone the 'release' branch.
    * If you want the latest features, clone the 'dev' branch.
1. Unless your git client already checks out git sub-modules for you, also run `git submodule init` and `git submodule update` in your local clone. The EZ project uses submodules to deliver additional data such as [sample content](https://github.com/ezEngine/content) and [precompiled tools](https://github.com/ezEngine/precompiled-tools).

## Regular Builds

1. Obtain and install all [prerequisites](build-prerequisites.md)
1. Run CMake and [configure your build](cmake-config.md)
1. Open the generated solution and build. Compiling the entire solution with editor, unit tests and samples takes around 5 minutes. The dependencies are set up such that only building, e.g. the *Editor* project will include all requirements, though.

## Other Builds

* [UWP Builds](build-uwp.md)
* [Linux Builds](build-linux.md)
* [MacOS Builds](build-macos.md)
* [Android Builds](build-android.md)
* [Building with Clang on Windows](clang-on-windows.md)

## See Also

* [Back to Index](../index.md)
* [Supported Platforms](supported-platforms.md)
* [ezEngine as a Submodule](submodule.md)
