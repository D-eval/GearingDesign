import json
import os
import numpy as np

root_dir = "/Users/broyou/Desktop/ME/gear_design"
with open(os.path.join(root_dir, "design.json"), "r") as f:
    data = json.load(f)

import bpy
import bmesh
import mathutils

# 编辑模式下
bpy.ops.object.mode_set(mode='OBJECT')
obj = bpy.context.object
mesh = obj.data
all_verts = mesh.vertices

def mirror(idx_dict, dim, x):
    for k,v in idx_dict.items():
        all_verts[k].co = all_verts[v].co.copy()
        all_verts[k].co[dim] = 2*x - all_verts[k].co[dim]

def stretch(idx_dict, dim, x):
    for k,v in idx_dict.items():
        all_verts[k].co = all_verts[v].co.copy()
        all_verts[k].co[dim] += x

def stretch_n(idx_target,idx_refer,n,x):
    all_verts[idx_target].co = all_verts[idx_refer].co.copy()
    v = n * x
    for i in range(3):
        all_verts[idx_target].co[i] += v[i]
 
# 从左下角开始,逆时针
def rectangle_n(lst,e1,e2,a,b):
    all_verts[lst[1]].co = all_verts[lst[0]].co.copy()
    all_verts[lst[2]].co = all_verts[lst[0]].co.copy()
    all_verts[lst[3]].co = all_verts[lst[0]].co.copy()
    r_0_1 = a * e1
    r_1_2 = b * e2
    r_2_3 = -a * e1
    for i in range(3):
        all_verts[lst[1]].co[i] += r_0_1[i]
        all_verts[lst[2]].co[i] += r_0_1[i] + r_1_2[i]
        all_verts[lst[3]].co[i] += r_0_1[i] + r_1_2[i] + r_2_3[i]

def offset_n(idx,e,x):
    r = e * x
    for i in range(3):
        all_verts[idx].co[i] += r[i]

