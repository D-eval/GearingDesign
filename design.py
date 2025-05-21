
'''
齿轮参数自动设计
给定:
输入功率 P
小齿轮转速 n
传动比 i
循环次数 N
小齿轮齿数 z

输出:
调整后的齿数z1,z2
模数m
压力角alpha
中心距a
齿宽b1,b2

还有一些不能更改的条件, 如果想改可以去AllCharts.py里按照机械设计书上的图表录入插值的数据
7级精度
小齿轮40Cr(调质),齿面硬度280
大齿轮45钢(调质),齿面硬度240
phi_d = 0.8
'''

import numpy as np
import matplotlib.pyplot as plt
from AllCharts import *


def cal_N(n):
    return 60 * n * 1 * (2*8*250*15)

def design_gear(P, n, i, N, z):
    # 常数
    phi_d = 0.8
    alpha = np.deg2rad(20)
    Z_E = 189.8
    h_a_star = 1
    sigma_Hlim1 = 600
    sigma_Hlim2 = 550
    sigma_Flim1 = 500
    sigma_Flim2 = 320
    S = 1
    S_ = 1.4
    K_A = 1
    c_star = 0.25
    # 开始设计
    z1 = z
    z2 = int(z * i)
    K_Ht = 1.3
    T_1 = 9.55e6 * P / n
    Z_H = (2 / (np.cos(alpha)*np.sin(alpha)))**(1/2)

    alpha_a1 = np.arccos(z1*np.cos(alpha)/(z1+2*h_a_star))
    alpha_a2 = np.arccos(z2*np.cos(alpha)/(z2+2*h_a_star))

    epsilon_a = (z1*(np.tan(alpha_a1)-np.tan(alpha))+z2*(np.tan(alpha_a2)-np.tan(alpha)))/(2*np.pi)
    print('epsilon_a = {:.3f}'.format(epsilon_a))
    Z_epsilon = ((4-epsilon_a)/3) ** (1/2)

    N1 = N
    N2 = N/i

    K_HN1 = f_fig_10_19.x2y(np.log10(N1))
    K_HN2 = f_fig_10_19.x2y(np.log10(N2))

    sigma_H_1 = K_HN1 * sigma_Hlim1 / S
    sigma_H_2 = K_HN2 * sigma_Hlim2 / S

    sigma_H = min(sigma_H_1, sigma_H_2)

    d_1t = (2*K_Ht*T_1/phi_d * (i+1)/(i) * (Z_H*Z_E*Z_epsilon/sigma_H)**2)**(1/3)
    print('试算 d_1t = {:.2f} mm'.format(d_1t))

    # 调整小齿轮分度圆直径
    v = np.pi * d_1t * n / (60 * 1000)
    b = phi_d * d_1t

    K_v = f_fig_10_8.x2y(v)

    F_t1 = 2*T_1/d_1t
    K_Ha = 1.2 if K_A*F_t1/b < 100 else 1

    K_Hb = f_cha_10_4.x2y(b)

    K_H = K_A * K_v * K_Ha * K_Hb

    d_1H = d_1t * (K_H/K_Ht)**(1/3)
    print('实际 d_1H = {:.2f} mm'.format(d_1H))
    m_H = d_1H / z1

    # 按齿根弯曲疲劳强度设计

    K_Ft = 1.3

    Y_epsilon = 0.25 + 0.75 / epsilon_a
    # 齿型系数
    Y_Fa1 = f_cha_10_5_Fa.x2y(z1)
    Y_Fa2 = f_cha_10_5_Fa.x2y(z2)
    # 应力修正系数
    Y_Sa1 = f_cha_10_5_Sa.x2y(z1)
    Y_Sa2 = f_cha_10_5_Sa.x2y(z2)

    # 弯曲疲劳寿命系数
    K_FN1 = f_fig_10_18.x2y(np.log10(N1))
    K_FN2 = f_fig_10_18.x2y(np.log10(N2))

    sigma_F_1 = K_FN1 * sigma_Flim1 / S_
    sigma_F_2 = K_FN2 * sigma_Flim2 / S_

    YYS1 = Y_Fa1 * Y_Sa1 / sigma_F_1
    YYS2 = Y_Fa2 * Y_Sa2 / sigma_F_2

    YYS = max(YYS1, YYS2)

    m_t = (2*K_Ft*T_1*Y_epsilon/(phi_d*z1**2)*YYS)**(1/3)
    print('试算 m_t = {:.2f} mm'.format(m_t))

    # 调整齿轮模数
    d_1 = m_t * z1
    v = np.pi * d_1 * n / (60*1000)

    b = phi_d * d_1

    h = (2*h_a_star + c_star)*m_t

    b_div_h = b/h

    K_v = f_fig_10_8.x2y(v)

    F_t1 = 2*T_1/d_1
    K_Fa = 1.2 if K_A*F_t1/b < 100 else 1
    K_Hb = f_cha_10_4.x2y(b)

    K_Fb = f_fig_10_13.y2x(K_Hb, b_div_h)
    print('K_Fb = {:.2f}'.format(K_Fb))

    K_F = K_A * K_v * K_Fa * K_Fb

    m_F = m_t * (K_F/K_Ft)**(1/3)
    print('实际 m_F = {:.2f} mm'.format(m_F))

    d_1F = m_F * z1
    print('实际 d_1F = {:.2f} mm'.format(d_1F))

    print('齿面接触疲劳强度计算: m_H = {:.3f}, d_H = {:.3f}'.format(m_H, d_1H))
    print('齿根弯曲疲劳强度计算: m_F = {:.3f}, d_F = {:.3f}'.format(m_F, d_1F))

    m = int(np.ceil(m_F*10)/10)
    m = max(m, 2)
    d1 = d_1H

    z1 = int(np.round(d1 / m))
    z2 = int(np.round(z1 * i))

    d1 = z1 * m
    d2 = z2 * m
    a = (d1+d2)/2
    b2 = round(phi_d * d1,2)
    b1 = b2 + 5

    result = '''
    主要设计结论:
    齿数z1 = {}
    齿数z2 = {}
    模数m = {} mm
    压力角alpha = {}°
    中心距a = {} mm
    齿宽b1 = {} mm
    齿宽b2 = {} mm
    小齿轮选用40Cr(调质),
    大齿轮选用45钢(调质),
    7级精度
    '''
    print(result.format(z1, z2, m, int(np.rad2deg(alpha)), int(a), int(b1), int(b2)))
    return z1,z2,m,b1,b2,a


