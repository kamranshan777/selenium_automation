
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import form_locators

class Validation(object):

    def __init__(self, driver):
        self.driver = driver

    def check_validation(self):
        click_to_next = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.next_button))
        )
        click_to_next.click()

    def required_questions(self):
        required_mcq = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="alert"]'))
        )
        return required_mcq[0]





