__author__ = 'kamran'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import form_locators


class Checkboxes(object):

    def __init__(self, driver):
        self.driver = driver

    def check_box_selector(self):
        select_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.chack_box_qutz))
        )
        return select_box

    def click_to_prime_num (self, num1, num2, num3=False):
        num1_select = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.chack_box_ans.format(num1)))
            # EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.chack_box_ans.format(equal_num)))
        )
        num1_select.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="31"][aria-checked="true"] '))
        )
        num2_selected = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.chack_box_ans.format(num2)))
        )
        num2_selected.click()

        if num3:
            num3_selected = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.chack_box_ans.format(num3)))
            )
            num3_selected.click()



