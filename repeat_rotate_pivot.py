import bpy
import bmesh
from mathutils import Matrix
from math import radians


bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

context = bpy.context
scene = context.scene
pp = bpy.context.scene.cursor.location
ob = context.edit_object
me = ob.data
bm = bmesh.from_edit_mesh(me)
S = ob.matrix_world.copy()
S.translation -= pp
R = Matrix.Rotation(radians(22.5), 3, (0, 0, 1))

bmesh.ops.rotate(bm, 
        matrix=R, 
        verts=[v for v in bm.verts if v.select],
        space=S)

bmesh.update_edit_mesh(me)
