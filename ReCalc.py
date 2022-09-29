import tkinter as tk

def add_digit(digit):
    value = calc.get()#принимает значение, которое хранится в вводе
    if value[0] == '0' and len(value) == 1:#если 1-ое значение - 0 И длина значения = 1
        value = value[1:]#то этот 0 убирается
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':#если последнее значение является операцией, то эту операцию должны убрать из value, т.е. все что там лежит КРОМЕ последней операции
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:#НО если или + или - или / или * уже есть в предыдущем выражении
        calculate()#то оно уже считывается
        value = calc.get()#и вновь получаем новое значение
    calc.delete(0, tk.END)#всё что было - очищаем
    calc.insert(0, value + operation)#к значению прибавляем новую операцию

def calculate():#функция содана для кнопки = для вычисления
    value = calc.get()#принимает значение, которое хранится в вводе
    if value[-1] in '+-/*':#если значение заканчивается на какую-то операцию 
        value = value + value[:-1]#то к этому значению "прибавляем" это же значение(пример 7* = 49)
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))#eval - функция для выполнения математических операций

def clear():#функция очищения
    calc.delete(0, tk.END)
    calc.insert(0, 0)

def make_digit_button(digit):#функция создана для кнопок от 1 до 9 и 0
    return tk.Button(text = digit, bd = 5, font = ('Arial', 13), command = lambda : add_digit(digit))

def make_operation_button(operation):#функция создана для кнопок операций
    return tk.Button(text = operation, bd = 5, font = ('Arial', 13), fg = 'red',
                     command = lambda : add_operation(operation))

def make_calc_button(operation):#фунция создана для =
    return tk.Button(text = operation, bd = 5, font = ('Arial', 13), fg = 'red',
                     command = calculate)

def make_clear_button(operation):#функция создана для кнопки очищения
    return tk.Button(text = operation, bd = 5, font = ('Arial', 13), fg = 'red',
                     command = clear)
    

win = tk.Tk()
win.geometry(f"240x270")#размер окна
win['bg'] = '#33ffe6'#цвет фона(бирюзовый)
win.title('Калькулятор')#заголовок приложения

calc = tk.Entry(win, justify = tk.RIGHT, font = ('Arial', 15), width = 15)#создание поля ввода; создана функция justify для ввода чисел и знаков справа, указан шрифт и её размер
calc.insert(0, '0')#при запуске приложения и при очищении поля ввода будет отображаться 0 в виде строки 
calc.grid(row = 0, column = 0, columnspan = 4, stick = 'we', padx = 5)#расположение поля ввода(его ряд и колонка), объединение колонок, растягивание слева направо и расстояние по x

#кнопки от 1 до 9 и 0; для каждой кнопки указан текст, ряд, колонка, расширение и расстояние между ними
make_digit_button('1').grid(row = 1, column = 0, stick = 'wens', padx =5, pady = 5)
make_digit_button('2').grid(row = 1, column = 1, stick = 'wens', padx =5, pady = 5)
make_digit_button('3').grid(row = 1, column = 2, stick = 'wens', padx =5, pady = 5)
make_digit_button('4').grid(row = 2, column = 0, stick = 'wens', padx =5, pady = 5)
make_digit_button('5').grid(row = 2, column = 1, stick = 'wens', padx =5, pady = 5)
make_digit_button('6').grid(row = 2, column = 2, stick = 'wens', padx =5, pady = 5)
make_digit_button('7').grid(row = 3, column = 0, stick = 'wens', padx =5, pady = 5)
make_digit_button('8').grid(row = 3, column = 1, stick = 'wens', padx =5, pady = 5)
make_digit_button('9').grid(row = 3, column = 2, stick = 'wens', padx =5, pady = 5)
make_digit_button('0').grid(row = 4, column = 0, stick = 'wens', padx =5, pady = 5)

#кнопки операций +-/*; для каждой кнопки указан текст, ряд, колонка, расширение и расстояние между ними
make_operation_button('+').grid(row = 1, column = 3, stick = 'wens', padx = 5, pady = 5)
make_operation_button('-').grid(row = 2, column = 3, stick = 'wens', padx = 5, pady = 5)
make_operation_button('/').grid(row = 3, column = 3, stick = 'wens', padx = 5, pady = 5)
make_operation_button('*').grid(row = 4, column = 3, stick = 'wens', padx = 5, pady = 5)

#кнопка вычисления =; для этой кнопки указан текст, ряд, колонка, расширение и расстояние между ними
make_calc_button('=').grid(row = 4, column = 2, stick = 'wens', padx = 5, pady = 5)

#кнопка очищения поля ввода; для этой кнопки указан текст, ряд, колонка, расширение и расстояние между ними
make_clear_button('C').grid(row = 4, column = 1, stick = 'wens', padx = 5, pady = 5)

#колонки будут занимать больше пространства по высоте и по длине
win.grid_columnconfigure(0, minsize = 60)
win.grid_columnconfigure(1, minsize = 60)
win.grid_columnconfigure(2, minsize = 60)
win.grid_columnconfigure(3, minsize = 60)

#ряды будут занимать больше пространства по высоте и по длине
win.grid_rowconfigure(1, minsize = 60)
win.grid_rowconfigure(2, minsize = 60)
win.grid_rowconfigure(3, minsize = 60)
win.grid_rowconfigure(4, minsize = 60)

win.mainloop()
