import bpy
from bl_ui.generic_ui_list import draw_ui_list


class BookmarkProp(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="name")
    position: bpy.props.FloatVectorProperty(name="position")


class GoToBookmarkOperator(bpy.types.Operator):
    bl_idname = "camera.go_to_bookmark"
    bl_label = "Go to Bookmark"

    def execute(self, context):
        print(f"Going to bookmark number {context.scene.bookmark_list_active_index}")
        # TODO
        return {'FINISHED'}


class BookmarkPanel(bpy.types.Panel):
    bl_label = "Registered camera bookmarks"
    bl_idname = "SCENE_PT_bookmark_list"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Camera Bookmark"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        draw_ui_list(
            layout,
            context,
            list_path="scene.bookmark_list",
            active_index_path="scene.bookmark_list_active_index",
            unique_id="bookmark_list",
        )
        row = layout.row()
        row.operator("camera.go_to_bookmark", text="Go to bookmark")


classes = [
    BookmarkProp,
    BookmarkPanel,
    GoToBookmarkOperator
]

class_register, class_unregister = bpy.utils.register_classes_factory(classes)

def register():
    class_register()
    bpy.types.Scene.bookmark_list = bpy.props.CollectionProperty(type=BookmarkProp)
    bpy.types.Scene.bookmark_list_active_index = bpy.props.IntProperty()


def unregister():
    class_unregister()
    del bpy.types.Scene.bookmark_list
    del bpy.types.Scene.bookmark_list_active_index
    
register()