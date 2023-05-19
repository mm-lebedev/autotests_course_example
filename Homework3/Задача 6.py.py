# Глобальные перемены.
# Имеется следующие переменные, определенные в глобальной области видимости модуля:
# number = 1
# string = 'Hello'
# Напишите и вызовите функцию, которая будет изменять и возвращать эти переменные, на следующие значения:
# number = 5
# string = 'Hello, dear friend'
#

number = 1
string = 'Hello'


def global_changes():
    """
    Данная функция изменяет глобальную переменную,
    возвращает функцию заданные значение переменных
    :return:
    """

    # Здесь нужно написать код
    global number, string
    number = 5
    string = 'Hello, dear friend'
    return number, string


global_changes()


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
assert number == 5, 'Переменная number должна иметь значение 5'
assert string == 'Hello, dear friend', 'Переменная number должна иметь значение Home, sweet home'
assert global_changes() == (5, 'Hello, dear friend')

print('Все ок')


# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    msg = 1

    def local_function():
        """
        Данная функция изменяет объемлющую переменную,
        возвращает новые значения в глобальную функцию
        """
        nonlocal msg
        msg = 2
    local_function()  # Необязательно вызывать локальную, т.к assert не проверяет т ничего кроме возвращения в функцию
    return msg


global_function()  # Необязательно вызывать глобальну т.к assert не проверяет т ничего кроме возвращения в функцию


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
