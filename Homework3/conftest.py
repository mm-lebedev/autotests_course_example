import datetime
import pytest


@pytest.fixture(scope="class")
def test_start():  # Печать времени
    """
    Фикстура выводит время до начала тест
    и после окончания теста
    :rtype: object
    """
    start = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    print(f"Время начала {start}")
    yield
    after_start = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    print(f"Время окончания теста {after_start}")



@pytest.fixture()
def test_time():  # Время выполнения теста, второе задание, выполняем 1 раз
    """
    Фикстура расчитывает время прохождения теста
    время начала минус время окончания
    :rtype: object
    """
    start = datetime.datetime.now()
    yield
    test_end = datetime.datetime.now()
    summ_time = test_end - start
    print(f"Время выполнения теста {summ_time}")
