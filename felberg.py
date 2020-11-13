# -*- coding: utf-8 -*-
import cf
import fun_ciones
import math


def calculo(hk, xk, yk, zk, ak, bk, ck, ek):
    r = 1
    while r > ek:
        k1_x = hk * fun_ciones.v_x(ak, yk, xk)
        k1_y = hk * fun_ciones.v_y(bk, xk, zk, yk)
        k1_z = hk * fun_ciones.v_z(xk, yk, ck, zk)
        k2_x = hk * fun_ciones.v_x(ak, yk + k1_y / 4, xk + k1_x / 4)
        k2_y = (hk * fun_ciones.v_y(bk, xk + k1_x / 4, zk + k1_z / 4, yk +
        k1_y / 4))
        k2_z = (hk * fun_ciones.v_z(xk + k1_x / 4, yk + k1_y / 4, ck, zk +
        k1_z / 4))
        k3_x = (hk * fun_ciones.v_x(ak, yk + cf.c1 * k1_y + cf.c2 * k2_y, xk +
        cf.c1 * k1_x + cf.c2 * k2_x))
        k3_y = (hk * fun_ciones.v_y(bk, xk + cf.c1 * k1_x + cf.c2 * k2_x, zk +
        cf.c1 * k1_z + cf.c2 * k2_z, yk + cf.c1 * k1_y + cf.c2 * k2_y))
        k3_z = (hk * fun_ciones.v_z(xk + cf.c1 * k1_x + cf.c2 * k2_x, yk +
        cf.c1 * k1_y + cf.c2 * k2_y, ck, zk + cf.c1 * k1_z + cf.c2 * k2_z))
        k4_x = (hk * + fun_ciones.v_x(ak, yk + cf.c3 * k1_y - cf.c4 * k2_y +
        cf.c5 * k3_y, xk + cf.c3 * k1_x - cf.c4 * k2_x + cf.c5 * k3_x))
        k4_y = (hk * fun_ciones.v_y(bk, xk + cf.c3 * k1_x - cf.c4 * k2_x +
        cf.c5 * k3_x, zk + cf.c3 * k1_z - cf.c4 * k2_z + cf.c5 * k3_z, yk +
        cf.c3 * k1_y - cf.c4 * k2_y + cf.c5 * k3_y))
        k4_z = (hk * fun_ciones.v_z(xk + cf.c3 * k1_x - cf.c4 * k2_x +
        cf.c5 * k3_x, yk + cf.c3 * k1_y - cf.c4 * k2_y + cf.c5 * k3_y, ck, zk +
        cf.c3 * k1_z - cf.c4 * k2_z + cf.c5 * k3_z))
        k5_x = (hk * fun_ciones.v_x(ak, yk + cf.c6 * k1_y - cf.c7 * k2_y -
        cf.c8 * k3_y, xk + cf.c6 * k1_x - cf.c7 * k2_x - cf.c8 * k3_x))
        k5_y = (hk * fun_ciones.v_y(bk, xk + cf.c6 * k1_x - cf.c7 * k2_x -
        cf.c8 * k3_x, zk + cf.c6 * k1_z - cf.c7 * k2_z - cf.c8 * k3_z, yk +
        cf.c6 * k1_y - cf.c7 * k2_y - cf.c8 * k3_y))
        k5_z = (hk * fun_ciones.v_z(xk + cf.c6 * k1_x - cf.c7 * k2_x -
        cf.c8 * k3_x, yk + cf.c6 * k1_y - cf.c7 * k2_y - cf.c8 * k3_y, ck, zk +
        cf.c6 * k1_z - cf.c7 * k2_z - cf.c8 * k3_z))
        k6_x = (hk * fun_ciones.v_x(ak, yk - cf.c9 * k1_y + cf.c10 * k2_y +
        cf.c11 * k3_y - cf.c12 * k5_y, xk - cf.c9 * k1_x + cf.c10 * k2_x +
        cf.c11 * k3_x - cf.c12 * k5_x))
        k6_y = (hk * fun_ciones.v_y(bk, xk - cf.c9 * k1_x + cf.c10 * k2_x +
        cf.c11 * k3_x - cf.c12 * k5_x, zk - cf.c9 * k1_z + cf.c10 * k2_z +
        cf.c11 * k3_z - cf.c12 * k5_z, yk - cf.c9 * k1_y + cf.c10 * k2_y +
        cf.c11 * k3_y - cf.c12 * k5_y))
        k6_z = (hk * fun_ciones.v_z(xk - cf.c9 * k1_x + cf.c10 * k2_x +
        cf.c11 * k3_x - cf.c12 * k5_x, yk - cf.c9 * k1_y + cf.c10 * k2_y +
        cf.c11 * k3_y - cf.c12 * k5_y, ck, zk - cf.c9 * k1_z + cf.c10 * k2_z +
        cf.c11 * k3_z - cf.c12 * k5_z))
        #----------------------------------------------
        sum_x4 = cf.c13 * k1_x + cf.c14 * k3_x + cf.c15 * k4_x - cf.c16 * k5_x
        sum_x5 = (cf.c17 * k1_x + cf.c18 * k3_x + cf.c19 * k4_x - cf.c20 *
        k5_x + cf.c21 * k6_x)
        sum_y4 = cf.c13 * k1_y + cf.c14 * k3_y + cf.c15 * k4_y - cf.c16 * k5_y
        sum_y5 = (cf.c17 * k1_y + cf.c18 * k3_y + cf.c19 * k4_y - cf.c20 *
        k5_y + cf.c21 * k6_y)
        sum_z4 = cf.c13 * k1_z + cf.c14 * k3_z + cf.c15 * k4_z - cf.c16 * k5_z
        sum_z5 = (cf.c17 * k1_z + cf.c18 * k3_z + cf.c19 * k4_z - cf.c20 *
        k5_z + cf.c21 * k6_z)
        # ###############################################
        x_4 = xk + sum_x4
        x_5 = xk + sum_x5
        y_4 = yk + sum_y4
        y_5 = yk + sum_y5
        z_4 = zk + sum_z4
        z_5 = zk + sum_z5
        x_e = math.fabs(x_5 - x_4)
        y_e = math.fabs(y_5 - y_4)
        z_e = math.fabs(z_5 - z_4)
        et = max(x_e, y_e, z_e)
        r = et / hk
        delta = 0.840896 * (ek / r) ** (1.0 / 4.0)
        hk = delta * hk
    return (x_5, y_5, z_5, hk)