import matplotlib.pyplot as plt
from math import sin, cos
from sympy import *
from scipy import integrate
x_max = 5 / 10 + 0.1
x: list
y: list
x1_list: list
y1_list: list
x2_list: list
y2_list: list
x_kas: list
y_kas: list
x_norm: list
y_norm: list
x_kas_2: list
y_kas_2: list
x_mo: float
y_mo: float
z_x: float
y_z: float
delx: int
def main():
    def integr(x):
        return sin(x)*cos(x**2+5)
    x1, y1 = symbols('x1 y1')
    function = 'sin(x)*cos(x**2+5)'
    x_max = 5/10 + 0.1
    x = []
    y = []
    x1_list = []
    y1_list = []
    x2_list = []
    y2_list = []
    x_kas = []
    y_kas = []
    x_norm = []
    y_norm = []
    x_kas_2 = []
    y_kas_2 = []
    x_mo = 0.3
    y_mo = 0.101
    for delx in range(0, 5+1):#значения для графика функции
        x_z =+ delx/10
        y_z = sin(x_z)*cos(x_z**2+5)
        x.append(x_z)
        y.append(y_z)
    for delx in range(0, 5+1):#значения для график первой производной
        x_z =+ delx/10
        y_z = -2*x_z*sin(x_z)*sin(x_z**2 + 5) + cos(x_z)*cos(x_z**2 + 5)
        x1_list.append(x_z)
        y1_list.append(y_z)
    for delx in range(0, 5+1):#значения для график второй производной
        x_z =+ delx/10
        y_z = -4*x_z**2*sin(x_z)*cos(x_z**2 + 5) - 4*x_z*sin(x_z**2 + 5)*cos(x_z) - 2*sin(x_z)*sin(x_z**2 + 5) - sin(x_z)*cos(x_z**2 + 5)
        x2_list.append(x_z)
        y2_list.append(y_z)
    for delx in range(0, 5+1):#значения для касательной в т. (0.3, 0.101)
        x_z =+ delx/10
        y_z = (sin(x_mo)*cos(x_mo**2+5)) + ((-2*x_mo*sin(x_mo)*sin(x_mo**2 + 5) + cos(x_mo)*cos(x_mo**2 + 5))*(x_z-x_mo))
        x_kas.append(x_z)
        y_kas.append(y_z)
    for delx in range(0, 5+1):#значения для нормали в т. (0.3, 0.101)
        x_z =+ delx/10
        y_z = (sin(x_mo)*cos(x_mo**2+5)) - ((1/(-2*x_mo*sin(x_mo)*sin(x_mo**2 + 5) + cos(x_mo)*cos(x_mo**2 + 5)))*(x_z-x_mo))
        x_norm.append(x_z)
        y_norm.append(y_z)
    for x_zn in range(0, 6):
        x_zh_z = x_zn/10
        for delx in range(0, 5 + 1):  # значения для касательной в т. (0.3, 0.101)
            x_z = + delx / 10
            y_z = (sin(x_zh_z) * cos(x_zh_z ** 2 + 5)) + ((-2 * x_zh_z * sin(x_zh_z) * sin(x_zh_z ** 2 + 5) + cos(x_zh_z) * cos(x_zh_z ** 2 + 5)) * (x_z - x_zh_z))
            x_kas_2.append(x_z)
            y_kas_2.append(y_z)
            plt.plot(x_kas_2, y_kas_2, color='orange')  # график касательной
    plt.plot(x, y, color = 'green')#график функции
    plt.plot(x1_list, y1_list, color = 'blue')#первая производная
    plt.plot(x2_list, y2_list, color = 'red')#график второй производной
    plt.plot([min(x)], [min(y)], 'o', color = 'b')#точка с минимальным значением фукнции
    plt.plot([max(x)], [max(y)], 'o', color='b')#точка с максимальным значением функции
    plt.plot(x_kas, y_kas, linestyle = '--', color = 'k')#график касательной
    plt.plot(x_norm, y_norm, linestyle = '--', color = 'k')#график нормали
    print('Длина дуги = ', (integrate.quad(integr, 0, 0.5)[0]))
    plt.show()



if __name__ == '__main__':
    main()
