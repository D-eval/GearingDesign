import json
import os

# 编辑好点名和索引名的对应
PName_idx = {
   "shaft_1":
       {1:0,
        2:1,
        3:3,
        4:2,
        5:4,
        6:5,
        7:6,
        8:7,
        9:8,
        10:9,
        11:10,
        12:11,
        13:12,
        14:13
       },
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
    return d
    # alpha = 20
    # return np.cos(np.deg2rad(alpha)) * d

# 命名规范:
# 轴向用l
# 半径用R
# 轴肩用h


class Parser:
    def __init__(self,str):
        dirName, ref, target = str.split('_')
        self.dirName = dirName
        self.ref = int(ref)
        self.target = int(target)

# 计算箱体宽度
box_width = 2*data['box']['Delta_2'] + data['box']['Delta_3'] + data['gear_pair_1']['b2_big'] + data['gear_pair_2']['b3_big'] + (data['gear_pair_1']['b1_small']-data['gear_pair_1']['b2_big'])/2 + (data['gear_pair_2']['b2_small']-data['gear_pair_2']['b3_big'])/2

dimentions = {
    "shaft_1":{},
}

k_shoulder = 0.07

dimentions['shaft_1']["x_1_2"]=data['coupling']['d1']/2 # 联轴器孔半径
dimentions['shaft_1']["y_2_3"]=40
dimentions['shaft_1']["x_3_4"]=data['bear_1']['d']/2 - data['coupling']['d1']/2
dimentions['shaft_1']["y_4_5"]=data['box']['B'] + data['end_cap_1']['e'] + data['box']['to_oil_slinger'] + 3
dimentions['shaft_1']["x_5_6"]=data['bear_1']['d'] * k_shoulder # 定位轴肩,用甩油环定位轴
dimentions['shaft_1']["y_6_7"]=box_width - data['box']['Delta_2'] - data['gear_pair_1']['b1_small'] - data['box']['to_oil_slinger']
dimentions['shaft_1']["x_7_8"]=cal_base_d(data['gear_pair_1']['d1_small'])/2 - dimentions['shaft_1']['x_1_2'] - dimentions['shaft_1']['x_3_4'] - dimentions['shaft_1']['x_5_6']
dimentions['shaft_1']['y_8_9']=data['gear_pair_1']['b1_small']
dimentions['shaft_1']['x_9_10']= - (dimentions['shaft_1']["x_7_8"])
dimentions['shaft_1']['y_10_11']=data['box']['Delta_2'] - data['box']['to_oil_slinger']
dimentions['shaft_1']['x_11_12']= - (data['bear_1']['d'] * k_shoulder)
dimentions['shaft_1']['y_12_13']=data['box']['to_oil_slinger'] + data['box']['to_bear_in'] + data['bear_1']['B'] - data['box']['shaft_to_bear']
dimentions['shaft_1']['x_13_14']= - (dimentions['shaft_1']['x_1_2'] + dimentions['shaft_1']['x_3_4'])

lst = [(Parser(key),dimentions['shaft_1'][key]) for key in sorted(dimentions['shaft_1'])]

# 保证逐个计算
lst.sort(key=lambda x:x[0].ref)

dirName2dir = {'x':0,'y':1,'z':2}

for i in range(len(lst)):
    target_Name = lst[i][0].target
    ref_Name = lst[i][0].ref
    dirName = lst[i][0].dirName
    direction = dirName2dir[dirName]
    for dim in range(3):
        all_verts[PName_idx['shaft_1'][target_Name]].co[dim] = all_verts[PName_idx['shaft_1'][ref_Name]].co[dim]
    all_verts[PName_idx['shaft_1'][target_Name]].co[direction] += lst[i][1]

