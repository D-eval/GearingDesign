import json
import os
import numpy as np

# 编辑好点名和索引名的对应

PName_idx = {
   1:3,
   2:2,
   3:1,
   4:0,
   5:4,
   6:5,
   7:6,
   8:7,
   9:8,
   10:9,
   11:10,
   12:11
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

l_interval = data['shaft']['l_interval']
l_5_6 = 5

# 计算箱体宽度
box_width = 2*data['box']['Delta_2'] + data['gear_pair_1']['b2_big'] + data['gear_pair_2']['b3_big'] + (data['gear_pair_1']['b1_small']-data['gear_pair_1']['b2_big'])/2 + (data['gear_pair_2']['b2_small']-data['gear_pair_2']['b3_big'])/2 + data['box']['Delta_3']

x_1_2 = data['bear_3']['d']/2


all_verts[PName_idx[2]].co = all_verts[PName_idx[1]].co.copy()
all_verts[PName_idx[2]].co[0] += x_1_2


y_shaft_end_to_box_in = (data['bear_3']['B'] - data['box']['shaft_to_bear']) + data['box']['to_bear_in']
y_2_3 = l_interval + y_shaft_end_to_box_in + data['box']['Delta_2'] + (data['gear_pair_2']['b2_small'] - data['gear_pair_2']['b3_big'])/2

all_verts[PName_idx[3]].co = all_verts[PName_idx[2]].co.copy()
all_verts[PName_idx[3]].co[1] -= y_2_3

all_verts[PName_idx[4]].co = all_verts[PName_idx[3]].co.copy()
all_verts[PName_idx[4]].co[0] += l_interval

y_4_5 = data['gear_pair_2']['b3_big'] - l_interval

all_verts[PName_idx[5]].co = all_verts[PName_idx[4]].co.copy()
all_verts[PName_idx[5]].co[1] -= y_4_5

all_verts[PName_idx[6]].co = all_verts[PName_idx[5]].co.copy()
all_verts[PName_idx[6]].co[0] += l_5_6

y_6_7 = box_width - 2 * data['box']['to_oil_slinger'] - (data['box']['Delta_2'] + (data['gear_pair_2']['b2_small'] - data['gear_pair_2']['b3_big'])/2) - data['gear_pair_2']['b3_big']

all_verts[PName_idx[7]].co = all_verts[PName_idx[6]].co.copy()
all_verts[PName_idx[7]].co[1] -= y_6_7

all_verts[PName_idx[8]].co = all_verts[PName_idx[7]].co.copy()
all_verts[PName_idx[8]].co[0] -= l_5_6 + l_interval

y_8_9 = data['box']['to_oil_slinger'] + data['box']['B'] + data['end_cap_3']['e'] + 3

all_verts[PName_idx[9]].co = all_verts[PName_idx[8]].co.copy()
all_verts[PName_idx[9]].co[1] -= y_8_9

all_verts[PName_idx[10]].co = all_verts[PName_idx[9]].co.copy()
all_verts[PName_idx[10]].co[0] = all_verts[PName_idx[1]].co[0] + data['coupling_2']['d1']/2

all_verts[PName_idx[11]].co = all_verts[PName_idx[10]].co.copy()
all_verts[PName_idx[11]].co[1] -= 50


all_verts[PName_idx[12]].co = all_verts[PName_idx[11]].co.copy()
all_verts[PName_idx[12]].co[0] = all_verts[PName_idx[1]].co[0]
