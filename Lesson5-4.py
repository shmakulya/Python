# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

with open('Fourth_file.txt', 'r', encoding='utf-8') as my_fourth_file:
    translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    numbers = []
    for i in my_fourth_file:
        i = i.split(' ', 1)
        numbers.append(translate[i[0]] + ' ' + i[1])
    print(numbers)
    with open('Fourth_file_new.txt', 'w', encoding='utf-8') as my_fourth_file_new:
        my_fourth_file_new.writelines(numbers)

