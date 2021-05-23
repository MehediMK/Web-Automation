from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..','..'))
webdriver_path = os.path.join(os.getcwd(),r'..\Utills\chromedriver.exe')

from Assignment.Pages.HomePage import Homepage


def test_setUp():
    global driver
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_Bikroy():
    driver.get('https://bikroy.com/')
    home = Homepage(driver)
    home.scroll_Down()
    home.check_copyright()
    home.assert_copyright()
    home.scroll_Up()
    home.find_Post_Your_Add_btn()
    home.assert_Post_Your_Add_btn()


def test_tearDown():
    driver.close()
    driver.quit()

