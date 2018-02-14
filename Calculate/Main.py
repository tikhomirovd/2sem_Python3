# Данная программа выполняет сложение и вычитание
# В троично-симметричной системе счисления

# Тихомиров Дмитрий, ИУ7-25


# text0, text1 - Вспомогательный текст
# x_entry, y_entry - размер окошек для данных
# x_vidget, y_vidget - размер окошек виджета
# width, height - ширина и высота меню
# color - цвет фона
# root - главное окно
# drop_menu - выпадающее окно
# first_drop, second_drop, third_drop - три выпадающих окна
# btn_plus, btn_minus, btn_sqrt1,btn_sqrt2 - кнопки арифметических вычислений
# text_first_num, text_second_num - окна для ввода данных
# lbl_equal - знак равенства



from tkinter import *
from tkinter import messagebox


# Удаление всех полей
def deletion_all(entry1, entry2, text1):
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    text1.destroy()
    text1 = Label(width=width, height=height, bg=color)
    text1.place(x=x_entry, y=y_entry)

# Удалить поле суммы
def deletion_sum(text1):
    text1.destroy()
    text1 = Label(width=width, height=height, bg=color)
    text1.place(x=x_entry, y=y_entry)

# Проверка введённых данных
def check_input(num1):
    count = 0
    num1 = num1
    if num1 == '':
        return 0
    else:
        for i in num1:
            if i in ['+', '-', '0']:
                count += 1
        if count == len(num1):
            return 1
        else:
            return 0

# Проверка длины
def len_num(num1, num2):
    if len(num1) > len(num2):
        num2 = '0' * (len(num1) - len(num2) + 1) + num2
        num1 = '0' + num1
    else:
        num1 = '0' * (len(num2) - len(num1) + 1) + num1
        num2 = '0' + num2

    return num1, num2

# Сумма
def mathmatic_plus(entry1, entry2, text):
    num1 = entry1.get()
    num2 = entry2.get()

    if check_input(num1) == 0 or check_input(num2) == 0:
        messagebox.showerror('Ошибка!',
                             'Проверьте правильность введённых данных!')
    else:
        subresult = []

        num1, num2 = len_num(num1, num2)

        for i in range(len(num1) - 1, -1, -1):
            subresult.append(num1[i] + num2[i])

        try:
            vidget.destroy()
            vidget = Label(text='+')
            vidget.place(x=x_vidget, y=y_vidget)
        except:
            vidget = Label(text='+')
            vidget.place(x=x_vidget, y=y_vidget)

        while ('0+' in subresult or '+0' in subresult or '0-' in subresult
              or '-0' in subresult or '+-' in subresult or '-+' in subresult
              or '++' in subresult or '--' in subresult or '00' in subresult):
            result = []
            subvar = ''
            for g in subresult:
                if g == '0+' or g == '+0':
                    result.append('+' + subvar)
                    subvar = ''
                elif g == '0-' or g == '-0':
                    result.append('-' + subvar)
                    subvar = ''
                elif g == '+-' or g == '-+':
                    result.append('0' + subvar)
                    subvar = ''
                elif g == '++':
                    result.append('-' + subvar)
                    subvar = '+'
                elif g == '--':
                    result.append('+' + subvar)
                    subvar = '-'
                elif g == '00':
                    result.append('0' + subvar)
                    subvar = '0'
                else:
                    result.append(g + subvar)
            subresult = result

        result.reverse()
        text_result = ''.join(result)
        text.destroy()
        text = Label(width=width, height=height, bg=color, text=text_result)
        text.place(x=x_entry, y=y_entry)

