import matplotlib.pyplot as plt
import numpy as np
a, b, c, d, e = -12, -18, 5, 10, -30
limit = 10
step = 0.01
step_acr = 0.000001
line_style = '-'
direct_up = True
color = 'b'
b_up,b_down,r_up,r_down,root = True,True,True,True,True

def switch_line():
    global line_style
    if line_style == '--':
        line_style = '-'
    else:
        line_style = '--'
    return line_style

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color

def func(x):
    f = a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e
    return f

x = np.arange(-limit, limit + step, step)
x_change = [(-limit, 'limit')]
for i in range(len(x) - 1):
    if func(x[i]) > 0 and func(x[i + 1]) < 0 or func(x[i]) < 0 and func(x[i + 1]) > 0:
        x_acr = np.arange(x[i], x[i + 1] + step_acr, step_acr)
        for j in range(len(x_acr) - 1):
            if func(x_acr[j]) > 0 and func(x_acr[j + 1]) < 0 or func(x_acr[j]) < 0 and func(x_acr[j + 1]) > 0:
                x_change.append((x_acr[j], 'zero'))

    if direct_up:
        if (func(x[i])) > func(x[i + 1]):
            direct_up = False
            x_change.append((x[i], 'dir'))
    else:
        if func(x[i]) < func(x[i + 1]):
            direct_up = True
            x_change.append((x[i], 'dir'))

x_change.append((limit, 'limit'))
for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        if root:
            lbl = 'Корень уравнения'
            root = False
        else:
            lbl=None
        plt.plot(x_change[i][0], func(x_change[i][0]), 'go',label = lbl)
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        if color == 'r' and line_style == '-' and b_up:
            lbl = 'Убывающая выше ноля'
            b_up = False
        elif color == 'r' and line_style == '--' and b_down:
            lbl = 'Убывающая ниже ноля'
            b_down = False
        if color == 'b' and line_style == '-' and r_up:
            lbl = 'Возрастающая выше ноля'
            r_up = False
        elif color == 'b' and line_style == '--' and r_down:
            lbl = 'Возрастающая ниже ноля'
            r_down = False
        plt.plot(cur_x, func(cur_x), switch_color(),label = lbl)
        lbl = None


plt.grid()
plt.legend()
plt.show()
