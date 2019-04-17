__author__ = 'kamran'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from locators import form_locators


class MultipleMcq(object):

    def __init__(self, driver):
        self.driver = driver

    def multi_choice_mcq(self):
        mcq = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.Mcqs))
            # EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.Mcqs))
        )
        return mcq

    def click_to_multi_ans(self, mcq):
        type_of_locator = WebDriverWait(self.driver, 5).until(
            # EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.mcq_1_selector.format(mcq)))
            EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.mcq_1_selector.format(mcq)))
        )
        type_of_locator.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="{}"]'.format(mcq)))
        )

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '[aria-label="{}"][aria-checked="false"]'.format(mcq)))
        )

    # def use_firebug_in_selenium(self, msq):
    #     firebug_in_selenium = WebDriverWait(self.driver, 5).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.mcq_1_selector.format(msq)))
    #     )
    #     firebug_in_selenium.click()

