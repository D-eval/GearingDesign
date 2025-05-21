import json
import os


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

# 轴肩 0.1 * d

import numpy as np
# 分度圆算基圆
def cal_base_d(d):
    alpha = 20
    return np.cos(np.deg2rad(alpha)) * d

# 命名规范:
# 轴向用l
# 半径用R
# 轴肩用h


# 计算箱体宽度
box_width = 2*data['box']['Delta_2'] + data['box']['Delta_3'] + data['gear_pair_1']['b2_big'] + data['gear_pair_2']['b3_big'] + (data['gear_pair_1']['b1_small']-data['gear_pair_1']['b2_big'])/2 + (data['gear_pair_2']['b2_small']-data['gear_pair_2']['b3_big'])/2


def mirror(idx_dict, dim, x):
    for k,v in idx_dict.items():
        all_verts[k].co = all_verts[v].co.copy()
        all_verts[k].co[dim] = 2*x - all_verts[k].co[dim]

def stretch(idx_dict, dim, x):
    for k,v in idx_dict.items():
        all_verts[k].co = all_verts[v].co.copy()
        all_verts[k].co[dim] += x

# 右上角顺时针
def rectangle(lst, x, y, dim1, dim2):
    all_verts[lst[1]].co = all_verts[lst[0]].co.copy()
    all_verts[lst[1]].co[dim1] += x
    all_verts[lst[2]].co = all_verts[lst[1]].co.copy()
    all_verts[lst[2]].co[dim2] -= y
    all_verts[lst[3]].co = all_verts[lst[2]].co.copy()
    all_verts[lst[3]].co[dim1] -= x


A1 = data['sight_hole_cover']['A1']
B1 = data['sight_hole_cover']['B1']
A2 = data['sight_hole_cover']['A2']
B2 = data['sight_hole_cover']['B2']
h = data['sight_hole_cover']['h']

rectangle([2,3,1,0],A1,B1,0,1)
stretch({4:0,5:1,6:2,7:3},2,h)

x_6_8 = (A1-A2)/2
y_6_8 = (B1-B2)/2

all_verts[8].co = all_verts[6].co.copy()
all_verts[8].co[0] += x_6_8
all_verts[8].co[1] -= y_6_8

rectangle([8,11,10,9],A2,B2,0,1)