import matplotlib.pyplot as plt
from math import sin, cos
from sympy import *
import pylab
from matplotlib.widgets import Button, Slider, RadioButtons, CheckButtons
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
    def addGraphBase(graph_axes, x, y):#базовая функция
        graph_axes.plot(x, y, color = 'red')
    def addGraphFirst(graph_first, x1_list, y1_list):#первая производная
        graph_first.plot(x1_list, y1_list, color = 'green')
    def addGraphSecond(graph_second, x2_list, y2_list):#первая производная
        graph_second.plot(x2_list, y2_list, color = 'blue')
    def addGraphPoint(graph_point, x, y):
        graph_point.plot(x, y, color = 'red')
        graph_point.plot(min(x), min(y), 'o', color = 'k')
        graph_point.plot(max(x), max(y), 'o', color='k')
    def addGraphTangent(graph_tangent, x, y, x_kas, y_kas):
        graph_tangent.plot(x, y, color='red')
        graph_tangent.plot(x_kas, y_kas, '--', color='k')
    def addGraphNormal(graph_normal, x, y, x_norm, y_norm):
        graph_normal.plot(x, y, color='red')
        graph_normal.plot(x_norm, y_norm, '--', color='k')
    def addGraphStratification(graph_stratification, x, y):
        graph_stratification.plot(x, y, color = 'r')
        for x_zn in range(0, 6):
            x_zh_z = x_zn / 10
            x_kas_2 = []
            y_kas_2 = []
            for delx in range(0, 5 + 1):  # значения для касательной в т. (0.3, 0.101)
                x_z = + delx / 10
                y_z = (sin(x_zh_z) * cos(x_zh_z ** 2 + 5)) + ((-2 * x_zh_z * sin(x_zh_z) * sin(x_zh_z ** 2 + 5) + cos(x_zh_z) * cos(x_zh_z ** 2 + 5)) * (x_z - x_zh_z))
                x_kas_2.append(x_z)
                y_kas_2.append(y_z)
                graph_stratification.plot(x_kas_2, y_kas_2, color='orange')  # график касательной
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
    # plt.plot(x, y, color = 'green')#график функции
    # plt.plot(x1_list, y1_list, color = 'blue')#первая производная
    # plt.plot(x2_list, y2_list, color = 'red')#график второй производной
    # plt.plot([min(x)], [min(y)], 'o', color = 'b')#точка с минимальным значением фукнции
    # plt.plot([max(x)], [max(y)], 'o', color='b')#точка с максимальным значением функции
    # plt.plot(x_kas, y_kas, linestyle = '--', color = 'k')#график касательной
    # plt.plot(x_norm, y_norm, linestyle = '--', color = 'k')#график нормали
    #график самой функции
    fig, graph_axes = pylab.subplots()
    graph_axes.set_title('График функции')
    graph_axes.grid()
    addGraphBase(graph_axes, x, y)

    #график первой производной
    fig, graph_first = pylab.subplots()
    graph_first.set_title('График первой производной')
    graph_first.grid()
    addGraphFirst(graph_first, x1_list, y1_list)

    #график второй производной
    fig, graph_second = pylab.subplots()
    graph_second.set_title('График второй производной')
    graph_second.grid()
    addGraphSecond(graph_second, x2_list, y2_list)

    #точки с минимальным и максимальным значением
    fig, graph_point = pylab.subplots()
    graph_point.set_title('Точки с наибольшим и наименьшим значением функции')
    graph_point.grid()
    addGraphPoint(graph_point, x, y)

    #график касательной
    fig, graph_tangent = pylab.subplots()
    graph_tangent.set_title('Касательная к графику')
    graph_tangent.grid()
    addGraphTangent(graph_tangent, x, y, x_kas, y_kas)

    #график нормали
    fig, graph_normal = pylab.subplots()
    graph_normal.set_title('Нормаль к графику')
    graph_normal.grid()
    addGraphNormal(graph_normal, x, y, x_norm, y_norm)

    #рафик расслоения
    fig, graph_stratification = pylab.subplots()
    graph_stratification.set_title('Касательное расслоение')
    graph_stratification.grid()
    addGraphStratification(graph_stratification, x, y)

    plt.show()


if __name__ == '__main__':
    main()
