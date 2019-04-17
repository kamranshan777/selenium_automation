__author__ = 'kamran'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import form_locators
import time


class StudentAssessment(object):

    def __init__(self, driver):
        self.driver = driver

    def scale_text(self):
        scale_hading = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.scale))
        )
        return scale_hading

    def assignment_scale_rating(self, scale):
        assessment = WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.scale_assisment))
        )

        assessment[int(scale)].click()
