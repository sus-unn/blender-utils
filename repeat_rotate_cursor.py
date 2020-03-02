import bpy
import bmesh
from mathutils import Matrix
from math import radians


bpy.ops.mesh.duplicate_move()

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
