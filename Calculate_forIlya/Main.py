# Данная программа вычисляет сумму, разность и корни
# в десятичной системе счисления
# Щерица Илья, ИУ7-25

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
from math import sqrt


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
def is_float(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

# Сложение
def mathmatic_plus(entry1, entry2, text):
    global vidget
    global result
    num1 = entry1.get()
    num2 = entry2.get()

    if not is_float(num1) or  not is_float(num2):
        messagebox.showerror('Ошибка!', 'Проверьте правильность введённых данных!')
    else:
        result = float(num1) + float(num2)
        text_result = str(result)
        text.destroy()
        text = Label(width=width, height=height, bg=color, text=text_result)
        text.place(x=x_entry, y=y_entry)

# Вычитание
def mathmatic_minus(entry1, entry2, text):
    global vidget
    global vidget2
    global result
    num1 = entry1.get()
    num2 = entry2.get()

    if not is_float(num1) or not is_float(num2):
        messagebox.showerror('Ошибка!', 'Проверьте правильность введённых данных!')
    else:

        result = float(num1) - float(num2)
        text_result = str(result)
        text.destroy()
        text = Label(width=width, height=height, bg=color, text=text_result)
        text.place(x=x_entry, y=y_entry)

# Извлечение корня
def mathmatic_sqrt(entry, text):
    global vidget
    global vidget2
    global result
    num = entry.get()

    if not is_float(num):
        messagebox.showerror('Ошибка!', 'Проверьте правильность введённых данных!')
    else:

        result = sqrt(float(num))
        text_result = str(result)
        text.destroy()
        text = Label(width=width, height=height, bg=color, text=text_result)
        text.place(x=x_entry, y=y_entry)

# Вывод информации
def info():
    text0 = 'Информация'
    text1 = '''Программа для выполнения арифметических действий в троичной симметричной 
системе. \n\n
Щерица Илья, ИУ7-25'''
    messagebox.showinfo(text0, text1)

x_entry = 370
y_entry = y_vidget = 15
x_vidget = 140
width = 15
height = 1
color = 'white'

root = Tk()
root.title('Калькулятор')
root.geometry('500x200')


drop_menu = Menu(root)
root.config(menu=drop_menu)

first_drop = Menu(drop_menu)
drop_menu.add_cascade(label='Чистка окон', menu=first_drop)
first_drop.add_command(label='Очистить все окна',
                       command=lambda: deletion_all(text_first_num, text_second_num, text_result))
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
                        command=lambda: mathmatic_plus(text_first_num, text_second_num, text_result))
second_drop.add_command(label='Вычесть',
                        command=lambda: mathmatic_minus(text_first_num, text_second_num, text_result))

third_drop = Menu(drop_menu)
drop_menu.add_cascade(label='Инфо', menu=third_drop)
third_drop.add_command(label='О программе', command=lambda: info())

btn_plus = Button(text='Сложить', width=10,
                  command=lambda: mathmatic_plus(text_first_num, text_second_num, text_result))
btn_plus.place(x=50, y=70)

btn_minus = Button(text='Вычесть', width=10,
                   command=lambda: mathmatic_minus(text_first_num, text_second_num, text_result))
btn_minus.place(x=140, y=70)

btn_sqrt1 = Button(text = 'Корень из 1-го числа', width=17,
                   command=lambda: mathmatic_sqrt(text_first_num, text_result))
btn_sqrt1.place(x=230, y=70)

btn_sqrt2 = Button(text = 'Корень из 2-го числа', width=17,
                   command=lambda: mathmatic_sqrt(text_second_num, text_result))
btn_sqrt2.place(x=365, y=70)



text_first_num = Entry(width=width)
text_first_num.place(x=10, y=y_entry)

text_second_num = Entry(width=width)
text_second_num.place(x=190, y=y_entry)

lbl_equal = Label(text='=')
lbl_equal.place(x=325, y=y_entry)

text_result = Label(width=width, height=height, bg=color)
text_result.place(x=x_entry, y=y_entry)

zero = Button(text="0", width=3,
             command = lambda: text_first_num.insert(END, "0"))
one = Button(text="1", width=3,
             command = lambda: text_first_num.insert(END, "1"))
two = Button(text="2", width=3,
             command = lambda: text_first_num.insert(END, "2"))
three = Button(text="3", width=3,
             command = lambda: text_first_num.insert(END, "3"))
four = Button(text="4", width=3,
             command = lambda: text_first_num.insert(END, "4"))
five = Button(text="5", width=3,
             command = lambda: text_first_num.insert(END, "5"))
six = Button(text="6", width=3,
             command = lambda: text_first_num.insert(END, "6"))
seven = Button(text="7", width=3,
             command = lambda: text_first_num.insert(END, "7"))
eight = Button(text="8", width=3,
             command = lambda: text_first_num.insert(END, "8"))
nine = Button(text="9", width=3,
             command = lambda: text_first_num.insert(END, "9"))


root.resizable(width=False, height=False)

root.mainloop()
