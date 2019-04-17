__author__ = 'kamran'


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from locators import form_locators


class FileUpload(object):

    def __init__(self, driver):
        self.driver = driver

    def get_file_upload_text(self):
        file_upload_list = WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.upload_files_text))
        )
        return file_upload_list

    def upload_pdf_or_image(self):
        file_upload_frame = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.add_files))
        )
        self.driver.switch_to_frame(file_upload_frame)
        click_to_my_drive = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.my_drive))
        )
        click_to_my_drive.click()
        upload_img_pdf = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, form_locators.upload_pdf))
        )
        upload_img_pdf[1].click()
        select_button = self.driver.find_element_by_css_selector(form_locators.select_file)
        select_button.click()

        self.driver.switch_to.default_content()