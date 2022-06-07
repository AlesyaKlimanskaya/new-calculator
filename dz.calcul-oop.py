#Калькулятор. Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввода данных.
class Calculator:
    def __init__(self, c, a, b):
        self.c = c
        self.a = a
        self.b = b

    def plus(self): return self.a + self.b
    def minus(self): return self.a - self.b
    def umnog(self): return self.a * self.b
    def razdel(self): return self.a / self.b

while True:
    c = input('Введите операцию(+,-,*,/,**,0-exit): ')
    if c not in '+,-,*,/,**,0':
        print('Не верно введена операция!!!')
        continue
    elif c == '0':
        print('Программа завершена')
        break
    try:
        a = float(input('Введите первое число: '))
    except ValueError:
        print('Вы ввели не число!')
        continue
    try:
        b = float(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели не число!')
        continue
  
    c_obj = Calculator(c, a, b)
    if c == '+': print(c_obj.plus())
    if c == '-': print(c_obj.minus())
    if c == '*': print(c_obj.umnog())
    if c == '/':
        try:
            print(c_obj.razdel())
        except ZeroDivisionError:
            print('Деление на 0. Ошибка!!!')
