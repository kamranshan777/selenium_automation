__author__ = 'kamran'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from locators import form_locators
from personal_Creden import PersonalInfo


class BasicInfo(object):
    def __init__(self, driver):
        self.driver = driver

    def fill_basic_info(self):
        cnic_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.cnic))
        )
        cnic_number.send_keys(PersonalInfo.userCnic)
        self.driver.find_element_by_css_selector(form_locators.email).send_keys(PersonalInfo.userEmail)
        self.driver.find_element_by_css_selector(form_locators.phone).send_keys(PersonalInfo.userPnone)
        self.driver.find_element_by_css_selector(form_locators.name).send_keys(PersonalInfo.userName)


