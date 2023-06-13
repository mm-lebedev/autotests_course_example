# Перейти на https://sbis.ru/  +
# Перейти в раздел "Контакты"  +
# Найти баннер Тензор, кликнуть по нему  +
# Перейти на https://tensor.ru/  +
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By


sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()  # Задаем переменную для драйвера

try:
    print('Переходим на сайт')
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, "Сайт не совпадает"

    print('Перейти в раздел "Контакты"')
    one_element = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    one_element.click()

    print('Найти баннер Тензор, кликнуть по нему')
    tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    tensor.click()

    print('Перейти на https://tensor.ru/')
    driver.switch_to.window(driver.window_handles[1])
    assert 'https://tensor.ru/' in driver.current_url, "Неверный сайт"

    print('Проверить, что есть блок новости "Сила в людях"')
    news = driver.find_element(By.CSS_SELECTOR,
                                ".tensor_ru-Index__block4-content "
                                "[class='tensor_ru-Index__card-title tensor_ru-pb-16']")
    assert news.text == "Сила в людях"

    print('Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about')
    podrobnee = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    podrobnee.location_once_scrolled_into_view
    podrobnee.click()
    assert "https://tensor.ru/about" in driver.current_url, "Неверный сайт"
    print("Автотест Завершен")

finally:
    driver.quit()


# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep
import datetime

sbis_site = 'https://fix-online.sbis.ru/'
title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
driver = webdriver.Chrome()  # Задаем переменную для драйвера
time = f"Тестовое сообщение на появление в реестре {datetime.datetime.now().strftime('%d.%m %H:%M:%S')}"
try:
    print("Авторизоваться на сайте https://fix-online.sbis.ru/")
    driver.get(sbis_site)
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys("Rush", Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys("Rush123", Keys.ENTER)
    sleep(8)

    print("Перейти в реестр Контакты")
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-name="contacts"]')
    action = ActionChains(driver)
    action.click(contacts)
    action.perform()
    sleep(3)

    print("Отправить сообщение самому себе")
    messenge = driver.find_element(By.CSS_SELECTOR, '.icon-EmptyMessage')
    messenge.click()
    sleep(2)
    poisk = driver.find_element(By.CSS_SELECTOR, ".controls-Field")
    poisk.send_keys("Семён Иванов Тест")
    sleep(1)
    fio = driver.find_element(By.CSS_SELECTOR, '.ws-inline-flexbox [title="Семён Иванов"]')
    fio.click()
    sleep(2)
    messenge_kart = driver.find_element(By.CSS_SELECTOR, ".textEditor_Viewer__Paragraph")
    messenge_kart.send_keys(time, Keys.ALT + Keys.ENTER)
    sleep(3)

    print("Убедиться, что сообщение появилось в реестре")
    reestr = driver.find_element(By.CSS_SELECTOR, ".richEditor_richContentRender_fontSize-m_theme-default")
    assert reestr.text == time, "Уведомление не найдено в ленте"
    action.move_to_element(reestr)
    action.perform()

    print("Удалить это сообщение и убедиться, что удалили")
    messenge_del = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    messenge_del.click()
    reestr2 = driver.find_element(By.CSS_SELECTOR, ".richEditor_richContentRender_fontSize-m_theme-default")
    assert reestr2.text != time, "Уведомление найдено в ленте"
    print("Автотест Завершен")

finally:
    driver.quit()
