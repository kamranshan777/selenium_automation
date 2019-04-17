__author__ = 'kamran'

from locators import form_locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class Title(object):
    def __init__(self, driver):
        self.driver = driver

    def page_title_locator(self):
        page_title_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.pageTitle))

        )
        return page_title_text.text
