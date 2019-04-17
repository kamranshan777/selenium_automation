__author__ = 'kamran'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from locators import form_locators


class MultipleChoiceGrid(object):

    def __init__(self, driver):
        self.driver = driver

    def choice_gride_selector(self):
        scale_hading = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.scale))
        )
        return scale_hading

    def get_multiple_grid_text(self):
        multiple_choice_text = WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.get_gride_text))
        )
        return multiple_choice_text

    def set_multiple_gride(self, grid_text):
        grid = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[aria-label="{}"] div.freebirdFormviewerViewItemsGridCell'
                                                   .format(grid_text.text)))
        )
        # self.driver.find_elements_by_css_selector('div[aria-label="{}"] label'.format(grid_text.text))
        grid[-1].click()
        # time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="{}"] label '
                                                    'div[data-value="5"][aria-checked="false"]'.format(grid_text.text)))
        )
