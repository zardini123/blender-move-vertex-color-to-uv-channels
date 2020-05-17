# Move Vertex Color to UV Map channels (Blender 2.8 Add-on)

This add-on provides users with a function to transfer the currently selected vertex color data into two UV Maps.

This is extremely useful models for Unity. Unity only imports and provides one vertex color channel per mesh (see [Unity's Mesh API and notice how there is only one color property](https://docs.unity3d.com/ScriptReference/Mesh.html)). Though, Unity does provide up to 8 uv maps. Therefore, this add-on relocates extra vertex color data into that available UV data.

The remapping looks something like this:
```
uv.x = vertex_color.r
uv.y = vertex_color.g
uv2.x = vertex_color.b
uv2.y = vertex_color.a
```

**Currently, this add-on replaces all data in the first two UV Maps in Blender!!** If you find a use for having the first UV map, and the extra vertex color data, let me know. Or, you can also implement it and provide a pull request :)

## Credit

This originally created by _numberkruncher_, posted on Unity Answers back in 2016 ([see post here](http://answers.unity.com/answers/1243374/view.html)). I updated the script for Blender 2.8, and adjusted the script to move the vertex data instead of swap. He originally designed the script to run when user uses shortcut _Ctrl+Shift+F1_ and that code is still in the add-on. I have no idea if the hotkey works still...

## Installation

1. Download move_vertex_colors_into_uvs.py
2. Go to _Preferences View -> Add-ons_ and click _Install_
3. Navigate to your download of move_vertex_colors_into_uvs.py and select

## Usage

1. Make the object you want to work on as the active object (select it).
2. Select the vertex color channel you want to move to UV's in _Object Data Properties (mesh-looking button) -> Vertex Colors_.
3. Search for the function (_Move Vertex Colors into UVs_) using the search function in Blender.

Once the mesh is imported into Unity, the vertex color data in the 2 UV channels can easily be accessed using the [_UV_ Node](https://docs.unity3d.com/Packages/com.unity.shadergraph@8.1/manual/UV-Node.html) in [Shader Graph](https://unity.com/shader-graph). With UV0 selected, the Node already combines the mesh's uv and uv2 into a Vector4 (which is essentially RGBA). Awesome!

![UV Node](https://bitinn.github.io/ScriptableRenderPipeline/ShaderGraph/images/UVNodeThumb.png)
