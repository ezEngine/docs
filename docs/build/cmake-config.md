# CMake Setup

To generate a solution, run the CMake GUI. Specify *Where is the source code* and *Where to build the binaries*, then run **Configure**. As a generator, pick *Visual Studio 2017 x64* or *Visual Studio 2019 x64* (or one of the other [Supported Platforms](supported-platforms.md)).

![CMake configuration](media/cmake-config.png)

The screenshot above shows a common setup. Noteworthy are the following points:

* **EZ_ENABLE_QT_SUPPORT** Disable this setting, if you want to compile ez without Qt. This will remove all editor code and several tools from the final solution. The default is "on". When possible the ez CMake scripts will automatically download Qt libraries and set everything up for you. On configurations for which we do not support fully automatic setup, you need to install Qt manually and then set set **EZ_QT_DIR** to its installation folder.

* **EZ_BUILD_FMOD** Enable this, if you want to add fmod sound support to your build. You need to have the fmod prerequisites installed for this to work.

* **EZ_BUILD_PHYSX** Enable this, if you want to add NVidia PhysX support to your build. Once enabled, the next run of "Configure" will automatically download PhysX binaries and set the **EZ_PHYSX_SDK** variable accordingly.

Once you have configured everything, run **Generate** and then **Open Project**.

## Advanced CMake Options

Checking *Advanced* in the CMake GUI will show additional options to configure the ez build. These are mostly used to remove specific 3rd party code (and all dependent features). This is particularly helpful, if you want to build ez on a platform on which one of the dependencies may not compile.

## See Also

* [Supported Platforms](supported-platforms.md)
* [ezEngine As Submodule](submodule.md)
* [Back to Index](../index.md)