def design_all(F_w, v_w, D):
    # 工作力矩
    T = F_w * D / 2 # N * m
    # 工作转速
    omega = v_w / (D / 2 * 0.001) # rad/s
    # 工作功率
    P_w = T * omega # W
    n_w = 60 * omega / (2 * np.pi)
    print('工作转速：{:.3f} rpm'.format(n_w))
    # 13页表格
    cls2eta = {
        '带': 0.96,
        '联轴器': 0.99,
        '链': 0.96,
        '轴承': 0.98,
        '齿轮': 0.98,
    }
    # 简图中统计
    cls_count = {
        '带': 1,
        '联轴器': 1,
        '链': 1,
        '轴承': 4,
        '齿轮': 2,
    }
    eta = 1
    for cls, count in cls_count.items():
        eta *= cls2eta[cls] ** count
    print('总效率为: {:.3f}'.format(eta))
    P_m = T * omega / eta
    print('电机所需功率为：{:.3f} W'.format(P_m))
    n_m = 1455
    i = n_m / n_w
    print('总传动比为:{:.3f}'.format(i))
    i_1 = np.sqrt(1.3 * i)
    i_2 = i / i_1
    print('i1 = {:.3f}, i2 = {:.3f}'.format(i_1, i_2))
    n1 = n_m
    n2 = n1 / i_1
    n3 = n2 / i_2
    print('轴1的转速为:{:.3f}, 轴2的转速为:{:.3f}, 轴3的转速为:{:.3f}'.format(n1, n2, n3))
    eta_1 = cls2eta['联轴器'] * cls2eta['轴承']
    eta_2 = cls2eta['齿轮'] * cls2eta['轴承']
    eta_3 = cls2eta['齿轮'] * cls2eta['轴承']
    P_1 = P_w * eta_1
    P_2 = P_1 * eta_2
    P_3 = P_2 * eta_3
    print('P1 = {:.3f} W, P2 = {:.3f} W, P3 = {:.3f} W'.format(P_1, P_2, P_3))
    # 查表
    A0 = 103
    d1 = A0 * (0.001 * P_1/n1)**(1/3)
    d2 = A0 * (0.001 * P_2/n2)**(1/3)
    d3 = A0 * (0.001 * P_3/n3)**(1/3)
    print('d1 = {:.3f} mm, d2 = {:.3f} mm, d3 = {:.3f} mm'.format(d1, d2, d3))
    T_1 = 9.55 * P_1 / n1
    T_2 = 9.55 * P_2 / n2
    T_3 = 9.55 * P_3 / n3
    print('T1 = {:.3f} N*m, T2 = {:.3f} N*m, T3 = {:.3f} N*m'.format(T_1, T_2, T_3))
    out_shaft = ((d1,d2,d3),(n1,n2,n3),(P_1,P_2,P_3),(T_1,T_2,T_3))
    out1 = design_gear(P_1*0.001,n1,i_1,cal_N(n1),17)
    out2 = design_gear(P_2*0.001,n2,i_2,cal_N(n2),20)
    return out1, out2, out_shaft


