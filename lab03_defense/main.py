import math as np


def f(x):
    return np.sin(x)


def fi(x):
    return x - f(x) / np.cos(x)


def search_root(a, b, eps, N):
    n = 0
    x = a
    if f(a) <= 0 and f(b) > 0 or f(a) >= 0 and f(b) < 0:
        y = fi(x)
        delta = abs(x - y)
        x = y
        n += 1
        while eps <= delta < 10 ** 10 and n < N:
            y = fi(x)
            delta = abs(x - y)
            x = y
            n += 1

        if a <= y <= b:
            table['ab'].append(str('[' + str(round(a, 3)) + ';' + str(round(b, 3)) + ']'))
            table['x'].append(round(y, 6))
            table['fx'].append(abs(round(f(y), 6)))
        else:
            table['ab'].append(str('[' + str(round(a, 3)) + ';' + str(round(b, 3)) + ']'))
            table['x'].append(5 * '-')
            table['fx'].append(5 * '-')

        table['n'].append(n)


table = {'ab': [], 'x': [], 'fx': [], 'n': []}

a = float(input('Введите начало интервала: '))
b = float(input('Введите конец интервала: '))
h = float(input('Введите шаг: '))
eps = 1e-5
n = 100
while a < b:
    if (a + h) < b:
        search_root(a, a + h, eps, n)
    else:
        search_root(a, b, eps, n)
    a += h

if table['ab'] != []:
    print(5 * ' ', 'n', 10 * ' ', 'ab', 10 * ' ', 'x', 10 * ' ', 'fx', 10 * ' ' \
          , 'N', 10 * ' ')
    for i in range(len(table['ab'])):
        if table['x'][i] != 5 * '-':
            if table['x'][i] >= 0: table['x'][i] = ' ' + str(table['x'][i])
            if table['fx'][i] >= 0: table['fx'][i] = ' ' + str(table['fx'][i])
        print((str(i + 1)).center(13), str(table['ab'][i]).center(14), \
              str(table['x'][i]).center(9), str(table['fx'][i]).center(16), \
              str(table['n'][i]).center(9))
else:
    print("Корней на данном интервале нет ")