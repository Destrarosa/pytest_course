from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

def test_checkout():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    button = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button.click()

    time.sleep(4)

    card = driver.find_element(By.CSS_SELECTOR, "a[class=shopping_cart_link]")
    card.click()

    # time.sleep(4)
    #
    # button_remove = driver.find_element(By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-backpack"]')
    # button_remove.click()
    # time.sleep(4)

    time.sleep(3)
    button_checkout = (driver.find_element(By.CSS_SELECTOR, 'button[data-test="checkout"]'))
    button_checkout.click()

    time.sleep(2)
    name_field = driver.find_element(By.CSS_SELECTOR, 'input[data-test="firstName"]')
    name_field.send_keys("standard_user")
    time.sleep(2)

    lastname_field = driver.find_element(By.CSS_SELECTOR,'input[data-test="lastName"]')
    lastname_field.send_keys("Smith")
    time.sleep(2)

    code_field = driver.find_element(By.CSS_SELECTOR, 'input[data-test="postalCode"]')
    code_field.send_keys("248000")
    time.sleep(3)

    button_continue = driver.find_element(By.CSS_SELECTOR, 'input[data-test="continue"]')
    button_continue.click()
    time.sleep(3)

    button_finish = driver.find_element(By.CSS_SELECTOR, "button[data-test='finish']")
    button_finish.click()
