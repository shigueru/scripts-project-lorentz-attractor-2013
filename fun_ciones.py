# -*- coding: utf-8 -*-
# funciones que generan el atractor de lorentz


def v_x(af, yf, xf):
    d_x = af * (yf - xf)
    return d_x


def v_y(bf, xf, zf, yf):
    d_y = xf * (bf - zf) - yf
    return d_y


def v_z(xf, yf, cf, zf):
    d_z = xf * yf - (cf * zf)
    return d_z
