import bpy
import mathutils
import math

bpy.ops.object.camera_add(location=(0, -10, 0), rotation=(math.radians(90), 0, 0))

cam = bpy.context.object
cam.data.type = 'ORTHO'
cam.data.ortho_scale = 10  # 根据需要调整视野范围

bpy.context.scene.camera = cam
bpy.ops.view3d.camera_to_view_selected()

bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

bpy.context.scene.render.filepath = "/Users/broyou/Desktop/ME/output/render.png"
bpy.ops.render.render(write_still=True)
