__author__ = 'kamran'

import unittest
from selenium import webdriver
from visit_form import OpenForm
from sign_in_page import LoginForm
from validation import Validation
from basic_info import BasicInfo
from next_button import NextButton
from page_title import Title
from multi_type_mcqs import MultipleMcq
from check_boxes import Checkboxes
from drop_down import Dropdown
from file_uplod import FileUpload
from student_assessment import StudentAssessment
from multiple_choice_grid import MultipleChoiceGrid
from chack_proficiency import Proficiency
from current_date_time import DateAndTime
from correct_answers import CorrectAnswer
from const import const_keyword
from answers import DICT
from locators import form_locators
from write_correct_ans_csv import creat_csv
from read_correct_ans_csv import read_csv
# from run_test_cases import SubmitResponse
import csv
import os
from pathlib import Path


class form_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.form_signIn = OpenForm(self.driver)
        self.form_signIn.visit()
        self.credential = LoginForm(self.driver)
        self.basicInfo = BasicInfo(self.driver)
        self.next = NextButton(self.driver)
        self.page_title = Title(self.driver)
        self.multiple_type_ques = MultipleMcq(self.driver)
        self.chackbox = Checkboxes(self.driver)
        self.drop_d = Dropdown(self.driver)
        self.upload_file = FileUpload(self.driver)
        self.obj_stu_assessment = StudentAssessment(self.driver)
        self.obj_stu_grid = MultipleChoiceGrid(self.driver)
        self.proficiency_language = Proficiency(self.driver)
        self.currentDateTime = DateAndTime(self.driver)
        self.correctAns = CorrectAnswer(self.driver)

    def upload_pdf(self):
        files_upload = self.upload_file.get_file_upload_text()
        for file_text in files_upload:
            file_text.click()
            self.upload_file.upload_pdf_or_image()
        self.next.next_page()

    def scale_assement(self):
        scale = self.obj_stu_assessment.scale_text()
        value = DICT.pages_ans.get(scale.text)
        self.obj_stu_assessment.assignment_scale_rating(value[3])
        self.next.next_page()

    def choice_grid(self):
        gride_rating = self.obj_stu_grid.choice_gride_selector()
        if gride_rating.text == 'How satisfied are you with the following? *':
            get_gride_text = self.obj_stu_grid.get_multiple_grid_text()
            for grideText in get_gride_text:
                self.obj_stu_grid.set_multiple_gride(grideText)
        self.next.next_page()

    def chack_box_grid(self):
        proficiency_text = self.proficiency_language.get_proficiency_text()
        for proficiencyText in proficiency_text:
            value = DICT.pages_ans.get(proficiencyText.text)
            if proficiencyText.text == value[0]:
                self.proficiency_language.set_proficiency_check_lang(value[0])
        self.next.next_page()

    def date_time(self):
        self.currentDateTime.current_date()
        self.currentDateTime.current_time()
        self.currentDateTime.submit_form()
        self.correctAns.click_to_view_button()

    def test_signIn(self):
        #login form and submit basic infomation
        self.credential.click_login_inputs()
        self.credential.submit_login_data(const_keyword.loninEmail, const_keyword.loginPassword)
        self.basicInfo.fill_basic_info()
        self.next.next_page()
        # page_title = self.page_title.page_title_locator()

        #Selecting multiple type ans
        assert "Multiple type Questions" in self.driver.page_source
        # assert page_title == "Multiple type Questions"
        mcq_questions = self.multiple_type_ques.multi_choice_mcq()
        for question in mcq_questions:
            value = DICT.pages_ans.get(question.text)
            self.multiple_type_ques.click_to_multi_ans(value[1])
        self.next.next_page()


        #Select multiple chack boxes
        assert "Checkboxes" in self.driver.page_source
        checkboxes_q = self.chackbox.check_box_selector()
        for checkBox in checkboxes_q:
            value = DICT.pages_ans.get(checkBox.text)
            if checkBox.text == "Select the two numbers that are not prime. *":
                self.chackbox.click_to_prime_num(value[0], value[3])
            elif checkBox.text == 'Select the correct answers *':
                self.chackbox.click_to_prime_num(value[0], value[3], value[2])
        self.next.next_page()

        #Selec capital of punjab or capital of pakistan
        assert "Dropdown" in self.driver.page_source
        capitals_q = self.drop_d.dropdown_cap_selector()
        for cap in capitals_q:
            value = DICT.pages_ans.get(cap.text)
            if cap.text == 'Capital of Punjab *':
                self.drop_d.click_capital_pun_drop()
                self.drop_d.select_drop_values(value[1])
            elif cap.text == 'Capital of Pakistan *':
                self.drop_d.click_capital_pak_drop()
                self.drop_d.select_drop_values(value[1])
        self.next.next_page()

        #upload PDF or image file
        assert "File Uploading" in self.driver.page_source
        self.upload_pdf()

        #select scale assesment regarding how hard this assignment
        assert "Scale" in self.driver.page_source
        self.scale_assement()

        #Give feedback related to Assignments, Example scripts, Training
        assert "Multiple Choice grid" in self.driver.page_source
        self.choice_grid()

        #proficiency check in diffrent languages
        assert "Checkbox Grid" in self.driver.page_source
        self.chack_box_grid()

        #Enter date and time
        assert "Enter Current time" in self.driver.page_source
        self.date_time()

        assert "Automation Assessment" in self.driver.page_source
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        mydict = self.correctAns.select_final_correct_ans()
        creat_csv(mydict)
        self.driver.switch_to_window(window_before)

