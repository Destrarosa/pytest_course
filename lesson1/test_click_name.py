from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
def test_click_name():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.CSS_SELECTOR,"a[id='item_4_title_link' ]>div[class='inventory_item_name']").text

    text = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link' ]>div[class='inventory_item_name']")
    text.click()

    time.sleep(4)

    text_after = driver.find_element(By.CSS_SELECTOR, "#inventory_item_container > div > div > div.inventory_details_desc_container > div.inventory_details_name.large_size").text
    time.sleep(3)
    assert (text_before == text_after)

