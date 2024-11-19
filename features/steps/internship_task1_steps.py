from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open the Reelly main page')
def open_reelly_main_page(context):
    context.app.Reelly_filter_function.open_reelly_pg()
    sleep(4)

@when('log in and enter email')
def enter_email(context):
    context.app.Reelly_filter_function.input_email('joelbenjamin.85@gmail.com')
    sleep(4)

@when('Enter password')
def enter_pw(context):
    context.app.Reelly_filter_function.input_password('Joziah9918!!!')
    sleep(4)

@when('Click Continue Button')
def click_continue(context):
    context.app.Reelly_filter_function.click_continue()
    sleep(4)

@when('Click Secondary on menu')
def click_secondary_on_menu(context):
    sleep(5)
    context.app.Reelly_filter_function.click_on_secondary()


@when('Click on Filters')
def click_on_filters_button(context):
    sleep(5)
    context.app.Reelly_filter_function.click_on_filter_BTN()

@when('Filter the products by price range from 1200000')
def input_price_range_in_from_field(context):
    sleep(4)
    context.app.Reelly_filter_function.input_price_from_field('1200000')


@when('Filter the products by price range to 2000000')
def input_price_range_in_to_field(context):
    context.app.Reelly_filter_function.input_price_in_to_field('2000000')
    sleep(4)

@when('Click Apply Filters')
def click_apply_filters(context):
    sleep(4)
    context.app.Reelly_filter_function.click_apply_filters()

@then('Verify all products are within the specified price range')
def verify_prices(context):
    sleep(3)
    context.app.Reelly_filter_function.verify_price_in_range()
