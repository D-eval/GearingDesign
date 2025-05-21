from design import design_all
import numpy as np
import matplotlib.pyplot as plt
import json
import argparse


parser = argparse.ArgumentParser(description="计算输送带相关参数")
parser.add_argument('--F_w', type=float, default=3.2, help='输出牵引力 (kN)')
parser.add_argument('--v_w', type=float, default=0.95, help='输送带速度 (m/s)')
parser.add_argument('--D', type=float, default=440, help='滚筒直径 (mm)')

args = parser.parse_args()

ALL_BOLT = [8,10,12,16,20,24,30]
def select_bolt(d):
    k = ALL_BOLT
    k = np.array(k)
    d = np.abs(k - d)
    idx = np.argmin(d)
    return ALL_BOLT[idx]

Bolt_to_c1c2D0 = {
    8: (13,11,18),
    10: (16,14,22),
    12: (18,16,26),
    16: (22,20,33),
    20: (26,24,20),
    24: (34,28,48),
    30: (40,34,61)
}


class Bolt:
    def __init__(self, d):
        self.d = d
        self.d = select_bolt(self.d)
        self.c1, self.c2, self.D0 = Bolt_to_c1c2D0[self.d]
    def __dict__(self):
        return {'d':self.d, 'c1':self.c1, 'c2':self.c2, 'D0':self.D0}

# 输入
F_w = args.F_w       # kN
v_w = args.v_w       # m/s
D = args.D    # 转换成米
out1, out2, out_shaft = design_all(F_w, v_w, D)
z1_small,z2_big,m12,b1_small,b2_big,a12 = out1
z2_small,z3_big,m23,b2_small,b3_big,a23 = out2
d1,d2,d3 = out_shaft[0]

d1_small = z1_small * m12
d2_big = z2_big * m12
d2_small = z2_small * m23
d3_big = z3_big * m23

box = {}
# 箱座壁厚
box['delta'] = max(8, 0.025*a23+3)
# 箱盖壁厚
box['delta_1'] = max(0.85*box['delta'], 8)
# 地脚螺栓直径
box['d_f'] = Bolt(0.036 * a23 + 12)
# 地脚螺栓数目
box['n'] = 4 if a23<=250 else 6

# 铸铁减速箱体结构之二
box['b'] = 1.5 * box['delta']
box['b_1'] = 1.5 * box['delta_1']
box['b_2'] = 2.5 * box['delta']
box['d_1'] = Bolt(0.75 * box['d_f'].d)
box['d_2'] = Bolt(0.6 * box['d_f'].d)
box['l'] = 200
box['d_3'] = Bolt(0.5 * box['d_f'].d)
box['d_4'] = Bolt(0.4 * box['d_f'].d)
box['d'] = 0.8 * box['d_2'].d
box['R_1'] = box['d_2'].c2
box['l_1'] = box['d_2'].c1 + box['d_2'].c2 + 8
box['m_1'] = 0.85 * box['delta_1']
box['m'] = 0.85 * box['delta']

box['Delta_1'] = box['delta']
box['Delta_2'] = box['delta']

# 分箱面凸缘尺寸A
box['A'] = box['delta']+box['d_1'].c1+box['d_1'].c2+5
box['B'] = box['A'] + 5

box['h'] = None
box['D_2'] = None
box['S'] = None

# all_data['box']['B'] = all_data['box']['A'] + 5
# 箱体内壁到甩油环
box['to_oil_slinger'] = 3
# 箱体内壁到轴承内侧
box['to_bear_in'] = 12
# 大齿轮距离
box['Delta_3'] = 10
# 闭轴承盖端, 轴面到轴承外面的距离
box['shaft_to_bear'] = 3

# 浸油深度
h_f = max(10, 0.7*m12*2.25)
h_s = [m23*2.25, 1/3*m23*z3_big/2]
h_expect = max(h_s)
box['h_s'] = h_expect
box['H_center_to_bottom'] = d3_big/2 + 30
box['delta_bottom'] = box['delta']
box['under_to_ground'] = 5



ALL_PART = {}
class Part:
    def __init__(self,key_name):
        ALL_PART[key_name] = self

# 轴承1 P161
class Bear(Part):
    def __init__(self, key_name, name, d, D, B, r, d_a, D_a, r_a):
        super().__init__(key_name)
        self.dict = {
            "name": name,
            "d": d,
            "D": D,
            "B": B,
            "r": r,
            "d_a": d_a,
            "D_a": D_a,
            "r_a": r_a
        }
    def __getitem__(self, key):
        return self.dict[key]
    def __dict__(self):
        return self.dict



T1,T2,T3 = out_shaft[3]
# 切向力
F1_small = T1 / d1_small * 2
F2_big = T2 / d2_big * 2
F2_small = T2 / d2_small * 2
F3_big = T3 / d3_big * 2
# 计算轴向力
F1_small_shaft = F1_small * np.tan(np.deg2rad(20))
F2_big_shaft = F2_big * np.tan(np.deg2rad(20))
F2_small_shaft = F2_small * np.tan(np.deg2rad(20))
F3_big_shaft = F3_big * np.tan(np.deg2rad(20))


bear_1 = Bear('bear_1',"6005", 25, 47, 12, 0.6, 30, 42, 0.6)
bear_2 = Bear('bear_2',"6008", 40, 68, 15, 1, 46, 62, 1)
bear_3 = Bear('bear_3',"6010", 50, 80, 16, 1, 56, 74, 1)

