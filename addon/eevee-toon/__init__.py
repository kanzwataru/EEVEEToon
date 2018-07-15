bl_info = {
    "name" : "EEVEE NPR",
    "category" : "Material",
    "version" : (0, 1, 0),
    "blender" : (2, 80, 0)
}

import bpy
import os

ADDON_PATH = os.path.dirname(__file__)

def import_from_library(library):
    path = os.path.join(ADDON_PATH, library + '.blend')
    with bpy.data.libraries.load(path) as (data_from, data_to):
        data_to.node_groups = [x for x in data_from.node_groups if not x in bpy.data.node_groups]
    
    for datablock in data_to.node_groups:
        datablock.use_fake_user = True

class AppendBaseNprNodes(bpy.types.Operator):
    """ Append Eevee NPR base nodes for creating shaders """
    bl_idname = "material.append_base_npr_nodes"
    bl_label = "Append Eeevee NPR Base Nodes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        import_from_library('base_nodes');
        return {'FINISHED'}

class AppendExtraNprNodes(bpy.types.Operator):
    """ Append sample Eeevee NPR shaders """
    bl_idname = "material.append_extra_npr_nodes"
    bl_label = "Append Eeevee NPR Sample Shaders"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        import_from_library('extra_shaders');
        return {'FINISHED'}

class EeveeNprPanel(bpy.types.Panel):
    bl_label = "Eevee Toon"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("material.append_base_npr_nodes")
        col.operator("material.append_extra_npr_nodes")

def register():
    bpy.utils.register_class(AppendBaseNprNodes)
    bpy.utils.register_class(AppendExtraNprNodes)
    bpy.utils.register_class(EeveeNprPanel)
    
def unregister():
    bpy.utils.unregister_class(AppendBaseNprNodes)
    bpy.utils.unregister_class(AppendExtraNprNodes)
    bpy.utils.unregister_class(EeveeNprPanel)

if __name__ == "__main__":
    register()