import os

import allure, time
from os import path
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *
import random


class homepg():
    homeclick = (By.XPATH, "//a[@class='logo-img']//img")
    watchnowclick = (By.XPATH,
                     "//div[@class='carousel-item active']//div[@class='movie-content']//div[@class='btn-container']//div//button[@class='btn-view available-text d-none d-sm-block'][contains(text(),'Watch Now')]")
    closeplayer = (By.XPATH, "//div[@class='close tele-close']//img[@class='close-btn-image']")
    nextmovie = (By.XPATH, "//span[@class='carousel-control-next-icon']")
    mutebutton = (By.XPATH, "//span[contains(text(),'Volume/Mute')]/ancestor::button")
    resumebutton = (By.XPATH, "//button[contains(text(),'Resume watching')]")
    playbutton = (By.XPATH,
                  "//span[contains(text(),'Play/Pause')]/ancestor::div[@class='bmpui-ui-playbacktoggle-overlay']/div/button")
    addtolistcarousel = (By.XPATH,
                         "//div[@class='carousel-item active']//button[@class='cui-btn btn-movie'][contains(text(),'ADD TO LIST')]")
    createlist = (By.XPATH, "//div[@class='createNewList']")

    def __init__(self, browser):
        self.browser = browser

    """Home page-18"""

    @allure.step('To Verify Watch Now button is clikable and on click of it opens playout pop up')
    def verify_watchnow(self):
        time.sleep(10)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.homeclick))
        self.browser.find_element(*self.homeclick).click()
        self.browser.refresh()
        time.sleep(40)

        while True:
            try:
                watchnow = self.browser.find_element(*self.watchnowclick)
                bool = watchnow.is_displayed()
                if bool == True:
                    self.browser.find_element(*self.watchnowclick).click()
                    break
                else:
                    self.browser.find_element(*self.nextmovie).click()
            except:
                self.browser.find_element(*self.nextmovie).click()
        time.sleep(15)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.closeplayer))
        verify = self.browser.find_element(*self.closeplayer).is_displayed()
        return verify

    """Home page-20"""

    @allure.step('To Verify mute control of the pop up works correctly')
    def verify_popupmutecontrols(self):
        time.sleep(4)
        try:
            time.sleep(3)
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.resumebutton))
            data = self.browser.find_element(*self.resumebutton)
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.resumebutton))
            self.browser.find_element(*self.resumebutton).click()
        time.sleep(10)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.mutebutton))
        clas = self.browser.find_element(*self.mutebutton).get_attribute('class')
        print(clas)
        return clas

    @allure.step('To Verify all controls of the pop up works correctly')
    def verify_popupplaycontrols(self):
        time.sleep(5)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.playbutton))
        clas = self.browser.find_element(*self.playbutton).get_attribute('class')
        self.browser.find_element(*self.playbutton).click()
        time.sleep(3)
        return clas

    def verify_closeplayer(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.closeplayer))
        self.browser.find_element(*self.closeplayer).click()

    """Home page-36"""

    @allure.step('Verify functionality of Add to List button')
    def verify_addtolistbutton(self):
        time.sleep(4)
        while True:
            try:
                addtolist = self.browser.find_element_by_xpath(
                    "//div[@class='carousel-item active']//button[contains(text(),'ADD TO LIST')]")
                bool = addtolist.is_displayed()
                if bool == True:
                    addtolist.click()
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
        time.sleep(5)
        verify = self.browser.find_element(*self.createlist).is_displayed()
        time.sleep(3)
        self.browser.refresh()
        return verify
