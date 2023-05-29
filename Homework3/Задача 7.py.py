# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

# Здесь пишем код
class Segment:
    def __init__(self, otrezok1, otrezok2):
        """
        Функция (в классе) рассчитывает длину отрезка,
        возвращает длину отрезка,
        возвращает булево значение для оси абсцисс и ординат
        :param otrezok1:
        :param otrezok2:
        """
        self.otrezok1 = otrezok1
        self.otrezok2 = otrezok2


    def length(self):
        x1, y1 = self.otrezok1
        x2, y2 = self.otrezok2
        return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


    def x_axis_intersection(self):
        x1, y1 = self.otrezok1
        x2, y2 = self.otrezok2
        if y1 == 0 or y2 == 0:
            return True
        elif (y1 > 0 and y2 < 0) or (y1 < 0 and y2 > 0):
            return True
        else:
            return False


    def y_axis_intersection(self):
        x1, y1 = self.otrezok1
        x2, y2 = self.otrezok2
        if x1 == 0 or x2 == 0:
            return True
        if (x1 > 0 and x2 < 0) or (x1 < 0 and x2 > 0):
            return True
        else:
            return False



# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')


# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. shortname, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
class PersonInfo:
    def __init__(self, name, age, *podrazdelenie):
        """
        Экземпляр класса работает с аргументами
        имени --> возраста --> места трудоустройства сотрудников
        Методы форматируют ФИО
        Возврщают подразделения в формате подразделение --> подразделение
        Индексируют ЗП на основании повторящихся букв в подразделении
        :param name:
        :param age:
        :param podrazdelenie:
        """
        self.name = name  # Фамилия - short_name
        self.age = age  # Число - Возраст сотрудника
        self.podrazdelenie = podrazdelenie  # path_deps это последние строки в задании



    def short_name(self):
        stroka_1 = self.name
        spisok = stroka_1.split()
        spisok.reverse()
        rezultat = f"{spisok[0]} {''.join(spisok[1][0])}."
        return rezultat


    def path_deps(self):
        # deportament = self.podrazdelenie
        # spisok_dportamenta = []
        # for x in deportament:
        #     spisok_dportamenta += x.split()
        #         # rezultat = " --> ".join(spisok_dportamenta)
        return " --> " .join(self.podrazdelenie)


    def new_salary(self):
        pustaya_str = ""
        summ_cifr = {}
        count = 1337
        pustaya_str += "".join(self.podrazdelenie)
        for x in pustaya_str:
            summ_cifr[x] = int(summ_cifr.get(x, 0) + 1)
            sortirovka = sorted(summ_cifr.items(), key=lambda z: z[1], reverse=True)
        vhohdenie = int(sortirovka[0][1] + sortirovka[1][1] + sortirovka[2][1])
        count *= self.age * vhohdenie
        return count



# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')

# I. Напишите класс PublicTransport
# Экземпляр класса создается из следующих атрибутов:
#   1. brand - Марка транспорта
#   2. ЗАЩИЩЕННЫЙ (protected) атрибут engine_power - Мощность двигателя --------> self._engine_power
#   3. year - Год выпуска
#   4. color - Цвет
#   5. max_speed - Максимальная скорость
# У класса должно быть СВОЙСТВО info, которое выводит на печать информацию о:
# марке, цвете, годе выпуска и мощности двигателя
#
# II. Напишите класс Bus унаследованный от PublicTransport
# Дополнительными атрибутами будут:
#   1. passengers - кол-во пассажиров
#   2. ПРИВАТНЫЙ (private) аттрибу park - Парк приписки автобуса
#   3. ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда
# Добавить свойство park, которое будет возвращать значение park
# а при присвоении проверять номер парка, что он в диапазоне от 1000 до 9999
#
# III. Напишите класс Tram унаследованный от PublicTransport
# Дополнительными атрибутами будут:
#   1. ПРИВАТНЫЙ (private) атрибут route - маршрут трамвая
#   2. path - длина маршрута
#   3. ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда
# У класса должно быть СВОЙСТВО how_long, которое вычисляет время прохождения маршрута по формуле max_speed/(4*path)

# Здесь пишем код


class PublicTransport:

    def __init__(self, brand, engine_power, year, color, max_speed):
        """
        Данный экземпляр работает с атрибутами
        Свойство возвращает на печать данные из экземпляра
        :param brand:
        :param engine_power:
        :param year:
        :param color:
        :param max_speed:
        """
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed

    @property
    def info(self):
        return f"{self.brand} {self.color} {self.year} {self._engine_power}"


class Bus(PublicTransport):

    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        """
        Экземпляр наследуюет атрибуты от PublicTransport
        Свойство возвращает парк и проверяемт присваивание
        :param brand:
        :param engine_power:
        :param year:
        :param color:
        :param max_speed:
        :param passengers:
        :param park:
        :param fare:
        """
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self.__park = park
        self._fare = fare

    @property
    def park(self):
        return self.__park

    @park.setter
    def park(self, park):
        assert park >= 1000 and park <= 9999
        self.__park = park


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        """
        Экземпляр наследует атрибуты от PublicTransport
        Свойство возращает время прохождения маршрута
        :param brand:
        :param engine_power:
        :param year:
        :param color:
        :param max_speed:
        :param route:
        :param path:
        :param fare:
        """
        super().__init__(brand, engine_power, year, color, max_speed)
        self.__route = route
        self.path = path
        self._fare = fare

    @property
    def how_long(self):
        return self.max_speed / (4 * self.path)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
transport = PublicTransport('Автомобиль', 500, 2040, 'Фиолетовый', 300)
first_bus = Bus('ЛиАЗ', 210, 2015, 'Зеленый', 100, 70, 1232, 32)
second_bus = Bus('VOLGABUS', 320, 2019, 'Желтый', 110, 39, 1111, 32)
first_tram = Tram('71-931M', 125, 2010, 'Красный', 75, 5, 15, 32)
second_tram = Tram('71-409-1', 240, 2018, 'Белый', 85, 7, 17, 32)

assert isinstance(type(transport).info, property), 'В классе PublicTransport, info - не свойство класса'
assert transport._engine_power, 'В классе PublicTransport, engine_power не защищенный атрибут'
assert first_bus._Bus__park, 'В классе Bus, park не приватный атрибут'
assert second_bus._fare, 'В классе Bus, fare не защищенный атрибут'
assert first_tram._fare, 'В классе Tram, fare не защищенный атрибут'
assert second_tram._Tram__route, 'В классе Tram, route не приватный атрибут'
assert isinstance(type(first_tram).how_long, property), 'В классе Tram, how_long - не свойство класса'
assert first_tram.how_long == 1.25, 'В классе Tram, how_long неверно вычисляется'
assert isinstance(type(second_bus).park, property), 'В классе Bus, park - не свойство класса'
try:
    second_bus.park = 999
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
except AssertionError:
    print('Проверка на правильность диапазона пройдена')
try:
    second_bus.park = 1234
    print('Проверка на правильность диапазона пройдена')
except AssertionError:
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
try:
    second_bus.park = 10000
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
except AssertionError:
    print('Проверка на правильность диапазона пройдена')
print('Всё ок')
