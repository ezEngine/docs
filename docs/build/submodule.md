# ezEngine as a Submodule

When using git and CMake for a project, ezEngine can be integrated as a submodule into the git repository and reference from CMake.

First ezEngine needs to be added as a submodule to git:

```cmd
git submodule add https://github.com/ezEngine/ezEngine.git
```

Next, add the ezEngine folder in your root `CMakeLists.txt`:

```cmake
add_subdirectory(ezEngine)
```

The ezEngine language detection can be reused by including the ezEngine submodule utility file:

```cmake
# include the ez submodule utility CMake functions
include("ezEngine/Code/BuildSystem/CMake/ezUtilsSubmodule.cmake")

ez_detect_languages()

project("MyProject" LANGUAGES ${EZ_LANGUAGES})
```

For a full example see: [https://github.com/ezEngine/submodule-example](https://github.com/ezEngine/submodule-example)

## See Also

* [Back to Index](../index.md)
* [CMake Setup](cmake-config.md)
