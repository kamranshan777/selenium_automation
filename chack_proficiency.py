from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import form_locators
import time


class Proficiency(object):

    def __init__(self, driver):
        self.driver = driver

    def get_proficiency_text(self):
        chack_box_gride = WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.chack_box_gride_selc))
        )
        return chack_box_gride

    def set_proficiency_check_lang(self, lang):
            reading = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.reading_selector.format(lang)))
            )
            reading.click()

            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Reading, response for {}"]'
                                                                     '[aria-checked="false"]'.format(lang)))
            )
            listing = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.listing_selector.format(lang)))
            )
            listing.click()


    # def proficiency_check_french(self, fre):
    #         listing = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.listing_selector.format(fre)))
    #         )
    #         listing.click()
    #
    # def proficiency_check_urdu(self, urdu):
    #         reading = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.reading_selector.format(urdu)))
    #         )
    #         reading.click()
    #         writing = self.driver.find_element_by_css_selector(
    #             form_locators.writing_selector.format(urdu))
    #         writing.click()
    #         listing = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, form_locators.listing_selector.format(urdu)))
    #         )
    #         listing.click()