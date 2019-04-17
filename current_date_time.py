from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from locators import form_locators


class DateAndTime(object):

    def __init__(self, driver):
        self.driver = driver

    def current_date(self):
        # mm = datetime.now().month
        # dd = datetime.now().day
        # yy = datetime.now().year

        date = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.date_drop))
        )
        date.click()
        date_input = self.driver.find_element_by_css_selector(form_locators.input_date)
        # join = dd+mm+yy
        date_input.send_keys('11111995')

    def current_time(self):
    #     hh = datetime.now().strftime("%H")
    #     mnt = datetime.now().strftime("%M")
        hours = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.Hours))
        )
        hours.send_keys('11')
        minute = self.driver.find_element_by_css_selector(form_locators.Minut)
        minute.send_keys('11')

    def submit_form(self):
        submit = self.driver.find_elements_by_css_selector(form_locators.form_submit)
        submit[-2].click()
