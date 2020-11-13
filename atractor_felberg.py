# -*- coding: utf-8 -*-
# ---------------------
# proyecto : atractor de lorentz
# autor : shigueru nagata
# descripcion : programa que resuelve las ecuaciones del atractor de lorentz
#               utilizando el metodo de runge kutta felberg y  graficando
#               la solucion.
# ---------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import felberg

maxIt = 400000  # numero de iteraciones

# estado inicial
x = 0.0
y = 1.0
z = 0.0
a = 10.0
c = 8.0 / 3.0
b = 14.00
h = 1e-3  # paso de tiempo
e = 0.02  # tolerancia del error
t = 0
datos_x = []  # --------------------------
datos_y = []
datos_z = []  # listas con los resultados
datos_t = []  # --------------------------
# ####################################
# definimos la figura 3d
fig = plt.figure("atractor de lorenz")
ax = fig.gca(projection='3d')
# ####################################
for i in range(maxIt):
    (x, y, z, h) = felberg.calculo(h, x, y, z, a, b, c, e)
    t = t + h
    datos_x.append(x)
    datos_y.append(y)
    datos_z.append(z)
    datos_t.append(t)
# ###############
# proyeccion 3-d
# ##############
ax.plot(datos_x, datos_y, datos_z)
ax.set_xlabel("valores de x")
ax.set_ylabel("valores de y")
ax.set_zlabel("valores de z")
# ########################################################
# definimos las proyecciones en los planos X-Y , X-Z , Y-Z
# ########################################################
plt.figure("figura 1")
plt.title("proyeccion en los planos")
plt.subplot(321)
plt.plot(datos_x, datos_y)
plt.xlabel("valores de x")
plt.ylabel("valores de y")
plt.subplot(324)
plt.plot(datos_x, datos_z)
plt.xlabel("valores de x")
plt.ylabel("valores de z")
plt.subplot(325)
plt.plot(datos_y, datos_z)
plt.xlabel("valores de y")
plt.ylabel("valores de z")
# #####################################################
# definimos las proyecciones de los datos en el tiempo
# #####################################################
plt.ishold()
plt.figure("figura 2")
plt.plot(datos_t, datos_x, label="x")
plt.plot(datos_t, datos_y, label="y")
plt.plot(datos_t, datos_z, label="z")
plt.xlabel("valores de t")
plt.ylabel("valores de x-y-z")
plt.title("evolucion temporal")
plt.legend()
plt.show()

