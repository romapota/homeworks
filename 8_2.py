import matplotlib.pyplot as plt
from math import sin, cos
from sympy import *
import pylab
from matplotlib.widgets import Button, Slider, RadioButtons, CheckButtons

colors: dict
styles: dict
x_kas: list
y_kas: list
x_new: int
x_old: int
x: list
y: list
check_flag: bool
button_flag: bool
flag_update: bool
def main():
    x_kas = []
    y_kas = []
    def addGraph(graph_axes, x, y, x_point, y_point):
        graph_axes.plot(x, y)
        graph_axes.plot(x_point, y_point, 'o', color='k')
    def updateGraph():#обновление графика
        global check_flag, button_flag, radiobuttons_color, radiobuttons_style, flag_update, x_old
        graph_axes.clear()
        colors = {'Красный': 'r', 'Синий': 'b', 'Зеленый': 'g'}
        styles = {'Сплошная': '-', 'Пунктир': '--', 'Точки': 'dotted'}
        color = colors[radiobuttons_color.value_selected]
        style = styles[radiobuttons_style.value_selected]
        if flag_update:
            x_new = slider_x.val
            x_old = x_new
            flag_update = False
        if flag_update == False:
            x_new = x_old
        if button_flag:
            x_new = 0
            button_flag = False
        if check_flag:
            y_new = sin(x_new) * cos(x_new ** 2 + 5)
            x_kas = []
            y_kas = []
            for delx in range(0, 5 + 1):  # значения для касательной в т. (0.3, 0.101)
                x_z = + delx / 10
                y_z = (sin(x_new) * cos(x_new ** 2 + 5)) + ((-2 * x_new * sin(x_new) * sin(x_new ** 2 + 5) + cos(x_new) * cos(x_new ** 2 + 5)) * (x_z - x_new))
                x_kas.append(x_z)
                y_kas.append(y_z)
            graph_axes.plot(x, y, color = color, linestyle = style)
            graph_axes.plot(x_new, y_new, 'o', color='k')
            graph_axes.plot(x_kas, y_kas, color = 'k')
        if check_flag == False:
            y_new = sin(x_new) * cos(x_new ** 2 + 5)
            graph_axes.plot(x, y, color = color, linestyle = style)
            graph_axes.plot(x_new, y_new, 'o', color='k')
        pylab.draw()
    def onChangeGraph(value):
        global flag_update
        flag_update = True
        updateGraph()
    def onCheckClicked(label):
        global check_flag
        if label == 'Касательная':
            check_flag = not check_flag
        updateGraph()
    def onButtonClickes(label):
        global button_flag
        button_flag = True
        updateGraph()
    def onRadioButtonsClicked_color(label):
        updateGraph()
    def onRadioButtonsClicked_style(label):
        updateGraph()
    global check_flag, button_flag, radiobuttons_color, radiobuttons_style, flag_update, x_old
    check_flag = False
    button_flag = False
    flag_update = False
    x_old = 0
    x_max = 5/10 + 0.1
    xx = 0
    x = []
    y = []
    for delx in range(0, 5+1):#значения для графика функции
        x_z =+ delx/10
        y_z = sin(x_z)*cos(x_z**2+5)
        x.append(x_z)
        y.append(y_z)

    fig, graph_axes = pylab.subplots()
    graph_axes.grid()
    addGraph(graph_axes, x, y, 0.3, 0.1)

    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.55)

    axes_slider_x = plt.axes([0.05, 0.35, 0.85, 0.04])
    slider_x = Slider(axes_slider_x, label = 'x', valmin=0, valmax=max(x), valinit=0)#создание слайдера
    slider_x.on_changed(onChangeGraph)#отслеживание изменения слайдера

    axes_checkbuttons = plt.axes([0.0, 0.15, 0.2, 0.1])
    check_button_kasat = CheckButtons(axes_checkbuttons, ['Касательная'], [False])
    check_button_kasat.on_clicked(onCheckClicked)

    axes_button_add = plt.axes([0.7, 0.05, 0.25, 0.075])
    button_delete = Button(axes_button_add, 'Сбросить')
    button_delete.on_clicked(onButtonClickes)
    axes_radiobuttons = plt.axes([0.25, 0.05, 0.2, 0.2])
    radiobuttons_color = RadioButtons(axes_radiobuttons,['Красный', 'Синий', 'Зеленый'])
    radiobuttons_color.on_clicked(onRadioButtonsClicked_color)
    axes_radiobuttons_two = plt.axes([0.45, 0.05, 0.2, 0.2])
    radiobuttons_style = RadioButtons(axes_radiobuttons_two,['Сплошная', 'Пунктир', 'Точки'])
    radiobuttons_color.on_clicked(onRadioButtonsClicked_style)

    updateGraph()
    pylab.show()



if __name__ == '__main__':
    main()
