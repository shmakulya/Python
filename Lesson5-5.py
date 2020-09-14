# 5) Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

with open('Fifth_file.txt', 'w+') as my_fifth_file:
    line = input('Введите цифры через пробел \n')
    my_fifth_file.write(line)
    numbers = line.split()
    print(sum(map(int, numbers)))


