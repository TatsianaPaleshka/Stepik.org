from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"  # old page
    link = "http://suninjuly.github.io/registration2.html"  # new page
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    input_first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class .form-control.first')
    input_first_name.send_keys("Ivan")  # First name*
    input_last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.second_class .form-control.second')
    input_last_name.send_keys("Petrov")  # Last name*
    input_email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class .form-control.third')
    input_email.send_keys("Smolensk@mail.ru")  # Email*

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