# Разность
def mathmatic_minus(entry1, entry2, text):
    num1 = entry1.get()
    num2 = entry2.get()

    if check_input(num1) == 0 or check_input(num2) == 0:
        messagebox.showerror('Ошибка!',
                             'Проверьте правильность введённых данных!')
    else:
        subresult = []

        if len(num1) >= len(num2):
            num2 = '0' * (len(num1) - len(num2)) + num2
        else:
            num1 = '0' * (len(num2) - len(num1)) + num1

        for i in range(len(num1) - 1, -1, -1):
            subresult.append(num1[i] + num2[i])
        try:
            vidget.destroy()
            vidget2.destroy()
            vidget2 = Label(text='-')
            vidget2.place(x=x_vidget, y=y_vidget)
        except:
            vidget2 = Label(text='-')
            vidget2.place(x=x_vidget, y=y_vidget)

        while ('0+' in subresult or '+0' in subresult or '0-' in subresult
               or '-0' in subresult or '+-' in subresult
               or '-+' in subresult or '++' in subresult
               or '--' in subresult or '00' in subresult):
            result = []
            subvar = ''
            for g in subresult:
                if g == '0+':
                    result.append('-' + subvar)
                    subvar = ''
                elif g == '+0':
                    result.append('+' + subvar)
                    subvar = ''
                elif g == '0-':
                    result.append('+' + subvar)
                    subvar = ''
                elif g == '-0':
                    result.append('-' + subvar)
                    subvar = ''
                elif g == '+-':
                    result.append('-' + subvar)
                    subvar = '-'
                elif g == '-+':
                    result.append('+' + subvar)
                    subvar = '+'
                elif g == '++':
                    result.append('0' + subvar)
                    subvar = ''
                elif g == '--':
                    result.append('0' + subvar)
                    subvar = ''
                elif g == '00':
                    result.append('0' + subvar)
                    subvar = ''
                else:
                    result.append(g + subvar)
            subresult = result
        result.reverse()
        text_result = ''.join(result)
        text.destroy()
        text = Label(width=width, height=height, bg=color, text=text_result)
        text.place(x=x_entry, y=y_entry)

# Информация о программе
def info():
    text0 = 'Информация'
    text1 = '''Программа для выполнения арифметических действий в троичной
симметричноый системе счисления. \n\n
Тихомиров Дмитрий Алексеевич, ИУ7-25'''
    messagebox.showinfo(text0, text1)


x_entry = 370
y_entry = y_vidget = 30
x_vidget = 140
width = 15
height = 1
color = 'white'
vidget = None
vidget2 = None
result = None

root = Tk()
root.title('Калькулятор')
root.geometry('500x200')

drop_menu = Menu(root)
root.config(menu=drop_menu)

first_drop = Menu(drop_menu)
drop_menu.add_cascade(label='Чистка окон', menu=first_drop)
first_drop.add_command(label='Очистить все окна',
                command=lambda: deletion_all(text_first_num,
                                             text_second_num, text_result))
new_menu = Menu(first_drop)
first_drop.add_cascade(label='Очистить по одному', menu=new_menu)

new_menu.add_command(label='Очистить поле первого слагаемого',
                     command=lambda: text_first_num.delete(0, 'end'))
new_menu.add_command(label='Очистить поле второго слагаемого',
                     command=lambda: text_second_num.delete(0, 'end'))
new_menu.add_command(label='Очистить поле суммы',
                     command=lambda: deletion_sum(text_result))

second_drop = Menu(drop_menu)
drop_menu.add_cascade(label='Выполнение операций', menu=second_drop)
second_drop.add_command(label='Сложить',
                command=lambda: mathmatic_plus(text_first_num,
                                               text_second_num, text_result))
second_drop.add_command(label='Вычесть',
                command=lambda: mathmatic_minus(text_first_num,
                                                text_second_num, text_result))

third_drop = Menu(drop_menu)
drop_menu.add_cascade(label='Инфо', menu=third_drop)
third_drop.add_command(label='О программе', command=lambda: info())

btn_plus = Button(text='Сложить', width=10,
            command=lambda: mathmatic_plus(text_first_num,
                                           text_second_num, text_result))
btn_plus.place(x=150, y=170)

btn_minus = Button(text='Вычесть', width=10,
            command=lambda: mathmatic_minus(text_first_num,
                                            text_second_num, text_result))
btn_minus.place(x=240, y=170)

text_first_num = Entry(width=width)
text_first_num.place(x=10, y=y_entry)

text_second_num = Entry(width=width)
text_second_num.place(x=190, y=y_entry)

lbl_equal = Label(text='=')
lbl_equal.place(x=325, y=y_entry)

text_result = Label(width=width, height=height, bg=color)
text_result.place(x=x_entry, y=y_entry)


minus = Button(text="-", width=3,
               command=lambda: text_first_num.insert(END,"-"))
minus.place(x=5, y=55)
zero = Button(text="0", width=3,
               command=lambda: text_first_num.insert(END,"0"))
zero.place(x=40, y=55)

plus = Button(text="+", width=3,
              command=lambda: text_first_num.insert(END,"+"))
plus.place(x=75, y=55)


minus1 = Button(text="-", width=3,
               command=lambda: text_second_num.insert(END,"-"))
minus1.place(x=190, y=55)

zero1 = Button(text="0", width=3,
               command=lambda: text_second_num.insert(END,"0"))
zero1.place(x=225, y=55)

plus1 = Button(text="+", width=3,
              command=lambda: text_second_num.insert(END,"+"))
plus1.place(x=260, y=55)



root.resizable(width=False, height=False)

root.mainloop()
