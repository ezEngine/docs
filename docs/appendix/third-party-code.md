# ThirdParty Code

This page lists which third party code and data is used by ez.

## Assimp

Link: [http://www.assimp.org](http://www.assimp.org)

Compile switch: None (hard dependency for the asset processing)

Open Asset Import Library, a portable Open Source library to import various well-known 3D model formats in a uniform manner.

## Dear Imgui

Link: [https://github.com/ocornut/imgui](https://github.com/ocornut/imgui)

Compile switch: **EZ_3RDPARTY_IMGUI_SUPPORT**

A nice library for easily creating ingame GUIs.

## DirectXTex

Link: [https://github.com/Microsoft/DirectXTex](https://github.com/Microsoft/DirectXTex)

Compile switch: Currently none

Used by ezImage and the ezTexConv tool for GPU-enabled block compression.

## Duktape

Link: [https://duktape.org](https://duktape.org)

Compile switch: **EZ_3RDPARTY_DUKTAPE_SUPPORT**

Duktape is an embeddable Javascript engine, with a focus on portability and compact footprint.
It can be used directly or through ezDuktapeWrapper. Non-essential for the engine, but scripting functionality (using [TypeScript](https://www.typescriptlang.org/)) is built on top of it.

## Enet

Link: [http://enet.bespin.org](http://enet.bespin.org)

Compile switch: **EZ_3RDPARTY_ENET_SUPPORT**

An efficient and easy to use networking library, built on top of the UDP protocoll. It is used by ezTelemetry to interact with the ezInspector, and it is also used to implement the file serving functionality.

## Fmod 2.x

Link: [https://www.fmod.com](https://www.fmod.com)

Compile switch: **EZ_BUILD_FMOD**

ez has an integration for the Fmod sound system. However, you need to download the SDK yourself.

1. Go to [fmod.com](https://www.fmod.com)
1. Sign up / log in
1. Download and install the Fmod Studio API for the desired platforms
1. For editing sounds you also need to download and install the Fmod Studio Tool
1. In CMake, enable the Fmod compile switch
1. Recompile ezEngine

## jc_voronoi

Link: [https://github.com/JCash/voronoi/blob/dev/src/jc_voronoi.h](https://github.com/JCash/voronoi/blob/dev/src/jc_voronoi.h)

Compile switch: None

A fast single file 2D voronoi diagram generator. Used by ezBreakableSheetComponent.

## Lua

Link: [(http://www.lua.org](http://www.lua.org)

Compile switch: **EZ_3RDPARTY_LUA_SUPPORT**

The Lua scripting language. Can be used directly or through ezLuaWrapper for easier access to common functionality. Non-essential for ez, only the ingame console interpreter would stop working without it.

## Mikktspace

Link: [http://mmikkelsen3d.blogspot.ie](http://mmikkelsen3d.blogspot.ie)

Compile switch: None (hard dependency for the asset processing)

Tangent space generation code by Morten S. Mikkelsen. See [https://wiki.blender.org/index.php/Dev:Shading/Tangent_Space_Normal_Maps](https://wiki.blender.org/index.php/Dev:Shading/Tangent_Space_Normal_Maps) for more information. It is used by ezGeometry.

## PhysX 4.1.1

Link: [https://github.com/NVIDIAGameWorks/PhysX](https://github.com/NVIDIAGameWorks/PhysX)

Compile switch: **EZ_BUILD_PHYSX**

NVIDIA PhysX is used to provide collision detection, physics simulation, character controllers and other interactions.

To build PhysX yourself:

1. Checkout **https://github.com/NVIDIAGameWorks/PhysX.git**
1. Goto **physx/buildtools/presets/public** and open all presets that you want to build and change or add\
\<cmakeSwitch name="NV_USE_STATIC_WINCRT" value="False" comment="Use the statically linked windows CRT" />\
\<cmakeSwitch name="NV_USE_DEBUG_WINCRT" value="True" comment="Use the debug version of the CRT" />
1. **Run physx/generate_projects.bat** for every configuration you want to build
1. Open **physx/compiler/.../PhysXSDK.sln** and compile **CMakePredefinedTargets/INSTALL** for both debug and release
1. Uwp installs are missing two include folders: **PhysX/include/cudamanager** and **PhysX/include/gpu** so copy those from **physx/include** to **physx/install/.../PhysX/include**
1. The content of the built configuration in **physx/install** is now ready to be consumed by ezEngine by pointing the advanced cmake var **EZ_PHYSX_SDK** to it.

## Qt 5

Link: [https://www.qt.io](https://www.qt.io)

Compile switch: **EZ_ENABLE_QT_SUPPORT**

Used for all desktop GUI code in the editor and tools.

## Qt Advanced Docking System

Link [https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System)

Compile switch **EZ_3RDPARTY_ADS_SUPPORT**

A docking system for Qt similiar to the one in visual studio. Used by the editor and inspector applications.

## Recast

Compile switch: **EZ_3RDPARTY_RECAST_SUPPORT**

Link: [https://github.com/recastnavigation/recastnavigation](https://github.com/recastnavigation/recastnavigation)

A library to generate navigation meshes from arbitrary 3D geometry.

## RenderDoc

Link: [https://renderdoc.org](https://renderdoc.org)

Compile switch: **EZ_3RDPARTY_RENDERDOC_SUPPORT**
  
RenderDoc is a free MIT licensed stand-alone graphics debugger. The ezRenderDocPlugin enables full control over taking RenderDoc snapshots from within the engine.

## SFML

Link: [http://www.sfml-dev.org](http://www.sfml-dev.org)

Compile switch: **currently none (TODO)**

This library provides a simple and portable interface for window creation, input handling and more. Used by ezWindow and ezStandardInputDevice on non-Windows platforms (Mac, Linux).

## Silk Icons

Link: [http://www.famfamfam.com/lab/icons/silk](http://www.famfamfam.com/lab/icons/silk)

Icons from this set are used by the tools.

## stb

Link: [https://github.com/nothings/stb](https://github.com/nothings/stb)

Compile switch: None

Public domain licensed code by Sean Barrett. Used by ezImage to read and write some of the supported formats like PNG and JPEG.

## UTF8-CPP

Link: [https://github.com/nemtrif/utfcpp](https://github.com/nemtrif/utfcpp)

Compile switch: None

A library that provides Unicode related functionality. Integrated directly into ezFoundation.

## xxHash

Link: [https://github.com/Cyan4973/xxHash](https://github.com/Cyan4973/xxHash)

Compile switch: None

A very fast hash algorithm. Integrated directly into ezFoundation.

## zLib

Link: [http://www.zlib.net](http://www.zlib.net)

Compile switch: **EZ_3RDPARTY_ZLIB_SUPPORT**

Provides algorithms for zip compression and decompression. It is used by ezCompressedStreamReaderZlib and ezCompressedStreamWriterZlib in ezFoundation.

## zstd

Link: [https://facebook.github.io/zstd](https://facebook.github.io/zstd)

Compile switch: **EZ_3RDPARTY_ZSTD_SUPPORT**

A very fast lossless compression library. It is used by ezCompressedStreamReaderZstd and ezCompressedStreamWriterZstd and also by ezArchive.

## See Also

* [Back to Index](../index.md)
