from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from Pages.base_page import Page

class ReellyFilterFunc(Page):

    secondary= (By.CSS_SELECTOR,"[href='/secondary-listings']")
    page_verification = (By.CSS_SELECTOR, "[class='page-title listing']")
    email_field = (By.CSS_SELECTOR, "[id='email-2']")
    password_field = (By.CSS_SELECTOR,"#field")
    continue_button = (By.CSS_SELECTOR, "[class='login-button w-button']")
    filters_button = (By.CSS_SELECTOR, "[class='filter-button']")
    unit_price_from_input = (By.CSS_SELECTOR, "[class='input-lield-text w-input']")
    unit_price_to_field = (By.CSS_SELECTOR, "[w-el-onchange-0-0='cca7a926-5d95-4018-a514-9633d083ed8c-0-0']")
    apply_filters_btn = (By.CSS_SELECTOR, "[class='button-filter w-button']")
    price_locator = (By.CLASS_NAME, "number-price-text")


    def __init__(self, driver):
        self.driver = driver

    def open_reelly_pg(self):
        self.driver.get('https://soft.reelly.io')

    def click_email_field(self):
        self.wait.until(EC.visibility_of_element_located(self.email_field), f' Element by {email_field} is not visible').click()

    def input_email(self,text):
        self.driver.find_element(*self.email_field).send_keys('joelbenjamin.85@gmail.com')

    def input_password(self,text):
        self.driver.find_element(*self.password_field).send_keys('Joziah9918!!!')

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def click_on_secondary(self):
        self.driver.find_element(*self.secondary).click()

    def click_on_filter_BTN(self):
        self.driver.find_element(*self.filters_button).click()

    # def click_from_input_field(self, text):
    #         self.driver.find_element(*self.unit_price_from_input).send_keys('1200000')
    #
    # def click_to_input_field(self, text):
    #         self.driver.find_element(*self.unit_price_to_field).send_keys('2000000')

    def input_price_from_field(self, text):
        self.driver.find_element(*self.unit_price_from_input).send_keys('1200000')

    def input_price_in_to_field(self, text):
        self.driver.find_element(*self.unit_price_to_field).send_keys('2000000')

    def click_apply_filters(self):
        self.driver.find_element(*self.apply_filters_btn).click()

    def verify_price_in_range(context):
        # Find all price elements
        price_elements = context.driver.find_elements(By.CLASS_NAME, 'number-price-text')

        for price_element in price_elements:
            price_text = price_element.text

            # Remove currency symbol and convert to integer
            numeric_price = int(price_text.replace('AED ', '').replace(',', ''))

            # Check if price is within the range
            assert 1200000 <= numeric_price <= 2000000, f"Price {numeric_price} is not within the range"
