# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('Third_file.txt', 'r', encoding='utf-8') as workers:
    from statistics import mean
    salaries = []
    for worker in workers:
        last_name, salary = worker.split()
        salary = float(salary)
        if salary < 20000.00:
            print('Оклад менее 20000: ', last_name)
        salaries.append(salary)
    print('Средняя велечина дохода: ', mean(salaries))
