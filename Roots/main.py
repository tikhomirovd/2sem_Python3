# Программа для нахождения приближенных корней функции смешанным методом
#               Тихомиров


# left - левая граница интервала
# right - правая граница интервала
# n - максимальное количество итераций
# eps - точность
# h - шаг
# funk_arr - массив иксов
# step_arr - массив иксов с шагом h
# table_m, row_m - массив с данными одной строчки таблицы
# k - номер корня
# it_num - число итераций

from tkinter import *

import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.geometry('700x550')
root.title('Приближенные корни')


# ОБЪЯВЛЕНИЕ ФУНКЦИЙ
# Функция
def f(x):
    return p.sin(x)


# Первая производная функции
def fi(x):
    return np.cos(x)


# Вторая производная функции
def fii(x):
    return -np.sin(x)


# Функция для отображения шага
def g(x):
    return x * 0


# Функция для прокрутки результатов
def scroll_function(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


# Очистка таблицы, если нажата кнопка
def but_press(event):
    for child in can_frame.winfo_children():
        child.destroy()


# Проверка ввода
def safe_get(en):
    inp = en.get()
    try:
        float(inp)
        if en == n_en:
            return int(inp)
        return float(inp)
    except ValueError:
        return '0'


# Показать график функции
def show_plot():
    # Получение переменных
    A = safe_get(a_en)
    B = safe_get(b_en)
    n = safe_get(n_en)
    eps = safe_get(eps_en)
    h = safe_get(h_en)
    if A == '0' or B == '0' or n == '0' or eps == '0' or h == '0':
        return 0
    elif B - A < h or B < A:
        return 0
    elif n <= 0 or eps <= 0 or h <= 0:
        return 0

    # Создание массивов значений переменной х
    func_arr = np.arange(A, B, 0.005)
    step_arr = np.arange(A, B + h, h)
    if step_arr[len(step_arr) - 1] > B:
        step_arr[len(step_arr) - 1] = B

    # Поиск экстремумов
    for i in func_arr:
        if abs(fi(i)) <= 0.0025:
            scatter1 = plt.scatter(i, f(i), c='g')

    # Отображение корней
    for i in func_arr:
        if abs(f(i)) <= 0.0025:
            scatter2 = plt.scatter(i, f(i), c='b')

    # Вывод графика и всех обозначений

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('sin(x)')
    plt.plot(func_arr, f(func_arr), 'r')

    plt.axis([A, B, -6, 6])
    plt.grid(True)
    plt.show()


# Главная функция программы
def main_f():
    # Закрытие графика и удаление таблицы
    for child in can_frame.winfo_children():
        child.destroy()

    # Получение переменных
    left = safe_get(a_en)
    right = safe_get(b_en)
    n = safe_get(n_en)
    eps = safe_get(eps_en)
    h = safe_get(h_en)
    if left == '0' or right == '0' or n == '0' or eps == '0' or h == '0':
        return 0
    elif right - left < h or right < left:
        return 0
    elif n <= 0 or eps <= 0 or h <= 0:
        return 0

    # Вывод заголовка таблицы
    table_m = ['Номер', 'Интервал', 'Значение корня', 'Значение функции',
               'Количество итераций', 'Код ошибки']
    for i in range(len(table_m)):
        Label(can_frame, text=table_m[i]).grid(row=0, column=i + 1, sticky='nsew')

    # Создание массивов переменной x
    func_arr = np.arange(left, right, 0.005)
    step_arr = np.arange(left, right + h, h)
    if step_arr[len(step_arr) - 1] > right:
        step_arr[len(step_arr) - 1] = right

    # Уточнение корней смешанным методом
    k = 0
    for i in range(len(step_arr) - 1):

        # Проверка на существование корня в интервале
        if f(step_arr[i]) >= 0 > f(step_arr[i + 1]) or \
                f(step_arr[i]) <= 0 < f(step_arr[i + 1]) or \
                (f(step_arr[i + 1]) == 0 and i == len(step_arr) - 2):
            k += 1
            it_num = 0
            a = step_arr[i]
            b = step_arr[i + 1]
            x2 = (a + b)
            x1 = (a + b) / 2

            # Уточнение корня
            while abs(a - b) > eps:
                it_num += 1

                if fi((a + b) / 2) * fii((a + b) / 2) > 0:
                    a = a - f(a) * (b - a) / (f(b) - f(a))
                    b = b - f(b) / fi(b)
                else:
                    a = a - f(a) / fi(a)
                    b = b - f(b) * (b - a) / (f(b) - f(a))

            x = (a + b) / 2


            # Вывод результатов в таблицу


            if eps < 1e-10:
                row_m = [k, ('%s  -  %s' % (step_arr[i], step_arr[i + 1])),
                         '-', '-', '-', 3]
            elif it_num > n:
                row_m = [k, ('%s  -  %s' % (step_arr[i], step_arr[i + 1])),
                         '-', '-', '-', 1]
            elif it_num == 0:
                row_m = [k, ('%s  -  %s' % (step_arr[i], step_arr[i + 1])),
                         '-', '-', '-', 2]
            elif x < step_arr[i] or x > step_arr[i + 1]:
                row_m = [k, ('%s  -  %s' % (step_arr[i], step_arr[i + 1])),
                         '-', '-', '-', 4]
            else:
                row_m = [k, ('%s  -  %s' % (step_arr[i], step_arr[i + 1])),
                         '{:3.5f}'.format(x), '{:1.0e}'.format(f(x)), it_num, 0]
            for i in range(len(row_m)):
                Label(can_frame, text=row_m[i]).grid(row=k, column=i + 1,
                                                     sticky='nsew')

    if k == 0:
        row_m = ['Корней нет', '','','','','']
        for i in range(len(row_m)):
            Label(can_frame, text=row_m[i]).grid(row=k, column=i + 1,
                                                 sticky='nsew')


root.bind('<Key>', but_press)

# Поля ввода переменных
a_lb = Label(text='Левая граница:')
a_en = Entry()
b_lb = Label(text='Правая граница:')
b_en = Entry()
n_lb = Label(text='Максимальное\nчисло итераций:')
n_en = Entry()
eps_lb = Label(text='Точность:')
eps_en = Entry()
h_lb = Label(text='Шаг:')
h_en = Entry()

# Описание ошибок и кнопки
error_info = Label(text='Описание ошибок:\n0 - нет ошибки\n1 - превышено\
    кол-во итераций\n2 - слишком большой eps\n3 - слишком маленький eps\
    \n4 - Выход за пределы отрезка')
solve_but = Button(text='Посчитать', command=main_f)
show_plot_but = Button(text='Показать график', command=show_plot)

table_frame = Frame(root, relief=GROOVE, bd=1)
table_frame.grid(row=3, column=0, columnspan=4)

canvas = Canvas(table_frame, width=550)
can_frame = Frame(canvas)
myscrollbar = Scrollbar(table_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

# Начальные значения переменных
a_en.insert(0, -1)
b_en.insert(0, 1)
n_en.insert(0, 10)
eps_en.insert(0, '0.00001')
h_en.insert(0, 1)

# Расположение всех виджетов
a_lb.grid(row=0, column=0, sticky='e')
a_en.grid(row=0, column=1, sticky='w')
b_lb.grid(row=1, column=0, sticky='e')
b_en.grid(row=1, column=1, sticky='w')
n_lb.grid(row=0, column=2, sticky='e')
n_en.grid(row=0, column=3, sticky='w')
eps_lb.grid(row=1, column=2, sticky='e')
eps_en.grid(row=1, column=3, sticky='w')
h_lb.grid(row=2, column=2, sticky='e')
h_en.grid(row=2, column=3, sticky='w')

error_info.grid(row=4, column=0, columnspan=2, rowspan=2)
solve_but.grid(row=4, column=2)
show_plot_but.grid(row=4, column=3)
myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=can_frame, anchor='nw')
can_frame.bind("<Configure>", scroll_function)

main_f()

for i in range(6):
    root.rowconfigure(i, weight=1)  
    if i < 4:
        root.columnconfigure(i, weight=1)

root.mainloop()
