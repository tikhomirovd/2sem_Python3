def f(x): return x * x - 4


def fi(x): return x + f(x)


def itera(a, b, eps, N):
    err = 0
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
            # print(y,x)
            x = y
            n += 1

        if a <= y <= b:
            table['ab'].append(str('[' + str(round(a, 3)) + ';' + str(round(b, 3)) + ']'))
            table['x'].append(round(y, 6))
            table['fx'].append(round(f(y), 6))
        else:
            err = 2
            table['ab'].append(str('[' + str(round(a, 3)) + ';' + str(round(b, 3)) + ']'))
            table['x'].append(5 * '-')
            table['fx'].append(5 * '-')

        if n == N: err = 1
        table['n'].append(n)
        table['err'].append(err)


table = {'ab': [], 'x': [], 'fx': [], 'n': [], 'err': []}

a = float(input('Введите начало интервала: '))
b = float(input('Введите конец интервала: '))
h = float(input('Введите шаг: '))
eps = float(input('Введите точность: '))
n = int(input('Введите максимальное кол-во итераций: '))

while a < b:
    if (a + h) < b:
        itera(a, a + h, eps, n)
    else:
        itera(a, b, eps, n)
    a += h

if table['ab'] != []:
    print(5 * ' ', 'n', 10 * ' ', 'ab', 10 * ' ', 'x', 10 * ' ', 'fx', 10 * ' ' \
          , 'N', 10 * ' ', 'err')
    for i in range(len(table['ab'])):
        if table['x'][i] != 5 * '-':
            if table['x'][i] >= 0: table['x'][i] = ' ' + str(table['x'][i])
            if table['fx'][i] >= 0: table['fx'][i] = ' ' + str(table['fx'][i])
        print((str(i + 1) + '.').center(13), str(table['ab'][i]).center(14), \
              str(table['x'][i]).center(9), str(table['fx'][i]).center(16), \
              str(table['n'][i]).center(9), str(table['err'][i]).rjust(9))

