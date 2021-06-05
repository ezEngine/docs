# Shader Debugging

To debug a shader, one can configure it such that the shader compiler includes debugging information. To do so, include **DEBUG** as a platform in the **[PLATFORMS]** section of the shader:

```cpp
[PLATFORMS]

ALL
DEBUG

[PERMUTATIONS]

ALPHATEST
WIREFRAME

[RENDERSTATE]

#if WIREFRAME == 1
  WireFrame = true
#endif

[VERTEXSHADER]

VS_OUT main(VS_IN Input)
{
  ...
}

[PIXELSHADER]

...
```

## See Also

* [Back to Index](../../index.md)
* [Shaders (TODO)](shaders-overview.md)
* [ShaderCompiler](../../tools/shadercompiler.md)
