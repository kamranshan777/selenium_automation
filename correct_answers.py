from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from locators import form_locators


class CorrectAnswer(object):

    def __init__(self, driver):
        self.driver = driver

    def click_to_view_button(self):
        click_to_view_score = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.quantumWizButtonPaperbuttonLabel.exportLabel"))
        )
        click_to_view_score.click()

    def select_final_correct_ans(self):
        # Multiple type Questions
        use_fire_bug = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.use_fire_bug))
        )
        ans_inspect_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.ans_inspect_element))
        )
        selec_name_not_type_locator = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.selec_name_not_type_locator))
        )
        ans_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.ans_password))
        )

        # Checkboxes
        two_num_that_not_prime = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.two_num_that_not_prime))
        )
        list_two_num_taht_not_prime = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.list_two_num_taht_not_prim))
        )
        num_list = []
        for num in list_two_num_taht_not_prime:
            num_list.append(num.text)
        select_correct_ans = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.select_correct_ans))
        )
        list_select_correct_ans = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, form_locators.list_select_correct_ans))
        )
        correct_ans_list = []
        for corct in list_select_correct_ans:
            correct_ans_list.append(corct.text)
        # Dropdown
        capital_of_pakistan = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.capital_of_pakistan))
        )
        islamabad = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.islamabad))
        )
        capital_of_punjab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.capital_of_punjab))
        )
        lahore = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, form_locators.lahore))
        )

        final_ans_dic = {use_fire_bug.text: ans_inspect_element.get_attribute("aria-label"), selec_name_not_type_locator.text:
            ans_password.get_attribute("aria-label"), two_num_that_not_prime.text: num_list,
                         select_correct_ans.text: correct_ans_list, capital_of_pakistan.text: islamabad.text,
                         capital_of_punjab.text: lahore.text}

        return final_ans_dic

        # for keys, values in final_ans_dic.items():
        #     print(keys)
        #     print(values)
        # self.driver.switch_to_window(self.window_before)
#=============================================================
        # all_questions = WebDriverWait(self.driver, 10).until(
        #     # EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="i.desc.866567686"]'))
        #     EC.presence_of_all_elements_located((By.CSS_SELECTOR,
        #     "div.freebirdFormviewerViewItemsItemItemHeader.freebirdFormviewerViewItemsItemIncorrect [role='heading']"))
        # )
        #
        # inspect_element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR,
        #         'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [aria-label="Inspecting Elements"]'))
        # )
        # password = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR,
        #         'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [aria-label="Password"]'))
        # )
        # not_a_prime_number1 = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR,
        #         'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [aria-label="51"]'))
        # )
        # not_a_prime_number2 = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR,
        #         'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [aria-label="21"]'))
        # )
        # select_correct_ans1 = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR,
        #         'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [aria-label="63/7 = 54/6"]'))
        # )
        # select_correct_ans2 = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR,
        #         'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [aria-label="72/9 = 64/8"]'))
        # )
        # select_correct_ans3 = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR,
        #         'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [aria-label="4*10 = 5*8"]'))
        # )

##==========================================================================================================
        # radio_buttons = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_all_elements_located((By.CSS_SELECTOR,
        #                             'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [role="radio"]'))
        # )
        # for radio in radio_buttons:
        #     print(radio.get_attribute("data-value"))
        #
        # checkboxs = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_all_elements_located((By.CSS_SELECTOR,
        #                             'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent [role="checkbox"]'))
        # )
        # for check in checkboxs:
        #     print(check.get_attribute("aria-label"))
        #
        # dropDowns = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_all_elements_located((By.CSS_SELECTOR,
        #         'div.freebirdFormviewerViewItemsItemGradingCorrectAnswerBoxContent div.freebirdFormviewerViewItemsSelectLabel'))
        # )
        # for drop in dropDowns:
        #     print(drop.text)





