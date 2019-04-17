__author__ = 'kamran'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from locators import form_locators


class Dropdown(object):

    def __init__(self, driver):
        self.driver = driver

    def dropdown_cap_selector(self):
        capitals_hading = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, form_locators.capitals_mcqs))
        )
        return capitals_hading

    def click_capital_pun_drop(self):
        cap_pun = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, form_locators.cap_pun_selector))
        )
        cap_pun.click()

    def click_capital_pak_drop(self):
        cap_pak = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, form_locators.cap_pak_selector))
        )
        cap_pak.click()

    def select_drop_values(self, capital):
        d_click = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, form_locators.capitals_ans.format(capital)))

        )
        d_click.click()

        # WebDriverWait(self.driver, 10).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR,  'input[value="{}"]'.format(capital)))
        # )
        # WebDriverWait(self.driver, 10).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR,  'div.exportSelectPopup .quantumWizMenuPaperselectOption.isSelected[data-value="{}"]'.format(capital)))
        # )
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[role="listbox"][aria-expanded="true"]'))
        )