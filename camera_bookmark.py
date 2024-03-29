import bpy

bl_info = {
    "name": "Camera Bookmark",
    "author": "Valérien",
    "version": (1, 0),
    "blender": (4, 0, 1),
    "location": "View3D > Sidebar > Camera Bookmarks",
    "description": "Allows bookmarking camera positions in Blender.",
    "category": "Camera"
}


class BookmarkProp(bpy.types.PropertyGroup):
    """
    Property group corresponding to a bookmark and storing its name, associated location and rotation.
    """
    name: bpy.props.StringProperty(name="Name")
    position: bpy.props.FloatVectorProperty(name="Position", subtype='XYZ')
    rotation: bpy.props.FloatVectorProperty(name="Rotation", subtype='XYZ')
    focal_length: bpy.props.FloatProperty(name="Focal")


class GoToBookmarkOperator(bpy.types.Operator):
    """
    Operator that jumps to the currently selected (active) bookmark from the bookmark list.
    """
    bl_idname = "camera.go_to_bookmark"
    bl_label = "Go to Bookmark"

    def execute(self, context):
        bookmark_index = context.scene.bookmark_list_active_index
        bookmark = context.scene.bookmark_list[bookmark_index]
        bpy.context.scene.camera.location = bookmark.position
        bpy.context.scene.camera.rotation_euler = bookmark.rotation
        bpy.context.scene.camera.data.angle = bookmark.focal_length
        return {'FINISHED'}


class BookmarkPanel(bpy.types.Panel):
    """
    UI pannel in the N menu for registering bookmarks and jumping to them.
    """
    bl_label = "Camera Bookmarks"
    bl_idname = "VIEW3D_PT_camera_bookmarks"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Camera Bookmarks"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        row = layout.row()
        row.template_list(
            "UI_UL_list",
            "BookmarkList", scene,
            "bookmark_list", scene,
            "bookmark_list_active_index"
        )
        col = row.column(align=True)
        col.operator("camera.add_bookmark", text="", icon='ADD')
        col.operator("camera.remove_bookmark", text="", icon='REMOVE')
        layout.operator("camera.go_to_bookmark",
                        text="Go to Selected Bookmark")


class AddBookmarkOperator(bpy.types.Operator):
    bl_idname = "camera.add_bookmark"
    bl_label = "Add Bookmark"

    def execute(self, context):
        scene = context.scene
        camera = context.scene.camera
        if camera is not None:
            bookmark = scene.bookmark_list.add()
            bookmark.name = "Bookmark " + str(len(scene.bookmark_list))
            bookmark.position = camera.location.copy()
            bookmark.rotation = camera.rotation_euler.copy()
            bookmark.focal_length = camera.data.angle
        return {'FINISHED'}


class RemoveBookmarkOperator(bpy.types.Operator):
    bl_idname = "camera.remove_bookmark"
    bl_label = "Remove Bookmark"

    @classmethod
    def poll(cls, context):
        return context.scene.bookmark_list_active_index != -1

    def execute(self, context):
        scene = context.scene
        scene.bookmark_list.remove(scene.bookmark_list_active_index)
        context.scene.bookmark_list_active_index = min(max(0, context.scene.bookmark_list_active_index - 1),
                                                       len(scene.bookmark_list) - 1)
        return {'FINISHED'}


classes = [
    BookmarkProp,
    BookmarkPanel,
    GoToBookmarkOperator,
    AddBookmarkOperator,
    RemoveBookmarkOperator
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.bookmark_list = bpy.props.CollectionProperty(
        type=BookmarkProp)
    bpy.types.Scene.bookmark_list_active_index = bpy.props.IntProperty(
        default=-1)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.bookmark_list
    del bpy.types.Scene.bookmark_list_active_index


if __name__ == "__main__":
    register()
