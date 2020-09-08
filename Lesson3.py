# # 1. + Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# # у пользователя, предусмотреть обработку ситуации деления на ноль.
#
# # 1 вариант без функции
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
if second == 0:
    try:
        first / second
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
else:
    print(first / second)

# # 2 вариант с функцией
def division(first, second):
    try:
        first, second = float(first), float(second)
        div = first / second
    except ZeroDivisionError:
        return 'Делить на ноль нельзя'
    return div

print(division(7, 5.5))

# # 2. + Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# # год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# # Реализовать вывод данных о пользователе одной строкой.
#
# # # Вариант 1
def my_func(name, surname, birth_year, city, e_mail, phone_number):
    print(name, surname, birth_year, city, e_mail, phone_number)
my_func('Ivan', 'Ivanov', '1990', 'Moscow', 'nnn@ya.ru', '89999999999')
#
# # # Вариант 2
def my_func_2( **kwargs):
    print(kwargs)
my_func_2(name='Ivan', surname='Ivanov', birth_year=1990, city='Moscow', e_mail='nnn@ya.ru', phone_number=89999999999)

#
# # 3. + Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# # двух аргументов.
#
# # Вариант 1
def my_sum(*args):
    return args


print(sum(my_sum(5, 1, 7)) - min(my_sum(5, 1, 7)))

# # Вариант 2
numbers = []
for a in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)
print(sum(numbers) - min(numbers))

# # # Вариант 3
def my_sum(numb):
    print(sum(numb) - min(numb))


my_sum([5, 1, 7])
#
#
# # 4. + Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# # возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# # необходимо обойтись без встроенной функции возведения числа в степень.
# # Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй
# # — более сложная реализация без оператора **, предусматривающая использование цикла.

# Вариант 1
def my_func(x, y):
    return x ** y


print(my_func(7, abs(-2)))

# Вариант 2
def my_func(x=7, y=-2):
    return pow(x, abs(y))


print(my_func())

# Вариант 3
print(pow(7, abs(-2)))

# Вариант 4
def my_pow_func(x, y):
    # y - целое отрицательное
    try:
        x, y = float(x), int(y)
        res = x
        for i in range(abs(y) - 1):
            res *= x
        return 1 / res
    except ValueError:
        return 'Check value'

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def summary():
    ex = False
    result = 0
    while ex == False:
        numbers = input('Enter numbers or q to exit: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res_line += int(num)
        result += res_line
    print(result)

print(summary())

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    return word.title()


print(int_func('hello'))

new_int_func = int_func('around big world')
print(new_int_func)
