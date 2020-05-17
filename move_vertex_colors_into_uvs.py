# LICENSE: MIT

import bpy

bl_info = {
    'name': 'Move Vertex Colors into UV channels',
    'author': 'numberkruncher, zardini123',
    'version': (0, 1),
    'blender': (2, 80, 0),
    'description': 'Moves vertex color data into the first two UV Map channels',
    'warning': 'Using this function will overwrite the data in the first two UV Maps.  Use it wisely!!',
    'category': 'Vertex Paint'
}

class MoveVertexColorsWithUVs(bpy.types.Operator):
    bl_label = "Move Vertex Colors into UVs"
    bl_idname = "object.move_vertex_colors_with_uvs"
    bl_description = "Moves vertex color data into the first two UV Map channels"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, "Moving vertex color data with uv1/uv2 data")

        # start in object mode
        obj = bpy.context.view_layer.objects.active
        mesh = obj.data

        # make sure that the object has vertex colors
        if not mesh.vertex_colors.active:
            self.report({"WARNING"}, "Ensure a source vertex color channel is selected on active object!")
            return {"CANCELLED"}

        # make sure that the object has uv data
        while len(mesh.uv_layers.values()) < 2:
            mesh.uv_layers.new()

        # grab the active vertex color data layer
        color_layer = mesh.vertex_colors.active
        # grab the active uv data layer
        uv_layers = mesh.uv_layers.values()

        i = 0
        for poly in mesh.polygons:
            for idx in poly.loop_indices:
                tempR = color_layer.data[i].color[0]  # r
                tempG = color_layer.data[i].color[1]  # g
                tempB = color_layer.data[i].color[2]  # b
                tempA = color_layer.data[i].color[3]  # a

                uv_layers[0].data[i].uv.x = tempR
                uv_layers[0].data[i].uv.y = tempG
                uv_layers[1].data[i].uv.x = tempB
                uv_layers[1].data[i].uv.y = tempA

                i += 1

        # set to vertex paint mode to see the result
        # bpy.ops.object.mode_set(mode='VERTEX_PAINT')

        self.report({'INFO'}, "Finished moving vertex color data with uv1/uv2 data")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MoveVertexColorsWithUVs)
    bpy.context.window_manager.keyconfigs.active.keymaps['Vertex Paint'].keymap_items.new('object.move_vertex_colors_with_uvs',value='PRESS',type='F1',ctrl=True,alt=False,shift=True,oskey=False)

def unregister():
    bpy.utils.unregister_class(MoveVertexColorsWithUVs)

if __name__ == "__main__":
    register()