################### Second time ######################
        self.driver.find_element_by_css_selector('div.freebirdFormviewerViewResponseLinksContainer a:nth-child(3)').click()
        assert "Automation Assessment" in self.driver.page_source
        self.basicInfo.fill_basic_info()
        self.next.next_page()

        csv_path = Path("D:/redesign_assignmen_2/csv_file_kamran.csv")
        if csv_path.is_file():
            checkboxes_q = self.chackbox.check_box_selector()
            for checkBox in checkboxes_q:
                value = DICT.pages_ans.get(checkBox.text)
                for correct_ans in read_csv()[2]:
                    if value[0] == correct_ans:
                        self.multiple_type_ques.click_to_multi_ans(value[0])

        self.next.next_page()

        assert "Checkboxes" in self.driver.page_source
        checkboxes_q = self.chackbox.check_box_selector()
        for checkBox in checkboxes_q:
            value = DICT.pages_ans.get(checkBox.text)
            if checkBox.text == "Select the two numbers that are not prime. *":
                self.chackbox.click_to_prime_num(value[0], value[3])
            elif checkBox.text == 'Select the correct answers *':
                self.chackbox.click_to_prime_num(value[0], value[3], value[2])
        self.next.next_page()
        
        # assert "Checkboxes" in self.driver.page_source
        # checkboxes_q = self.chackbox.check_box_selector()
        # for checkBox in checkboxes_q:
        #     value = DICT.pages_ans.get(checkBox.text)
        #     if checkBox.text == "Select the two numbers that are not prime. *":
        #         number_2 = read_csv()[2][2]
        #         for correct_ans in number_2:
        #             if value[1] == correct_ans[0] and value[3] == correct_ans[1]:
        #                 self.chackbox.click_to_prime_num(correct_ans[0], correct_ans[1])
        #     elif checkBox.text == 'Select the correct answers *':
        #         number_3 = read_csv()[2][2]
        #         for correct_ans in number_3:
        #             if value[1] == correct_ans[0] and value[3] == correct_ans[1] and value[2] == correct_ans[2]:
        #                 self.chackbox.click_to_prime_num(correct_ans[0], correct_ans[1], correct_ans[2])
        self.next.next_page()

      # Selec capital of punjab or capital of pakistan
        assert "Dropdown" in self.driver.page_source
        capitals_q = self.drop_d.dropdown_cap_selector()
        csv_path = Path("D:/redesign_assignmen_2/csv_file_kamran.csv")
        for cap in capitals_q:
            value = DICT.pages_ans.get(cap.text)
            if cap.text == 'Capital of Punjab *':
                if csv_path.is_file():
                    for correct_ans in read_csv()[2]:
                        if value[0] == correct_ans:
                            self.drop_d.click_capital_pun_drop()
                            self.drop_d.select_drop_values(correct_ans)
                            break
            elif cap.text == 'Capital of Pakistan *':
                if csv_path.is_file():
                    for correct_ans in read_csv()[2]:
                        if value[0] == correct_ans:
                            self.drop_d.click_capital_pak_drop()
                            self.drop_d.select_drop_values(correct_ans)
                            break
        self.next.next_page()

       #upload PDF or image file
        assert "File Uploading" in self.driver.page_source
        self.upload_pdf()

        #select scale assesment regarding how hard this assignment
        assert "Scale" in self.driver.page_source
        self.scale_assement()

        #Give feedback related to Assignments, Example scripts, Training
        assert "Multiple Choice grid" in self.driver.page_source
        self.choice_grid()

        #proficiency check in diffrent languages
        assert "Checkbox Grid" in self.driver.page_source
        self.chack_box_grid()


        #Enter date and time
        assert "Enter Current time" in self.driver.page_source
        self.date_time()

        self.correctAns.click_to_view_button()
        os.remove('csv_file_kamran.csv')
        self.driver.quit()