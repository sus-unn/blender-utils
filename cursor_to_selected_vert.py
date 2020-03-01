import bpy

area = bpy.context.area
old_type = area.type
area.type = 'VIEW_3D'
original_cursor_coord = bpy.context.scene.cursor.location[:]
bpy.ops.view3d.snap_cursor_to_selected()
bpy.ops.object.editmode_toggle()
bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
bpy.ops.object.editmode_toggle()
bpy.context.scene.cursor.location = original_cursor_coord 
area.type = old_type
