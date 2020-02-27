# Building with Clang on Windows

You can build ezEngine using the Clang front-end on Windows through Visual Studio. This can be useful to find and fix compilation errors and warnings, that do not happen with MSVC. However, as Clang support on Windows is still experimental, you may not be able to build a working executable.

## Using the CMake GUI

1. Create a new solution for the Clang build by pointing *Where to build the binaries* to a new location.
1. Press **Configure** once, a dialog will show up.
1. Choose the desired Visual Studio generator at the top.
1. In the field **Optional toolset to use (argument to -T)** type **v140_clang_c2**
1. Finish the dialog and run 'Configure'.
1. Check the **Advanced** checkbox to show additional options.
1. **Disable EZ_USE_PCH**, as the Clang build will not work with precompiled headers.
1. You may also want to **disable EZ_ENABLE_FOLDER_UNITY_FILES** as that makes it easier to see from which file a compilation error originated.
1. Finish the [CMake configuration](cmake-config.md), open the solution in Visual Studio and start compiling.

## See Also

* [Building ezEngine](building-ez.md)
* [Back to Index](../index.md)
