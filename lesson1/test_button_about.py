from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
def test_button_about():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger = driver.find_element(By.ID, "react-burger-menu-btn")
    burger.click()
    time.sleep(3)

    button_about = driver.find_element(By.ID, "about_sidebar_link")
    button_about.click()
    time.sleep(4)

    assert driver.current_url == 'https://saucelabs.com/'
    driver.quit()


