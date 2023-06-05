# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
with open("test_file/task1_data.txt", mode="r", encoding="utf-8") as f:
    k = f.read()
summ = ""
for x in k:
    if not x.isdigit():
        summ += x
print(summ)
with open("test_file/task1_answer.txt", mode="w", encoding="utf-8") as f:
    f.write(summ)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')



# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# # func2()
# # func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime

# Здесь пишем код

def func_log(file_log='log.txt'):
    def func1(func):
        def wrapper(*args, **kwargs):
            with open(file_log, "a", encoding="utf-8") as f:
                f.write(f"{func1.__name__} вызвана {datetime.datetime.now().strftime('%d.%m %H:%M:%S')}\n")
            return func
        return wrapper
    return func1

def func_log2(file_log='func2.txt'):
    def func2(func):
        def wrapper(*args, **kwargs):
            with open(file_log, "a", encoding="utf-8") as f:
                f.write(f"{func2.__name__} вызвана {datetime.datetime.now().strftime('%d.%m %H:%M:%S')}\n")
            return func
        return wrapper
    return func2

@func_log(file_log='log.txt')
def func1():
    print("Расширяем функцию, на запись не влияет")

@func_log2(file_log='func2.txt')
def func2():
    print("Расширяем функцию, на запись не влияет")

func1()
func2()
func1()



# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt") as f:
    summ = 0
    summ1 = []  # сюда поместим список и потом воспользуемся sorted, reverse=True
    for x in f:
        try:
            summ += int(x)
        except ValueError:
            if summ != 0:
                summ1.append(summ)
                summ = 0
    summ1 = sorted(summ1, reverse=True)
    three_most_expensive_purchases = sum(summ1[:3])
print(three_most_expensive_purchases)



assert three_most_expensive_purchases == 202346


