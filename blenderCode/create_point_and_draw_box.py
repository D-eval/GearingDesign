import json
import os

design_json_path = "/Users/broyou/Desktop/ME/gear_design/design.json"

import bpy
import mathutils


def create_point_cloud_container(name="PointContainer", num=200):
    # 如果已存在同名对象，先删除
    obj = bpy.data.objects.get(name)
    if obj:
        bpy.data.objects.remove(obj, do_unlink=True)
    # 创建空网格和对象
    mesh = bpy.data.meshes.new(name + "_Mesh")
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    # 设置为活动对象并选中
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    # 生成 num 个顶点（平铺）
    verts = [(i % 10, i // 10, 0) for i in range(num)]
    mesh.from_pydata(verts, [], [])  # 无边无面，只含顶点
    mesh.update()
    print(f"已创建物体 {name}，包含 {len(mesh.vertices)} 个点。")

# 调用函数
create_point_cloud_container(num=200)



# 编辑好点名和索引名的对应
PName_idx = {
   1:0,
   2:1,
   3:2,
   4:3,
   5:4,
   6:5,
   7:6,
   8:7,
   9:8,
   10:9,
   11:10,
   12:11,
   13:12,
   14:13,
   15:14,
   16:15,
   17:16,
   18:17,
   19:18,
   20:19,
   21:20,
   22:21,
   23:22,
   24:23,
   25:24,
   26:25,
   27:26,
   28:27,
   29:28,
   30:29,
   31:30,
   32:31,
   33:32,
   34:33,
   35:34,
   36:35,
   37:36,
   38:37,
   39:38,
   40:39,
   41:40,
   42:41,
   43:42,
   44:43,
   45:44,
   46:45,
   47:46,
   48:47,
   49:48,
   50:49,
   51:50,
   52:51,
   53:52,
   54:53,
   55:54,
   56:55,
   57:56,
   58:57,
   59:58,
   60:59,
   61:60,
   62:61,
   63:62,
   64:63,
   65:64,
   66:65,
   67:66,
   68:67,
   69:68,
   70:69,
   71:70,
   72:71,
   73:72,
   74:73,
   75:74,
   76:75,
   77:76,
   78:77,
   79:78,
   80:79,
   81:80,
   82:81,
   83:82,
   84:83,
   85:84,
   86:85,
   87:86,
   88:87,
   89:88,
   90:89,
   91:90,
   92:91,
   93:92,
   94:93,
   95:94,
   96:95,
   97:96,
   98:97,
   99:98,
   100:99,
}

for i in range(101,111):
    PName_idx[i] = i-1

for i in range(111,115):
    PName_idx[i] = i-1

for i in range(115,123):
    PName_idx[i] = i-1

for i in range(123,131):
    PName_idx[i] = i-1

for i in range(131,131+16):
    PName_idx[i] = i-1

for i in range(147,149):
    PName_idx[i] = i-1
    
for i in range(149,161):
    PName_idx[i] = i-1
    
for i in range(161,173):
    PName_idx[i] = i-1

for i in range(173,175):
    PName_idx[i] = i-1

for i in range(175,179):
    PName_idx[i] = i-1

for i in range(179,183):
    PName_idx[i] = i-1
    
for i in range(183,187):
    PName_idx[i] = i-1
    
for i in range(187,191):
    PName_idx[i] = i-1
    
for i in range(191,195): # 
    PName_idx[i] = i-1


with open(design_json_path, "r") as f:
    data = json.load(f)

import bpy
import bmesh
import mathutils




obj = bpy.data.objects.get("PointContainer")
# bpy.context.collection.objects.link(obj)

# 设置为活动对象并选中
# bpy.context.view_layer.objects.active = obj
obj.select_set(True)

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


x_1_2 = data['bear_1']['D']



all_verts[PName_idx[2]].co = all_verts[PName_idx[1]].co.copy()
all_verts[PName_idx[2]].co[0] += x_1_2

x_2_5 =  data['gear_pair_1']['a12'] - data['bear_1']['D']/2 - data['bear_2']['D']/2

all_verts[PName_idx[5]].co = all_verts[PName_idx[2]].co.copy()
all_verts[PName_idx[5]].co[0] += x_2_5

all_verts[PName_idx[6]].co = all_verts[PName_idx[5]].co.copy()
all_verts[PName_idx[6]].co[0] += data['bear_2']['D']

x_6_9 = data['gear_pair_2']['a23'] - data['bear_2']['D']/2 - data['bear_3']['D']/2

all_verts[PName_idx[9]].co = all_verts[PName_idx[6]].co.copy()
all_verts[PName_idx[9]].co[0] += x_6_9

all_verts[PName_idx[10]].co = all_verts[PName_idx[9]].co.copy()
all_verts[PName_idx[10]].co[0] += data['bear_3']['D']

all_verts[PName_idx[3]].co = all_verts[PName_idx[1]].co.copy()
all_verts[PName_idx[3]].co[1] += box_width

all_verts[PName_idx[4]].co = all_verts[PName_idx[2]].co.copy()
all_verts[PName_idx[4]].co[1] += box_width

all_verts[PName_idx[7]].co = all_verts[PName_idx[5]].co.copy()
all_verts[PName_idx[7]].co[1] += box_width

all_verts[PName_idx[8]].co = all_verts[PName_idx[6]].co.copy()
all_verts[PName_idx[8]].co[1] += box_width

all_verts[PName_idx[11]].co = all_verts[PName_idx[9]].co.copy()
all_verts[PName_idx[11]].co[1] += box_width

all_verts[PName_idx[12]].co = all_verts[PName_idx[10]].co.copy()
all_verts[PName_idx[12]].co[1] += box_width

B = data['box']['B']

all_verts[PName_idx[17]].co = all_verts[PName_idx[1]].co.copy()
all_verts[PName_idx[17]].co[1] -= B

all_verts[PName_idx[18]].co = all_verts[PName_idx[2]].co.copy()
all_verts[PName_idx[18]].co[1] -= B

all_verts[PName_idx[19]].co = all_verts[PName_idx[5]].co.copy()
all_verts[PName_idx[19]].co[1] -= B

all_verts[PName_idx[20]].co = all_verts[PName_idx[6]].co.copy()
all_verts[PName_idx[20]].co[1] -= B

all_verts[PName_idx[21]].co = all_verts[PName_idx[9]].co.copy()
all_verts[PName_idx[21]].co[1] -= B

all_verts[PName_idx[22]].co = all_verts[PName_idx[10]].co.copy()
all_verts[PName_idx[22]].co[1] -= B

all_verts[PName_idx[30]].co = all_verts[PName_idx[3]].co.copy()
all_verts[PName_idx[30]].co[1] += B

all_verts[PName_idx[29]].co = all_verts[PName_idx[4]].co.copy()
all_verts[PName_idx[29]].co[1] += B

all_verts[PName_idx[28]].co = all_verts[PName_idx[7]].co.copy()
all_verts[PName_idx[28]].co[1] += B

all_verts[PName_idx[27]].co = all_verts[PName_idx[8]].co.copy()
all_verts[PName_idx[27]].co[1] += B

all_verts[PName_idx[26]].co = all_verts[PName_idx[11]].co.copy()
all_verts[PName_idx[26]].co[1] += B

all_verts[PName_idx[25]].co = all_verts[PName_idx[12]].co.copy()
all_verts[PName_idx[25]].co[1] += B

x_10_13 = data['box']['Delta_1'] + data['gear_pair_2']['d3_big']/2 - data['bear_3']['D']/2

all_verts[PName_idx[13]].co = all_verts[PName_idx[10]].co.copy()
all_verts[PName_idx[13]].co[0] += x_10_13

all_verts[PName_idx[14]].co = all_verts[PName_idx[13]].co.copy()
all_verts[PName_idx[14]].co[1] += box_width

all_verts[PName_idx[23]].co = all_verts[PName_idx[22]].co.copy()
all_verts[PName_idx[23]].co[0] += x_10_13 + data['box']['A']

all_verts[PName_idx[24]].co = all_verts[PName_idx[25]].co.copy()
all_verts[PName_idx[24]].co[0] += x_10_13 + data['box']['A']

all_verts[PName_idx[33]].co = all_verts[PName_idx[9]].co.copy()
all_verts[PName_idx[33]].co[0] = (all_verts[PName_idx[9]].co[0] + all_verts[PName_idx[10]].co[0]) / 2

all_verts[PName_idx[34]].co = all_verts[PName_idx[5]].co.copy()
all_verts[PName_idx[34]].co[0] = (all_verts[PName_idx[5]].co[0] + all_verts[PName_idx[6]].co[0]) / 2

all_verts[PName_idx[35]].co = all_verts[PName_idx[1]].co.copy()
all_verts[PName_idx[35]].co[0] = (all_verts[PName_idx[1]].co[0] + all_verts[PName_idx[2]].co[0]) / 2

r = data['end_cap_1']['D2']/2
c1 = data['box']['d_1']['c1']
c2 = data['box']['d_1']['c2']
h = np.sqrt(2*r*c1 - c1**2)

x_35_40 = data['end_cap_1']['D2']/2

all_verts[PName_idx[40]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[40]].co[2] += h
all_verts[PName_idx[40]].co[1] -= c1 + data['box']['delta']
all_verts[PName_idx[40]].co[0] -= x_35_40

all_verts[PName_idx[36]].co = all_verts[PName_idx[40]].co.copy()
all_verts[PName_idx[36]].co[0] += c1
all_verts[PName_idx[36]].co[1] += c1

all_verts[PName_idx[37]].co = all_verts[PName_idx[40]].co.copy()
all_verts[PName_idx[37]].co[0] += c1
all_verts[PName_idx[37]].co[1] -= c2

all_verts[PName_idx[39]].co = all_verts[PName_idx[40]].co.copy()
all_verts[PName_idx[39]].co[0] -= c2
all_verts[PName_idx[39]].co[1] += c1

all_verts[PName_idx[38]].co = all_verts[PName_idx[40]].co.copy()
all_verts[PName_idx[38]].co[0] -= c2
all_verts[PName_idx[38]].co[1] -= c2

x_35_38 = all_verts[PName_idx[35]].co[0] - all_verts[PName_idx[38]].co[0]
y_35_38 = all_verts[PName_idx[38]].co[1] - all_verts[PName_idx[35]].co[1]

_R = np.sqrt(x_35_38**2 + y_35_38**2)

x_35_16 = _R
all_verts[PName_idx[16]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[16]].co[0] -= x_35_16

all_verts[PName_idx[15]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[15]].co[1] += box_width

all_verts[PName_idx[32]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[32]].co[0] -= data['box']['A']
all_verts[PName_idx[32]].co[1] -= B

all_verts[PName_idx[31]].co = all_verts[PName_idx[15]].co.copy()
all_verts[PName_idx[31]].co[0] -= data['box']['A']
all_verts[PName_idx[31]].co[1] += B

x_35_36 = x_35_40 - c1

all_verts[PName_idx[41]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[41]].co[0] += x_35_36
all_verts[PName_idx[41]].co[1] -= data['box']['delta']
all_verts[PName_idx[41]].co[2] += h

all_verts[PName_idx[44]].co = all_verts[PName_idx[41]].co.copy()
all_verts[PName_idx[44]].co[1] -= c1 + c2

x_34_42 = np.sqrt((data['end_cap_2']['D2']/2)**2 - h**2)

all_verts[PName_idx[42]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[42]].co[0] -= x_34_42
all_verts[PName_idx[42]].co[1] -= data['box']['delta']
all_verts[PName_idx[42]].co[2] += h

all_verts[PName_idx[43]].co = all_verts[PName_idx[42]].co.copy()
all_verts[PName_idx[43]].co[1] -= c1 + c2

all_verts[PName_idx[45]].co = all_verts[PName_idx[42]].co.copy()
all_verts[PName_idx[45]].co[0] = (all_verts[PName_idx[41]].co[0] + all_verts[PName_idx[42]].co[0])/2
all_verts[PName_idx[45]].co[1] -= c1

all_verts[PName_idx[46]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[46]].co[0] += x_34_42
all_verts[PName_idx[46]].co[1] -= data['box']['delta']
all_verts[PName_idx[46]].co[2] += h

all_verts[PName_idx[49]].co = all_verts[PName_idx[46]].co.copy()
all_verts[PName_idx[49]].co[1] -= c1 + c2

x_33_47 = np.sqrt((data['end_cap_3']['D2']/2)**2 - h**2)

all_verts[PName_idx[47]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[47]].co[0] -= x_33_47
all_verts[PName_idx[47]].co[1] -= data['box']['delta']
all_verts[PName_idx[47]].co[2] += h

all_verts[PName_idx[48]].co = all_verts[PName_idx[47]].co.copy()
all_verts[PName_idx[48]].co[1] -= c1 + c2

all_verts[PName_idx[50]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[50]].co[0] += data['end_cap_2']['D2']/2 + c1
all_verts[PName_idx[50]].co[1] -= data['box']['delta'] + c1
all_verts[PName_idx[50]].co[2] += h

all_verts[PName_idx[51]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[51]].co[0] -= data['end_cap_3']['D2']/2 + c1
all_verts[PName_idx[51]].co[1] -= data['box']['delta'] + c1
all_verts[PName_idx[51]].co[2] += h

all_verts[PName_idx[52]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[52]].co[0] += x_33_47
all_verts[PName_idx[52]].co[1] -= data['box']['delta']
all_verts[PName_idx[52]].co[2] += h

all_verts[PName_idx[55]].co = all_verts[PName_idx[52]].co.copy()
all_verts[PName_idx[55]].co[1] -= c1 + c2

all_verts[PName_idx[53]].co = all_verts[PName_idx[52]].co.copy()
all_verts[PName_idx[53]].co[0] += c1 + c2

all_verts[PName_idx[54]].co = all_verts[PName_idx[55]].co.copy()
all_verts[PName_idx[54]].co[0] += c1 + c2

all_verts[PName_idx[56]].co = all_verts[PName_idx[52]].co.copy()
all_verts[PName_idx[56]].co[0] += c1
all_verts[PName_idx[56]].co[1] -= c1

all_verts[PName_idx[57]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[57]].co[0] -= data['end_cap_1']['D2']/2
all_verts[PName_idx[57]].co[1] -= data['box']['B']

all_verts[PName_idx[58]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[58]].co[0] += data['end_cap_1']['D2']/2
all_verts[PName_idx[58]].co[1] -= data['box']['B']

all_verts[PName_idx[59]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[59]].co[0] -= data['end_cap_2']['D2']/2
all_verts[PName_idx[59]].co[1] -= data['box']['B']

all_verts[PName_idx[60]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[60]].co[0] += data['end_cap_2']['D2']/2
all_verts[PName_idx[60]].co[1] -= data['box']['B']

all_verts[PName_idx[61]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[61]].co[0] -= data['end_cap_3']['D2']/2
all_verts[PName_idx[61]].co[1] -= data['box']['B']

all_verts[PName_idx[62]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[62]].co[0] += data['end_cap_3']['D2']/2
all_verts[PName_idx[62]].co[1] -= data['box']['B']

all_verts[PName_idx[63]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[63]].co[0] -= data['box']['delta']
all_verts[PName_idx[63]].co[1] -= data['box']['delta']

all_verts[PName_idx[64]].co = all_verts[PName_idx[13]].co.copy()
all_verts[PName_idx[64]].co[0] += data['box']['delta']
all_verts[PName_idx[64]].co[1] -= data['box']['delta']

all_verts[PName_idx[65]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[65]].co[1] += box_width / 2
all_verts[PName_idx[65]].co[0] -= data['box']['A']

all_verts[PName_idx[66]].co = all_verts[PName_idx[13]].co.copy()
all_verts[PName_idx[66]].co[1] += box_width / 2
all_verts[PName_idx[66]].co[0] += data['box']['A']

all_verts[PName_idx[67]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[67]].co[0] -= data['box']['delta'] + data['box']['d_2']['c1']
all_verts[PName_idx[67]].co[1] += data['box']['d_2']['c1']

all_verts[PName_idx[68]].co = all_verts[PName_idx[23]].co.copy()
all_verts[PName_idx[68]].co[0] -= data['box']['d_2']['c2']
all_verts[PName_idx[68]].co[1] += data['box']['d_2']['c2']

all_verts[PName_idx[69]].co = all_verts[PName_idx[57]].co.copy()
all_verts[PName_idx[69]].co[1] += data['box']['B'] - data['box']['delta']

all_verts[PName_idx[70]].co = all_verts[PName_idx[58]].co.copy()
all_verts[PName_idx[70]].co[1] += data['box']['B'] - data['box']['delta']

all_verts[PName_idx[71]].co = all_verts[PName_idx[59]].co.copy()
all_verts[PName_idx[71]].co[1] += data['box']['B'] - data['box']['delta']

all_verts[PName_idx[72]].co = all_verts[PName_idx[60]].co.copy()
all_verts[PName_idx[72]].co[1] += data['box']['B'] - data['box']['delta']

all_verts[PName_idx[73]].co = all_verts[PName_idx[61]].co.copy()
all_verts[PName_idx[73]].co[1] += data['box']['B'] - data['box']['delta']

all_verts[PName_idx[74]].co = all_verts[PName_idx[62]].co.copy()
all_verts[PName_idx[74]].co[1] += data['box']['B'] - data['box']['delta']

R_3 = data['gear_pair_2']['d3_big']/2 + data['box']['Delta_1']
R_2 = data['gear_pair_1']['d2_big']/2 + data['box']['Delta_1']
a_23 = data['gear_pair_2']['a23']

cos_theta = - (R_3 - R_2) / a_23
sin_theta = np.sqrt(1 - cos_theta**2)
x_33_75 = R_3 * cos_theta
z_33_75 = R_3 * sin_theta
x_33_80 = (R_3 + data['box']['delta_1']) * cos_theta
z_33_80 = (R_3 + data['box']['delta_1']) * sin_theta

all_verts[PName_idx[75]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[75]].co[0] += x_33_75
all_verts[PName_idx[75]].co[2] += z_33_75
all_verts[PName_idx[80]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[80]].co[0] += x_33_80
all_verts[PName_idx[80]].co[1] -= data['box']['delta']
all_verts[PName_idx[80]].co[2] += z_33_80

sin_alpha = - cos_theta
x_16_33 = all_verts[PName_idx[33]].co[0] - all_verts[PName_idx[16]].co[0]
b = - R_3 / cos_theta - x_16_33
x_16_77 = b * sin_alpha / (1 - sin_alpha)

all_verts[PName_idx[77]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[77]].co[0] += x_16_77

x_76_77 = x_16_77 * cos_theta
z_76_77 = x_16_77 * sin_theta
x_76_81 = (x_16_77 + data['box']['delta_1']) * cos_theta
z_76_81 = (x_16_77 + data['box']['delta_1']) * sin_theta

all_verts[PName_idx[76]].co = all_verts[PName_idx[77]].co.copy()
all_verts[PName_idx[76]].co[0] += x_76_77
all_verts[PName_idx[76]].co[2] += z_76_77

all_verts[PName_idx[81]].co = all_verts[PName_idx[77]].co.copy()
all_verts[PName_idx[81]].co[0] += x_76_81
all_verts[PName_idx[81]].co[1] -= data['box']['delta']
all_verts[PName_idx[81]].co[2] += z_76_81

all_verts[PName_idx[78]].co = all_verts[PName_idx[13]].co.copy()
all_verts[PName_idx[78]].co[2] -= data['box']['H_center_to_bottom']

all_verts[PName_idx[79]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[79]].co[2] -= data['box']['H_center_to_bottom']

all_verts[PName_idx[82]].co = all_verts[PName_idx[16]].co.copy()
all_verts[PName_idx[82]].co[0] -= data['box']['delta']

all_verts[PName_idx[83]].co = all_verts[PName_idx[82]].co.copy()
all_verts[PName_idx[83]].co[2] -= data['box']['H_center_to_bottom'] + data['box']['delta_bottom']

all_verts[PName_idx[85]].co = all_verts[PName_idx[13]].co.copy()
all_verts[PName_idx[85]].co[0] += data['box']['delta']

all_verts[PName_idx[84]].co = all_verts[PName_idx[85]].co.copy()
all_verts[PName_idx[84]].co[2] -= data['box']['H_center_to_bottom'] + data['box']['delta_bottom']

b2 = data['box']['b_2']
c1 = data['box']['d_f']['c1']
c2 = data['box']['d_f']['c2']

all_verts[PName_idx[86]].co = all_verts[PName_idx[83]].co.copy()
all_verts[PName_idx[86]].co[1] -= data['box']['delta']
all_verts[PName_idx[86]].co[2] += b2 - data['box']['under_to_ground']

all_verts[PName_idx[87]].co = all_verts[PName_idx[86]].co.copy()
all_verts[PName_idx[87]].co[1] -= c1 + c2

all_verts[PName_idx[88]].co = all_verts[PName_idx[87]].co.copy()
all_verts[PName_idx[88]].co[2] -= b2

all_verts[PName_idx[89]].co = all_verts[PName_idx[88]].co.copy()
all_verts[PName_idx[89]].co[1] += c1 + c2 - 3

all_verts[PName_idx[90]].co = all_verts[PName_idx[89]].co.copy()
all_verts[PName_idx[90]].co[2] += data['box']['under_to_ground']

all_verts[PName_idx[96]].co = all_verts[PName_idx[86]].co.copy()
all_verts[PName_idx[96]].co[2] = all_verts[PName_idx[16]].co[2] - data['box']['b']

all_verts[PName_idx[97]].co = all_verts[PName_idx[96]].co.copy()
all_verts[PName_idx[97]].co[1] = all_verts[PName_idx[32]].co[1]

all_verts[PName_idx[98]].co = all_verts[PName_idx[97]].co.copy()
all_verts[PName_idx[98]].co[2] += data['box']['b']

all_verts[PName_idx[99]].co = all_verts[PName_idx[98]].co.copy()
all_verts[PName_idx[99]].co[2] += data['box']['b_1']

all_verts[PName_idx[100]].co = all_verts[PName_idx[96]].co.copy()
all_verts[PName_idx[100]].co[2] += data['box']['b'] + data['box']['b_1']

def mirror(idx_dict, dim, x):
    for k,v in idx_dict.items():
        all_verts[PName_idx[k]].co = all_verts[PName_idx[v]].co.copy()
        all_verts[PName_idx[k]].co[dim] = 2*x - all_verts[PName_idx[k]].co[dim]

mirror({91:86, 92:87, 93:88, 94:89, 95:90}, 1, all_verts[PName_idx[79]].co[1] + box_width/2)

mirror({101:86,102:87,103:88,104:89,105:90,106:91,107:92,108:93,109:94,110:95}, 0, (all_verts[PName_idx[79]].co[0] + all_verts[PName_idx[78]].co[0])/2)

mirror({111:80,112:81,113:75,114:76},1,all_verts[PName_idx[66]].co[1])

def stretch(idx_dict, dim, x):
    for k,v in idx_dict.items():
        all_verts[PName_idx[k]].co = all_verts[PName_idx[v]].co.copy()
        all_verts[PName_idx[k]].co[dim] += x

z_main = [13,14,15,16,23,24,31,32]
stretch({k:v for k,v in zip(list(range(115,123)),z_main)},2,data['box']['b_1'])
stretch({k:v for k,v in zip(list(range(123,131)),z_main)},2,-data['box']['b'])

convex_main = [36,37,38,39,41,42,43,44,46,47,48,49,52,53,54,55]
mirror({k:v for k,v in zip(list(range(131,131+16)),convex_main)},2,all_verts[PName_idx[85]].co[2])

mirror({147:78,148:79},1,all_verts[PName_idx[66]].co[1])

dx = data['box']['m']/2
dz_1 = np.sqrt((data['end_cap_1']['D2']/2)**2 - dx**2)
dy = data['box']['delta']

all_verts[PName_idx[149]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[149]].co[0] -= dx
all_verts[PName_idx[149]].co[1] -= dy
all_verts[PName_idx[149]].co[2] -= dz_1

all_verts[PName_idx[150]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[150]].co[0] -= dx
all_verts[PName_idx[150]].co[1] -= dy
all_verts[PName_idx[150]].co[2] = all_verts[PName_idx[86]].co[2]

all_verts[PName_idx[151]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[151]].co[0] += dx
all_verts[PName_idx[151]].co[1] -= dy
all_verts[PName_idx[151]].co[2] -= dz_1

all_verts[PName_idx[152]].co = all_verts[PName_idx[35]].co.copy()
all_verts[PName_idx[152]].co[0] += dx
all_verts[PName_idx[152]].co[1] -= dy
all_verts[PName_idx[152]].co[2] = all_verts[PName_idx[86]].co[2]

dz_2 = np.sqrt((data['end_cap_2']['D2']/2)**2 - dx**2)
dz_3 = np.sqrt((data['end_cap_3']['D2']/2)**2 - dx**2)

all_verts[PName_idx[153]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[153]].co[0] -= dx
all_verts[PName_idx[153]].co[1] -= dy
all_verts[PName_idx[153]].co[2] -= dz_2

all_verts[PName_idx[154]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[154]].co[0] -= dx
all_verts[PName_idx[154]].co[1] -= dy
all_verts[PName_idx[154]].co[2] = all_verts[PName_idx[86]].co[2]

all_verts[PName_idx[155]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[155]].co[0] += dx
all_verts[PName_idx[155]].co[1] -= dy
all_verts[PName_idx[155]].co[2] -= dz_2

all_verts[PName_idx[156]].co = all_verts[PName_idx[34]].co.copy()
all_verts[PName_idx[156]].co[0] += dx
all_verts[PName_idx[156]].co[1] -= dy
all_verts[PName_idx[156]].co[2] = all_verts[PName_idx[86]].co[2]

all_verts[PName_idx[157]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[157]].co[0] -= dx
all_verts[PName_idx[157]].co[1] -= dy
all_verts[PName_idx[157]].co[2] -= dz_3

all_verts[PName_idx[158]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[158]].co[0] -= dx
all_verts[PName_idx[158]].co[1] -= dy
all_verts[PName_idx[158]].co[2] = all_verts[PName_idx[86]].co[2]

all_verts[PName_idx[159]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[159]].co[0] += dx
all_verts[PName_idx[159]].co[1] -= dy
all_verts[PName_idx[159]].co[2] -= dz_3

all_verts[PName_idx[160]].co = all_verts[PName_idx[33]].co.copy()
all_verts[PName_idx[160]].co[0] += dx
all_verts[PName_idx[160]].co[1] -= dy
all_verts[PName_idx[160]].co[2] = all_verts[PName_idx[86]].co[2]

stretch({k:v for k,v in zip(list(range(161,173)),list(range(149,161)))},1,-(all_verts[95].co[1]-all_verts[96].co[1]))

all_verts[PName_idx[173]].co = all_verts[86].co.copy()
all_verts[PName_idx[173]].co[0] += data['box']['d_f']['c2']
all_verts[PName_idx[173]].co[1] += data['box']['d_f']['c2']

all_verts[PName_idx[174]].co = all_verts[101].co.copy()
all_verts[PName_idx[174]].co[0] -= data['box']['d_f']['c2']
all_verts[PName_idx[174]].co[1] += data['box']['d_f']['c2']

e1 = all_verts[80].co - all_verts[111].co
e1 = e1/np.linalg.norm(e1)
e2 = all_verts[110].co - all_verts[111].co
e2 = e2/np.linalg.norm(e2)
e3 = np.cross(e1,e2)

a_110_80 = all_verts[80].co - all_verts[111].co
a_110_80 = np.dot(a_110_80,e1)
b_111_110 = all_verts[110].co - all_verts[111].co
b_111_110 = np.dot(b_111_110,e2)

a_111_175 = (a_110_80 - data['sight_hole_cover']['B1']) / 2
b_111_175 = (b_111_110 - data['sight_hole_cover']['A1']) / 2

r_111_175 = a_111_175*e1 + b_111_175*e2
all_verts[PName_idx[175]].co = all_verts[111].co.copy()
all_verts[PName_idx[175]].co[0] += r_111_175[0]
all_verts[PName_idx[175]].co[1] += r_111_175[1]
all_verts[PName_idx[175]].co[2] += r_111_175[2]

r_80_176 = (-a_111_175)*e1 + b_111_175*e2
all_verts[PName_idx[176]].co = all_verts[80].co.copy()
all_verts[PName_idx[176]].co[0] += r_80_176[0]
all_verts[PName_idx[176]].co[1] += r_80_176[1]
all_verts[PName_idx[176]].co[2] += r_80_176[2]

r_110_178 = a_111_175*e1 + (-b_111_175)*e2
all_verts[PName_idx[178]].co = all_verts[110].co.copy()
all_verts[PName_idx[178]].co[0] += r_110_178[0]
all_verts[PName_idx[178]].co[1] += r_110_178[1]
all_verts[PName_idx[178]].co[2] += r_110_178[2]

r_79_177 = (-a_111_175)*e1 + (-b_111_175)*e2
all_verts[PName_idx[177]].co = all_verts[79].co.copy()
all_verts[PName_idx[177]].co[0] += r_79_177[0]
all_verts[PName_idx[177]].co[1] += r_79_177[1]
all_verts[PName_idx[177]].co[2] += r_79_177[2]

def stretch_n(idx_target,idx_refer,n,x):
    all_verts[idx_target].co = all_verts[idx_refer].co.copy()
    v = n * x
    for i in range(3):
        all_verts[idx_target].co[i] += v[i]

for k,v in zip(list(range(178,182)),list(range(174,178))):
    stretch_n(k,v,e3,data['sight_hole_cover']['h'])
    
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


all_verts[182].co = all_verts[178].co.copy()
a = (data['sight_hole_cover']['B1'] - data['sight_hole_cover']['B'])/2
b = (data['sight_hole_cover']['A1'] - data['sight_hole_cover']['A'])/2
r = a * e1 + b * e2
for i in range(3):
    all_verts[182].co[i] += r[i]

rectangle_n([182,183,184,185],e1,e2,data['sight_hole_cover']['B'],data['sight_hole_cover']['A'])


for k,v in zip(list(range(186,190)),list(range(182,196))):
    stretch_n(k,v,-e3,data['sight_hole_cover']['h']+data['box']['delta_1'])

def offset_n(idx,e,x):
    r = e * x
    for i in range(3):
        all_verts[idx].co[i] += r[i]

all_verts[190].co = all_verts[178].co.copy()
offset_n(190,e1,(data['sight_hole_cover']['B1'] - data['sight_hole_cover']['B2'])/2)
offset_n(190,e2,(data['sight_hole_cover']['A1'] - data['sight_hole_cover']['A2'])/2)

rectangle_n(list(range(190,194)),e1,e2,data['sight_hole_cover']['B2'],data['sight_hole_cover']['A2'])



# 在编辑模式中,记录圆心center,法向量n,角度theta,半径r
# 然后创建一个新物体Arc作为原来物体的子集, 设置采样点num
# 将圆心设置为center

def create_arc(id_center,id_1,id_2,num=16,name='Arc'):
    arc_obj = bpy.data.objects.get(name)
    if arc_obj:
        return
    center = all_verts[id_center].co.copy()
    p1 = all_verts[id_1].co.copy()
    p2 = all_verts[id_2].co.copy()
    e1 = p1 - center
    e2 = p2 - center
    e1 = e1.normalized()
    e2 = e2.normalized()
    n = e1.cross(e2).normalized()

    # 弧角
    theta = e1.angle(e2)
    r = (p1 - center).length

    e2 = n.cross(e1).normalized() # 保证垂直

    # 采样点数
    num = 16

    mesh_data = bpy.data.meshes.new("ArcMesh")
    arc_obj = bpy.data.objects.new(name, mesh_data)
    bpy.context.collection.objects.link(arc_obj)

    bpy.context.view_layer.objects.active = arc_obj
    arc_obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')

    # 创建 bmesh
    bm = bmesh.new()
    bm.from_mesh(mesh_data)

    verts = []  # 用来保存点

    ts = np.linspace(0, theta, num)

    for i in range(num):
        t = ts[i]
        x = r * np.cos(t)
        y = r * np.sin(t)
        vec = x * e1 + y * e2
        pos = center.copy()
        for i in range(3):
            pos[i] = vec[i]
        v_temp = bm.verts.new(pos)
        verts.append(v_temp)
        
    # 更新内部索引表（建议加上）
    bm.verts.ensure_lookup_table()
    for i in range(len(verts) - 1):
        bm.edges.new((verts[i], verts[i + 1]))
    # 切回对象模式（这是必须的，否则 to_mesh 会报错）
    bpy.ops.object.mode_set(mode='OBJECT')
    # 将修改写入 mesh
    bm.to_mesh(mesh_data)
    mesh_data.update()
    # 清理 bmesh（释放内存）
    bm.free()
    arc_obj.parent = obj
    arc_obj.location = center
    
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    return arc_obj




def create_circle(id_center,id_1,id_2,num=64,name='Arc'):
    arc_obj = bpy.data.objects.get(name)
    if arc_obj:
        return
    center = all_verts[id_center].co.copy()
    p1 = all_verts[id_1].co.copy()
    p2 = all_verts[id_2].co.copy()
    e1 = p1 - center
    e2 = p2 - center
    e1 = e1.normalized()
    e2 = e2.normalized()
    n = e1.cross(e2).normalized()

    # 弧角
    theta = 2 * np.pi
    r = (p1 - center).length # 第一个点确定半径,第二个确定平面

    e2 = n.cross(e1).normalized() # 保证垂直
    mesh_data = bpy.data.meshes.new("ArcMesh")
    arc_obj = bpy.data.objects.new(name, mesh_data)
    bpy.context.collection.objects.link(arc_obj)

    bpy.context.view_layer.objects.active = arc_obj
    arc_obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')

    # 创建 bmesh
    bm = bmesh.new()
    bm.from_mesh(mesh_data)

    verts = []  # 用来保存点

    ts = np.linspace(0, theta, num)

    for i in range(num):
        t = ts[i]
        x = r * np.cos(t)
        y = r * np.sin(t)
        vec = x * e1 + y * e2
        pos = center.copy()
        for i in range(3):
            pos[i] = vec[i]
        v_temp = bm.verts.new(pos)
        verts.append(v_temp)
        
    # 更新内部索引表（建议加上）
    bm.verts.ensure_lookup_table()
    for i in range(len(verts) - 1):
        bm.edges.new((verts[i], verts[i + 1]))
    bm.edges.new((verts[-1], verts[0]))
    # 切回对象模式（这是必须的，否则 to_mesh 会报错）
    bpy.ops.object.mode_set(mode='OBJECT')
    # 将修改写入 mesh
    bm.to_mesh(mesh_data)
    mesh_data.update()
    # 清理 bmesh（释放内存）
    bm.free()
    arc_obj.parent = obj
    arc_obj.location = center
    
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    return arc_obj


arc1_obj = create_arc(32,74,12,name='Arc1')
arc2_obj = create_arc(76,15,75,name='Arc2')

all_verts[195].co = all_verts[76].co.copy()
all_verts[195].co[1] = all_verts[99].co[1]

arc3_obj = create_arc(195,99,80,name='Arc3')

all_verts[196].co = all_verts[32].co.copy()
all_verts[196].co[1] = all_verts[99].co[1]

arc4_obj = create_arc(196,79,63,name='Arc4')

circle1 = create_circle(34,1,117,name='Cir1')

all_verts[197].co = all_verts[34].co.copy()
all_verts[197].co[1] = all_verts[16].co[1]

all_verts[197].co = all_verts[34].co.copy()
all_verts[197].co[1] = all_verts[16].co[1]

all_verts[198].co = all_verts[36].co.copy()
all_verts[198].co[1] = all_verts[16].co[1]

circle2 = create_circle(197,198,56,name='Cir2')
