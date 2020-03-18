# ezEngine As Submodule

When using git and cmake for a project ezEngine can be integrated as a submodule into the git repository and be reference from cmake.

First ezEngine needs to be added as a submodule to git:

``` git submodule add https://github.com/ezEngine/ezEngine.git```

Next add the ezEngine folder in your root CMakeLists.txt:

``` add_subdirectory(ezEngine)```

The ezEngine language detection can be reused by including the ezEngine submodule utility file:

```
# include the ez submodule utility cmake functions
include("ezEngine/Code/BuildSystem/CMake/ezUtilsSubmodule.cmake")

ez_detect_languages()

project("MyProject" LANGUAGES ${EZ_LANGUAGES})
```

For a full example see: https://github.com/ezEngine/submodule-example

## See Also

* [CMake Setup](cmake-config.md)
* [Back to Index](../index.md)