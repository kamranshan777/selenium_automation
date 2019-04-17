__author__ = 'kamran'

from locators import form_locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class LoginForm(object):
    def __init__(self, driver):
        self.driver = driver

    def click_login_inputs(self):
        click_to_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.click_sign_button))
        )
        click_to_input.click()

    def submit_login_data(self, email, pwd):
        email_address = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.email_locator))
        )
        email_address.send_keys(email, Keys.RETURN)

        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, form_locators.password_locator))
        )
        password.send_keys(pwd, Keys.RETURN)

