import json
import os
import numpy as np

# 编辑好点名和索引名的对应
PName_idx = {
   1:3,
   2:2,
   3:1,
   4:0,
   5:10,
   6:9,
   7:11,
   8:19,
   9:20,
   10:21,
   11:4,
   12:5,
   13:6,
   14:7,
   15:8,
   16:12,
   17:13,
   18:14,
   19:15,
   20:16,
   21:17,
   22:18
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

k_b2_m_b1 = 1
theta_felt = 15
x_9_10 = 0.1 * (data['end_cap_1']['D6'] - data['end_cap_1']['D4'])

x_1_2 = (data['end_cap_1']['D0']/2 - data['end_cap_1']['d0']/2 + data['felt_1']['d']/2) / 2
all_verts[PName_idx[2]].co = all_verts[PName_idx[1]].co + mathutils.Vector((x_1_2,0,0))
isCertain[2] = True

x_1_3 = data['end_cap_1']['D2']/2
all_verts[PName_idx[3]].co = all_verts[PName_idx[1]].co + mathutils.Vector((x_1_3,0,0))
isCertain[3] = True

y_3_4 = data['end_cap_1']['e']
all_verts[PName_idx[4]].co = all_verts[PName_idx[3]].co + mathutils.Vector((0,y_3_4,0))
isCertain[4] = True

x_1_6 = data['end_cap_1']['D0']/2
all_verts[PName_idx[6]].co = all_verts[PName_idx[1]].co + mathutils.Vector((x_1_6,y_3_4,0))
isCertain[6] = True

x_6_5 = data['end_cap_1']['d0']/2
all_verts[PName_idx[5]].co = all_verts[PName_idx[6]].co + mathutils.Vector((x_6_5,0,0))
isCertain[5] = True
all_verts[PName_idx[7]].co = all_verts[PName_idx[6]].co + mathutils.Vector((-x_6_5,0,0))
isCertain[7] = True


x_1_10 = data['end_cap_1']['D']/2
all_verts[PName_idx[8]].co = all_verts[PName_idx[1]].co + mathutils.Vector((x_1_10-x_9_10,y_3_4,0))
isCertain[8] = True

all_verts[PName_idx[9]].co = all_verts[PName_idx[1]].co + mathutils.Vector((x_1_10-x_9_10,y_3_4+x_9_10,0))
isCertain[9] = True

all_verts[PName_idx[10]].co = all_verts[PName_idx[1]].co + mathutils.Vector((x_1_10,y_3_4+x_9_10,0))
isCertain[10] = True

y_8_11 = data['end_cap_1']['e1']
all_verts[PName_idx[11]].co = all_verts[PName_idx[10]].co + mathutils.Vector((0,y_8_11 - x_9_10,0))
isCertain[11] = True

x_1_12 = data['end_cap_1']['D6']/2
x_12_11 = all_verts[PName_idx[11]].co[0] - x_1_12
all_verts[PName_idx[12]].co = all_verts[PName_idx[11]].co + mathutils.Vector((-x_12_11,x_12_11,0))
isCertain[12] = True

y_8_13 = data['end_cap_1']['m']
all_verts[PName_idx[13]].co = all_verts[PName_idx[12]].co.copy()
all_verts[PName_idx[13]].co[1] = all_verts[PName_idx[8]].co[1] + y_8_13
isCertain[13] = True

x_1_14 = data['end_cap_1']['D4']/2
all_verts[PName_idx[14]].co = all_verts[PName_idx[13]].co.copy()
all_verts[PName_idx[14]].co[0] = all_verts[PName_idx[1]].co[0] + x_1_14
isCertain[14] = True


y_16_17 = k_b2_m_b1 * (data['end_cap_1']['b2'] - data['end_cap_1']['b1'])/2
y_2_22 = y_16_17
y_1_15 = y_2_22 + data['end_cap_1']['b2'] + 2 * y_16_17
all_verts[PName_idx[15]].co = all_verts[PName_idx[14]].co.copy()
all_verts[PName_idx[15]].co[1] = all_verts[PName_idx[1]].co[1] + y_1_15
isCertain[15] = True

x_1_17 = data['end_cap_1']['d1']/2
y_17_18 = data['end_cap_1']['b2']/2 - data['end_cap_1']['b1']/2
x_17_18 = 1/np.tan(np.deg2rad(theta_felt)/2) * y_17_18

all_verts[PName_idx[16]].co = all_verts[PName_idx[15]].co.copy()
all_verts[PName_idx[16]].co[0] = all_verts[PName_idx[1]].co[0] + x_1_17
isCertain[16] = True

all_verts[PName_idx[17]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[17]].co[1] = all_verts[PName_idx[16]].co[1] - y_16_17
isCertain[17] = True

all_verts[PName_idx[18]].co = all_verts[PName_idx[17]].co.copy()
all_verts[PName_idx[18]].co[0] += x_17_18
all_verts[PName_idx[18]].co[1] -= y_17_18
isCertain[18] = True

all_verts[PName_idx[19]].co = all_verts[PName_idx[18]].co.copy()
all_verts[PName_idx[19]].co[1] -= data['end_cap_1']['b1']
isCertain[19] = True

all_verts[PName_idx[20]].co = all_verts[PName_idx[17]].co.copy()
all_verts[PName_idx[20]].co[1] -= data['end_cap_1']['b2']
isCertain[20] = True

all_verts[PName_idx[21]].co = all_verts[PName_idx[20]].co.copy()
all_verts[PName_idx[21]].co[1] -= y_16_17
isCertain[21] = True

all_verts[PName_idx[22]].co = all_verts[PName_idx[2]].co.copy()
all_verts[PName_idx[22]].co[1] += y_2_22
isCertain[22] = True


# 检查
for i in range(1,23):
    if not isCertain[i]:
        raise NotImplementedError("未确定参数：{}".format(i))

print("参数确定完成")
