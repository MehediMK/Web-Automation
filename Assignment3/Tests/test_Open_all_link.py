from selenium import webdriver
import time
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..','..'))
webdriver_path = os.path.join(os.getcwd(),r'..\Utills\chromedriver.exe')

from Assignment3.Pages.OpenLink import OpenLinkPage

def test_setUp():
    global driver
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_openLink():
    # call OpenLinkPage class
    open_link = OpenLinkPage(driver)

    driver.get('https://bikroy.com/en/ads')
    # scroll down
    open_link.scrollDown()
    # check copyright assert
    open_link.assert_copyright()

    # click link More from Bikroys
    open_link.open_all_link('//*[@id="app-wrapper"]/div[1]/div[6]/div/div/div/div[1]/div[2]/ul')


    # halp & support
    driver.get('https://bikroy.com/en/ads')
    # scroll down
    open_link.scrollDown()
    # click link More from Bikroys
    open_link.open_all_link('//*[@id="app-wrapper"]/div[1]/div[6]/div/div/div/div[1]/div[3]/ul')


    # Follow Bikroy
    driver.get('https://bikroy.com/en/ads')
    # scroll down
    open_link.scrollDown()
    # click link More from Bikroys
    open_link.open_all_link('//*[@id="app-wrapper"]/div[1]/div[6]/div/div/div/div[1]/div[4]/ul')


    # About Bikroy
    driver.get('https://bikroy.com/en/ads')
    # scroll down
    open_link.scrollDown()
    # click link More from Bikroys
    open_link.open_all_link('//*[@id="app-wrapper"]/div[1]/div[6]/div/div/div/div[1]/div[5]/ul')


def test_tearDown():
    driver.close()
    driver.quit()
