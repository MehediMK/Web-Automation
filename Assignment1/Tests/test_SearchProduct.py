from selenium import webdriver
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..','..'))
webdriver_path = os.path.join(os.getcwd(),r'..\Utills\chromedriver.exe')

from Assignment1.Pages.SearchProduct import SearchProducts


def test_setUp():
    global driver
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_SearchProduct():
    # get citys name from home page
    driver.get('https://bikroy.com/en')
    b_city = SearchProducts(driver)
    b_city.list_the_city()

    # this is used for product row
    driver.get('https://bikroy.com/en/ads/dhaka')
    b_city.lowest_product_price()

    # Posted on 22 May 8:26 pm, Farmgate, Dhaka or not
    b_city.post_date_location()

    # here checked description or not
    b_city.check_description()

    # # here click to show phone number
    b_city.click_phone_number()

    # assert phone valid or not
    b_city.check_phone_valid()

def test_tearDown():
    driver.close()
    driver.quit()


