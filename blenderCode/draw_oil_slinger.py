import json
import os
import numpy as np

# 编辑好点名和索引名的对应
PName_idx = {
   1:0,
   2:1,
   3:2,
   4:4,
   5:5,
   6:3,
   7:6
}


root_dir = "/Users/broyou/Desktop/ME/gear_design"
with open(os.path.join(root_dir, "design.json"), "r") as f:
    data = json.load(f)

import bpy
import mathutils

# 编辑模式下
bpy.ops.object.mode_set(mode='OBJECT')
obj = bpy.context.object
mesh = obj.data
all_verts = mesh.vertices

bear_name = 'bear_3'

r = data[bear_name]['d']/2
R = data[bear_name]['D']/2

b = data['box']['to_oil_slinger'] + data['box']['to_bear_in']

x_2_5 = (3*R + r)/4 - r
x_2_3 = 0.5 * x_2_5
x_4_5 = x_2_5 - x_2_3
y_3_4 = 0.5 * b
y_5_6 = b - y_3_4

all_verts[PName_idx[2]].co = all_verts[PName_idx[1]].co + mathutils.Vector((r,0,0))
all_verts[PName_idx[3]].co = all_verts[PName_idx[2]].co + mathutils.Vector((x_2_3,0,0))
all_verts[PName_idx[4]].co = all_verts[PName_idx[3]].co + mathutils.Vector((0,y_3_4,0))
all_verts[PName_idx[5]].co = all_verts[PName_idx[4]].co + mathutils.Vector((x_4_5,0,0))
all_verts[PName_idx[6]].co = all_verts[PName_idx[5]].co + mathutils.Vector((0,y_5_6,0))
all_verts[PName_idx[7]].co = all_verts[PName_idx[2]].co + mathutils.Vector((0,b,0))

