import json
import os
import numpy as np

# 编辑好点名和索引名的对应
PName_idx = {
   1:0,
   2:5,
   3:2,
   4:3,
   5:4,
   6:1,
   7:6
}


isCertain = {i:False for i in range(1,23)}
isCertain[1] = True

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



y_1_2 = data['bear_1']['B']/2
r = data['bear_1']['d']/2
R = data['bear_1']['D']/2


all_verts[PName_idx[2]].co = all_verts[PName_idx[1]].co + mathutils.Vector((0,-y_1_2,0))
all_verts[PName_idx[3]].co = all_verts[PName_idx[2]].co + mathutils.Vector((r,0,0))
all_verts[PName_idx[4]].co = all_verts[PName_idx[2]].co + mathutils.Vector((R,0,0))

all_verts[PName_idx[7]].co = all_verts[PName_idx[1]].co + mathutils.Vector((0,y_1_2,0))
all_verts[PName_idx[6]].co = all_verts[PName_idx[7]].co + mathutils.Vector((r,0,0))
all_verts[PName_idx[5]].co = all_verts[PName_idx[7]].co + mathutils.Vector((R,0,0))
