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


class tvdetails():
    televisionclick = (By.XPATH, "//ul[@class='menu-items']//a[@id='Television']")
    searchmovie = (By.XPATH, "//input[@placeholder='Search Movie Title, Actor, or Genre']")
    viewdetailclick = ((By.XPATH, "//li[1]//div[@class='desk-on']//button[contains(text(),'View details')]"))
    synopsisimage = (By.XPATH, "//img[@class='images image-loaded']")
    synopsisrate = (By.XPATH, "//p[contains(text(),'Rated')]")
    synopsisgenre = (By.XPATH, "//p[contains(text(),'Genre')]")
    synopsisrelease = (By.XPATH, "//p[contains(text(),'Us Release Date')]")
    synopsiscast = (
        By.XPATH, "//div[@class='synopsis-cast ng-star-inserted']//p[@class='cast-title'][contains(text(),'Cast')]")
    synopsiscopyright = (By.XPATH, "//span[contains(text(),'© 2011-2016 MTV Networks and Viacom International')]")
    synopsisdesc = (By.XPATH, "//div[@class='synopsis-detail']/preceding-sibling::p")
    trailertitle = (By.XPATH, "//div[contains(text(),'Trailer')]")
    traileroverlay = (By.XPATH, "//button[@id='bmpui-id-204']")
    portofplayer = (By.XPATH, "//button[@id='bmpui-id-187']")
    phototitle = (By.XPATH, "//div[contains(text(),'Photos')]")
    slidearrow = (By.XPATH, "//i[@class='next ng-star-inserted']")
    play_pause = (By.XPATH, "//button[@id='bmpui-id-187']")
    play = (By.XPATH, "//button[@id='bmpui-id-204']//div[@class='bmpui-image']")
    viewport = (By.XPATH,
                "//ng-scrollbar[@class='scroll-event ng-scrollbar ng-scrollbar-dark_background']//div[@class='ng-scroll-content']")
    verifyphotochange = (By.XPATH, "//div[@class='active-img ng-star-inserted']/preceding-sibling::i")
    castdetails = (By.XPATH, "//div[@class='row']/div/div[1]/p[2]")
    execproducername = (By.XPATH, "//p[@class='cast-sub-title cast-executive']/following-sibling::p/span")

    def __init__(self, browser):
        self.browser = browser

    """Tv details-31"""

    @allure.step('To verify Tv detail page')
    def verify_Tvdetails(self):
        actionchains = ActionChains(self.browser)
        self.browser.refresh()
        time.sleep(35)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.televisionclick))
        self.browser.find_element(*self.televisionclick).click()
        time.sleep(40)
        self.browser.find_element(*self.searchmovie).send_keys("Teen Wolf")
        actionchains.send_keys(Keys.ENTER).perform()
        time.sleep(30)
        card4 = self.browser.find_element(*self.viewdetailclick)
        ActionChains(self.browser).move_to_element(card4).perform()
        time.sleep(2)
        card4.click()

    @allure.step('Verify elements in Synopsis section of Movie Details page')
    def verify_synopsisimage(self):
        time.sleep(10)
        self.browser.refresh()
        time.sleep(40)
        lst = self.browser.find_element(*self.synopsisimage)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.synopsisimage))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        synopimage = lst.is_displayed()
        return synopimage

    @allure.step('Verify desc in Synopsis section of Movie Details page')
    def verify_synopsisdesc(self):
        time.sleep(10)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.synopsisdesc))
        desc = self.browser.find_element(*self.synopsisdesc).is_displayed()
        return desc

    @allure.step('Verify rated in Synopsis section of Movie Details page')
    def verify_synopsisrate(self):
        time.sleep(10)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.synopsisrate))
        desc = self.browser.find_element(*self.synopsisrate).is_displayed()
        return desc

    @allure.step('Verify genre in Synopsis section of Movie Details page')
    def verify_synopsisgenre(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.synopsisgenre))
        desc = self.browser.find_element(*self.synopsisgenre).is_displayed()
        return desc

    @allure.step('Verify release date in Synopsis section of Movie Details page')
    def verify_synopsisrelease(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.synopsisrelease))
        desc = self.browser.find_element(*self.synopsisrelease).is_displayed()
        return desc

    @allure.step('Verify cast in Synopsis section of Movie Details page')
    def verify_synopsiscast(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.synopsiscast))
        desc = self.browser.find_element(*self.synopsiscast).is_displayed()
        return desc

    @allure.step('Verify copy right in Synopsis section of Movie Details page')
    def verify_synopsiscopyright(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.synopsiscopyright))
        desc = self.browser.find_element(*self.synopsiscopyright).is_displayed()
        return desc

    """tv details-32"""

    @allure.step('Verify title in Trailer section of tv Details page')
    def verify_trailertitle(self):
        time.sleep(20)
        lst = self.browser.find_element(*self.trailertitle)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.trailertitle))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        trailer = lst.is_displayed()
        return trailer

    @allure.step('Verify trailer screen of tv Details page')
    def verify_trailerscreen(self):
        time.sleep(30)
        verifyoverlay = self.browser.find_element(*self.traileroverlay)
        ActionChains(self.browser).move_to_element(verifyoverlay).perform()
        verifyoverlay.click()
        time.sleep(4)
        play = self.browser.find_element(*self.play_pause)
        trailerplaybutton = play.is_displayed()
        return trailerplaybutton
        # time.sleep(15)
        # verifyoverlay1 = self.browser.find_element(*self.portofplayer)
        # ActionChains(self.browser).move_to_element(verifyoverlay1).perform()
        # lst = self.browser.find_element(*self.portofplayer)
        # WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.portofplayer))
        # self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        # verifyoverlay1.click()

    """tv details-33"""

    @allure.step('Verify trailer is getting play or not')
    def verify_trailerplay(self):
        time.sleep(2)
        clas = self.browser.find_element(*self.traileroverlay).get_attribute('class')
        print(clas)
        # verifyoverlay = self.browser.find_element(*self.traileroverlay)
        # verifyoverlay.click()
        return clas

    """movie details-34"""

    @allure.step('To verify title in photo section')
    def verify_phototitle(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.phototitle)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verifyphototitle = self.browser.find_element(*self.phototitle).is_displayed()
        return verifyphototitle

    @allure.step('To verify slide arrow in photo section')
    def verify_photoslidearrow(self):
        time.sleep(10)
        lst = self.browser.find_element(*self.slidearrow)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verifyphotoarrow = self.browser.find_element(*self.slidearrow).is_displayed()
        return verifyphotoarrow

    @allure.step('To verify view port in photo section')
    def verify_photoviewport(self):
        time.sleep(10)
        lst = self.browser.find_element(*self.viewport)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verifyphotoviewport = self.browser.find_element(*self.viewport).is_displayed()
        return verifyphotoviewport

    """movie details-35"""

    @allure.step('To verify User should be able to navigate between photos by clicking the arrows')
    def verify_photoslidearrow(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.slidearrow)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        self.browser.find_element(*self.slidearrow).click()
        time.sleep(10)
        verifyphotochnge = self.browser.find_element(*self.verifyphotochange).is_displayed()
        return verifyphotochnge

    """movie details-37"""

    @allure.step('To Verify elements of Cast, Crew & Prodcution')
    def verify_castdetails(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.castdetails)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.castdetails))
        verify = self.browser.find_element(*self.castdetails).is_displayed()
        return verify

    @allure.step('To Verify exec. producer name in move details page')
    def verify_execproducername(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.execproducername)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.execproducername))
        verify = self.browser.find_element(*self.execproducername).is_displayed()
        return verify