# 毡圈 课程设计P180
felt_d0_to_params = {
    15:(14,23,2.5,24,16,2,3),
    16:(15,26,3.5,27,17,3,4,3),
    18:(17,28,3.5,29,19,3,4.3),
    20:(19,30,3.5,31,21,3,4.3),
    22:(21,23,3.5,33,23,3,4.3),
    25:(24,37,5,38,26,4,5.5),
    28:(27,40,5,38,26,4,5.5),
    30:(29,42,5,43,31,4,5.5),
    32:(31,44,5,45,33,4,5.5),
    35:(34,47,5,48,36,4,5.5),
    38:(37,50,5,51,39,4,5.5),
    40:(39,52,5,53,41,4,5.5),
    42:(41,54,5,53,41,4,5.5),
    45:(44,57,5,58,46,4,5.5),
    48:(47,60,5,61,49,4,5.5),
    50:(49,66,7,67,51,5,7.1),
}

class FeltRing(Part):
    def __init__(self,key_name,d0):
        super().__init__(key_name)
        params = felt_d0_to_params[d0]
        self.dict = {
            "d": params[0],
            "D": params[1],
            "b": params[2],
            "D1": params[3],
            "d1": params[4],
            "b1": params[5],
            "b2": params[6],
            "d0": d0,
        }
    def __getitem__(self, key):
        return self.dict[key]
    def __dict__(self):
        return self.dict

felt_1 = FeltRing('felt_1',bear_1['d'])
felt_2 = FeltRing('felt_2',bear_2['d'])
felt_3 = FeltRing('felt_3',bear_3['d'])

Dd3n = {
    (45,70): (6,4),
    (70,100): (8,4),
    (110,140): (10,6),
    (150,230): (12,6)
}

def D_to_d3_num_screw(D):
    for key, value in Dd3n.items():
        if D >= key[0] and D <= key[1]:
            return value
    raise ValueError("D is out of range")

# 轴承端盖
class EndCapOpen(Part):
    def __init__(self,key_name, bear:Bear, felt_ring:FeltRing):
        super().__init__(key_name)
        D = bear['D']
        d3, num_screw = D_to_d3_num_screw(D)
        m = box['B'] - bear['B'] - box['to_bear_in']
        # m = box['l_1'] + box['delta'] - 8 - bear['B']
        d0 = d3 + 1
        D0 = D + 2.5*d3
        D2 = D0 + 2.5*d3
        e = 1.3*d3
        e1 = e
        D4 = D - 10
        D5 = D0 - 3 * d3
        D6 = D - 4
        d1 = felt_ring['d1']
        b1 = felt_ring['b1']
        b2 = felt_ring['b2']
        self.dict = {
            "d3":d3,
            "D": D,
            "d0": d0,
            "D0": D0,
            "D2": D2,
            "e": e,
            "e1": e1,
            "D4": D4,
            "D5": D5,
            "D6": D6,
            "d1": d1,
            "b1": b1,
            "b2": b2,
            "num_screw": num_screw,
            "m": m
        }
    def __getitem__(self, key):
        return self.dict[key]
    def __dict__(self):
        return self.dict


end_cap_1 = EndCapOpen('end_cap_1',bear_1, felt_1)
end_cap_2 = EndCapOpen('end_cap_2',bear_2, felt_2)
end_cap_3 = EndCapOpen('end_cap_3',bear_3, felt_3)
# 阶梯轴


all_data = {
    "gear_pair_1": {
        "z1_small": z1_small,
        "d1_small": round(d1_small, 3),
        "z2_big": z2_big,
        "d2_big": round(d2_big, 3),
        "m12": m12,
        "b1_small": b1_small,
        "b2_big": b2_big,
        "a12": a12
    },
    "gear_pair_2": {
        "z2_small": z2_small,
        "d2_small": round(d2_small, 3),
        "z3_big": z3_big,
        "d3_big": round(d3_big, 3),
        "m23": m23,
        "b2_small": b2_small,
        "b3_big": b3_big,
        "a23": a23
    },
    "shaft": {
        "d1": round(d1, 3),
        "d2": round(d2, 3),
        "d3": round(d3, 3),
        "l_interval": 3,
    },
    "coupling": { # 联轴器
        "name": "LT4",
        "d1": 20,
    },
    "coupling_2": {
        "name": "LT7",
        "d1": 45,
    }
}


all_data['box'] = {}
for key, value in box.items():
    if isinstance(value, Bolt):
        all_data['box'][key] = value.__dict__()
    else:
        all_data['box'][key] = value

for key, value in ALL_PART.items():
    all_data[key] = value.__dict__()

data = all_data
box_width = 2*data['box']['Delta_2'] + data['box']['Delta_3'] + data['gear_pair_1']['b2_big'] + data['gear_pair_2']['b3_big'] + (data['gear_pair_1']['b1_small']-data['gear_pair_1']['b2_big'])/2 + (data['gear_pair_2']['b2_small']-data['gear_pair_2']['b3_big'])/2
A = 100
d4 = 14.38 # M8, P145
A1 = A + 5 * d4
A2 = (A1 + A)/2
B1 = box_width - 20
B = B1 - 5 * d4
B2 = (B1 + B)/2
h = 3

all_data['sight_hole_cover'] = {
    'A':A,
    'd4':d4,
    'A1':A1,
    'A2':A2,
    'B1':B1,
    'B':B,
    'B2':B2,
    'h':h
}

# 保存数据到 JSON 文件
with open("./design.json", "w") as file:
    json.dump(all_data, file, indent=4)

print("数据已保存到 design.json")

