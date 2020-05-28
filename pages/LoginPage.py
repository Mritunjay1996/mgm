"""
This module contains the page object
for the homepage.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.webdriver import WebDriver
import allure
from pathlib import Path
import csv
import time

class loginpage:
    """
    Define all web element locators and test steps
    in this class for homepage
    """

    URL = "https://mgm-roar-dev.practicallogix.com/"
    verify_login_title = (By.XPATH, "//h1[@class='login-text']")
    carousal_image = (By.XPATH, "//div[@class='auth-component']")
    email_textbox = (By.XPATH, "//input[@name='username']")
    next_button = (By.XPATH, "//div[@class='o-form-button-bar']/input")
    request_an_account = (By.XPATH, "//a[contains(text(),'Create an account')]")
    enter_password = (By.XPATH, "//input[@type='password']")
    menu_link_movie = (By.XPATH, "//a[@id='Movies']")

    def __init__(self, browser):
        self.browser = browser
        #self.browser = WebDriver

    @allure.step('Load Login page When user hit ROAR app url')
    def load(self):
        self.browser.get(self.URL)
        verify = self.browser.find_element(*self.verify_login_title).text
        print(verify)
        return verify

    @allure.step('verify carousel image set by admin')
    def CarouselImage(self):
        verify_image = self.browser.find_element(*self.carousal_image).is_displayed()
        return verify_image

    @allure.step('On each visit user see different carousel image')
    def DifferentCarouselImage(self):
        time.sleep(4)
        FirstImage = self.browser.find_element(*self.carousal_image).get_attribute("style")
        self.browser.refresh()
        time.sleep(4)
        SecondImage = self.browser.find_element(*self.carousal_image).get_attribute("style")
        self.browser.refresh()
        time.sleep(4)
        ThirdImage = self.browser.find_element(*self.carousal_image).get_attribute("style")
        print(FirstImage)
        print(SecondImage)
        print(ThirdImage)
        
        if(FirstImage == SecondImage and SecondImage == ThirdImage):
            return False
        else:
            return True

    @allure.step('Verify Email box present in login model')
    def VerifyEmail(self):
        #self.browser.find_element(*self.email_textbox).send_keys("aaaa")
        return self.browser.find_element(*self.email_textbox).is_displayed()

    @allure.step('Verify Next button present in login model')
    def VerifyNextButton(self):
        return self.browser.find_element(*self.next_button).is_displayed()

    @allure.step('Verify Request an account button present in login model')
    def VerifyRequestAnAccount(self):
        return self.browser.find_element(*self.request_an_account).is_displayed()

    @allure.step('Verify user is able to enter Email in email field')
    def EnterEmail(self, username):
        self.browser.find_element(*self.email_textbox).send_keys(username)

    @allure.step('Verify user with valid email id can proceed to next step')
    def ClickNext(self):
        self.browser.find_element(*self.next_button).click()
        return self.browser.find_element(*self.enter_password).is_displayed()

    @allure.step('verify user is successfully logged in')
    def EnterPassword(self, password):
        self.browser.find_element(*self.enter_password).send_keys(password)
        time.sleep(4)

    def VerifyLogin(self):
        time.sleep(10)
        return self.browser.find_element(*self.menu_link_movie).is_displayed()

        '''with open(self.license_file, mode='a', newline='') as csvFile:
            csv_writer = csv.writer(csvFile)
            csv_writer.writerow([abc])
        print(len(jobs))
        print(abc)'''
    