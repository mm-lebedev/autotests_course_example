# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код


def generate_random_name(start, end):
    alfawit = 'qwertyuiopasdfghjklzxcvbnm'
    while start < end:
        # https://docs-python.ru/standart-library/modul-random-python/funktsija-random-choice/
        # https://pythonim.ru/osnovy/randint
        name1 = ''.join(random.choice(alfawit) for x in range(random.randint(start, end)))
        name2 = ''.join(random.choice(alfawit) for x in range(random.randint(start, end)))
        yield f"{name1} {name2}"


gen = generate_random_name(1, 15)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    a, b = arg1
    return a / b

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("a,b,result", [
    pytest.param(0, 0, 0, marks=pytest.mark.skip("Пробный скип parametrize")),
    (10, 2, 5),
    pytest.param(-1, 1, -1, marks=pytest.mark.smoke),
    (-5, -5, 1),
    (-20, 8, -2.5)])
def test1(a, b, result):
    assert all_division(a, b) == result

