# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open('Second_file.txt') as my_second_file:
    lines = 0
    for line in my_second_file:
        lines += 1
        flag = 0
        words = 0
        for letter in line:
            if letter != ' ' and flag == 0:
                words += 1
                flag = 1
            elif letter == ' ':
                flag = 0
        print(f'{lines}', ')', 'символов - ', len(line), ',  слов - ', words)

    print('Всего', lines, 'строки')
