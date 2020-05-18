# Editor Documents

In the editor nearly everything that you work with is a dedicated *document*. Most documents are backed by a file, which is usually in [OpenDDL](https://openddl.org/) format.

Documents are an editor specific representation of things like [scenes](../scenes/scene-editing.md), [prefab (TODO)](../prefabs/prefabs-overview.md), [materials](../materials/materials-overview.md) and so on. The document format is not understood by the runtime and therefore cannot be loaded by applications like [ezPlayer](../tools/player.md) directly.

A document can represent any type of data. However, the most common case is, that it represents data that shall be converted (or *transformed*) from its source representation into something that the engine runtime can use. For example a [texture](../graphics/textures-overview.md) must be transformed from a source *JPG* format to a more optimized *DDS* format. These types of documents are called [assets](../assets/assets-overview.md) in ez and they are by far the most common type of document.

The only exception to documents in the editor are things like [project settings](../projects/project-settings.md) and [editor settings](editor-settings.md), which are not handled by documents.

## See Also

* [Back to Index](../index.md)
* [Assets](../assets/assets-overview.md)
