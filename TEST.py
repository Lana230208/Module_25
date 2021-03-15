import pytest
from selenium.webdriver.chrome import webdriver


def test_show_my_pets(driver):
    # driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('http://petfriends1.herokuapp.com/login')
    # Вводим email
    driver.find_element_by_id('email').send_keys('office@jakera.com.ua')
    # Вводим пароль
    driver.find_element_by_id('pass').send_keys('ASDfg230208')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element_by_tag_name('h1').text == "PetFriends"



