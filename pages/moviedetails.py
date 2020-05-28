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


class moviedetails():
    movieheader = (By.XPATH, "//ul[@class='menu-items']//a[@id='Movies']")
    searchmovie = (By.XPATH, "//input[@placeholder='Search Movie Title, Actor, or Genre']")
    moviedetail = (
        By.XPATH,
        "//li[1]//div[2]//mgm-list-poster[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]")
    viewdetailclick = (By.XPATH,
                       "//li[1]//div[@class='desk-on']//button[contains(text(),'View details')]")
    movieheaderinfo = (By.XPATH, "//div[@class='movie-info']")
    moviesynopsis = (By.XPATH, "//div[@class='col-7 right active']/p")
    movietrailer = (By.XPATH, "//div[contains(text(),'Trailer')]")
    moviephotos = (By.XPATH, "//div[contains(text(),'Photos')]")
    castprod = (By.XPATH, "//h1[contains(text(),'Cast, Production and Crew')]")
    HeroImage = (By.XPATH, "//div[@class='overlay ng-star-inserted']")
    titlelogo = (By.XPATH, "//img[@class='logo-image ng-star-inserted']")
    watchmoviebutton = (By.XPATH, "//button[contains(text(),'Watch movie')]")
    watchtrailerbutton = (By.XPATH, "//button[contains(text(),'Watch trailer')]")
    addtolistbutton = (By.XPATH, "//button[contains(text(),'ADD TO LIST')]")
    closemovie = (By.XPATH, "//div[@class='close tele-close']//img[@class='close-btn-image']")
    trailerverify = (By.XPATH, "//button[@class='bmpui-ui-volumetogglebutton bmpui-unmuted']")
    traileroverlay = (By.XPATH, "//button[@id='bmpui-id-849']//div[@class='bmpui-image']")
    addtolistarrow = (By.XPATH, "//div[@class='add-to-list']/span")
    addtolistmovie = (By.XPATH, "//span[contains(text(),'movietest')]/preceding-sibling::span[1]")
    addmovietolist = (By.XPATH, "//div[@class='atl-newlistbox']/button/span")
    mylist = (By.XPATH, "//ul[@class='menu-items']//a[@id='My Lists']")
    titleinlist = (By.XPATH, "//a[contains(text(),'movietest')]")
    verifytitlelist = (
        By.XPATH, "//div[@class='desk-on']//p[contains(text(),'Spectre')]")
    synopsisimage = (By.XPATH, "//img[@class='images image-loaded']")
    synopsisrate = (By.XPATH, "//p[contains(text(),'Rated')]")
    synopsisgenre = (By.XPATH, "//p[contains(text(),'Genre')]")
    synopsisrelease = (By.XPATH, "//p[contains(text(),'Us Release Date')]")
    synopsisdirector = (By.XPATH, "//p[@class='director-title']")
    synopsiscast = (By.XPATH, "//div[@class='synopsis-cast']//p[@class='cast-title'][contains(text(),'Cast')]")
    synopsiscopyright = (By.XPATH, "//span[contains(text(),'© 2015 Danjaq, LLC, Metro-Goldwyn-Mayer Studios In')]")
    synopsisdesc = (By.XPATH, "//p[@class='synopsis-title']/following-sibling::p")
    trailertitle = (By.XPATH, "//div[contains(text(),'Trailer')]")

    trailer_button = (By.XPATH, "//button[@class='cui-btn btn-trailer']")
    play_trailer = (By.XPATH, "//button[@id='bmpui-id-204']")
    portofplayer = (By.XPATH, "//button[@id='bmpui-id-187']")
    phototitle = (By.XPATH, "//div[contains(text(),'Photos')]")
    slidearrow = (By.XPATH, "//i[@class='next']")
    viewport = (By.XPATH,
                "//ng-scrollbar[@class='scroll-event ng-scrollbar-dark_background ng-scrollbar']//div[@class='ng-scroll-content']")
    verifyphotochange = (By.XPATH, "//div[@class='active-img']/preceding-sibling::i")
    castdetails = (By.XPATH, "//div[@class='cast']//p[@class='cast-desc']/span")
    directorname = (By.XPATH, "//p[@class='cast-sub-desc']//span[contains(text(),'Sam Mendes')]")
    producername = (By.XPATH, "//div[@class='row']//div[2]//div[1]//p[2]")
    execproducername = (By.XPATH, "//div[@class='col-lg-3 cast-sub-info']//p[@class='cast-sub-desc']")

    def __init__(self, browser):
        self.browser = browser

    """movie details-26"""

    @allure.step('To verify movie detail page')
    def verify_moviedetails(self):
        actionchains = ActionChains(self.browser)
        self.browser.refresh()
        time.sleep(35)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.movieheader))
        self.browser.find_element(*self.movieheader).click()
        time.sleep(40)
        self.browser.find_element(*self.searchmovie).send_keys("spectre")
        actionchains.send_keys(Keys.ENTER).perform()
        time.sleep(12)
        lst = self.browser.find_element(*self.viewdetailclick)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verifyoverlay = self.browser.find_element(*self.viewdetailclick)
        ActionChains(self.browser).move_to_element(verifyoverlay).perform()
        time.sleep(6)
        self.browser.find_element(*self.viewdetailclick).click()

    @allure.step('To verify movie header in movie detail page')
    def verify_movieheader(self):
        time.sleep(40)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.movieheaderinfo))
        verify = self.browser.find_element(*self.movieheaderinfo).is_displayed()
        return verify

    @allure.step('To verify movie synopsis in movie detail page')
    def verify_moviesynopsis(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.moviesynopsis)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.moviesynopsis))
        verify = self.browser.find_element(*self.moviesynopsis).is_displayed()
        return verify

    @allure.step('To verify movie trailer in movie detail page')
    def verify_movietrailer(self):
        time.sleep(20)
        lst = self.browser.find_element(*self.movietrailer)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.movietrailer))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.movietrailer))
        verify = self.browser.find_element(*self.movietrailer).is_displayed()
        return verify

    @allure.step('To verify movie trailer in movie detail page')
    def verify_moviephotos(self):
        time.sleep(10)
        lst = self.browser.find_element(*self.moviephotos)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.moviephotos))
        verify = self.browser.find_element(*self.moviephotos).is_displayed()
        return verify

    @allure.step('To verify movie trailer in movie detail page')
    def verify_moviecastprod(self):
        lst = self.browser.find_element(*self.castprod)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.castprod))
        verify = self.browser.find_element(*self.castprod).is_displayed()
        return verify

    """movie details-27"""

    @allure.step('To verify header image in movie detail page')
    def verify_movieheaderimage(self):
        time.sleep(10)
        verify = self.browser.find_element(*self.HeroImage).is_displayed()
        return verify

    @allure.step('To verify title logo in movie detail page')
    def verify_movielogo(self):
        time.sleep(2)
        verify = self.browser.find_element(*self.titlelogo).is_displayed()
        return verify

    @allure.step('To verify watch movie button in movie detail page')
    def verify_watchmoviebutton(self):
        time.sleep(1)
        verify = self.browser.find_element(*self.watchmoviebutton).is_displayed()
        return verify

    @allure.step('To verify watch trailer button in movie detail page')
    def verify_watchtrailerbutton(self):
        time.sleep(1)
        verify = self.browser.find_element(*self.watchtrailerbutton).is_displayed()
        return verify

    @allure.step('To verify Add to List button in movie detail page')
    def verify_addtolistbutton(self):
        time.sleep(1)
        verify = self.browser.find_element(*self.addtolistbutton).is_displayed()
        return verify

    """movie details-28"""

    @allure.step('To verify watch movie on watch movie button click')
    def verify_watchmovie(self):
        time.sleep(5)
        self.browser.find_element(*self.watchmoviebutton).click()
        time.sleep(20)
        verify = self.browser.find_element(*self.closemovie).is_displayed()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.closemovie))
        self.browser.find_element(*self.closemovie).click()
        return verify

    """movie details-29"""

    @allure.step('To verify watch trailer on watch trailer button click')
    def verify_watchtrailer(self):
        time.sleep(30)
        lst = self.browser.find_element(*self.watchtrailerbutton)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.watchtrailerbutton))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        self.browser.find_element(*self.watchtrailerbutton).click()
        time.sleep(20)

    """movie details-30"""

    @allure.step('To verify added movie in the list')
    def verify_addedmovieinlist(self):
        time.sleep(5)
        lst = self.browser.find_element(*self.addtolistbutton)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        self.browser.find_element(*self.addtolistbutton).click()
        time.sleep(4)
        # lsst = self.browser.find_element(*self.addtolistmovie)
        # self.browser.execute_script("arguments[0].scrollIntoView();", lsst)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.addtolistmovie))
        self.browser.find_element(*self.addtolistmovie).click()
        time.sleep(8)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.addmovietolist))
        self.browser.find_element(*self.addmovietolist).click()
        time.sleep(50)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.mylist))
        lst = self.browser.find_element(*self.mylist)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        self.browser.find_element(*self.mylist).click()
        time.sleep(8)
        self.browser.refresh()
        time.sleep(55)
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titleinlist))
        self.browser.find_element(*self.titleinlist).click()
        time.sleep(30)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.verifytitlelist))
        footer = self.browser.find_element(*self.verifytitlelist).is_displayed()
        return footer

    """movie details-31"""

    @allure.step('Verify elements in Synopsis section of Movie Details page')
    def verify_synopsisimage(self):
        time.sleep(20)
        self.browser.refresh()
        time.sleep(50)
        # WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.watchmoviebutton))
        verifyoverlay = self.browser.find_element(*self.watchmoviebutton)
        ActionChains(self.browser).move_to_element(verifyoverlay).perform()
        time.sleep(30)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.synopsisimage))
        lst = self.browser.find_element(*self.synopsisimage)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        synopimage = self.browser.find_element(*self.synopsisimage).is_displayed()
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

    @allure.step('Verify director in Synopsis section of Movie Details page')
    def verify_synopsisdirector(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.synopsisdirector))
        desc = self.browser.find_element(*self.synopsisdirector).is_displayed()
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

    """movie details-32"""

    @allure.step('Verify elements in Trailer section of Movie Details page')
    def verify_trailerelements(self):
        time.sleep(5)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.watchtrailerbutton))
        self.browser.find_element(*self.watchtrailerbutton).click()
        time.sleep(25)
        lst = self.browser.find_element(*self.trailertitle)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        trailer = self.browser.find_element(*self.trailertitle).is_displayed()
        return trailer

    @allure.step('Verify port of player in Trailer section of Movie Details page')
    def verify_trailerplayer(self):
        time.sleep(14)
        lst = self.browser.find_element(*self.play_trailer)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.play_trailer))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        time.sleep(10)
        verify = lst.is_displayed()
        return verify

    """movie details-33"""

    @allure.step('Click on trailer button to play trailer')
    def click_trailer_button(self):
        time.sleep(1)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.trailer_button))
        trailer = self.browser.find_element(*self.trailer_button)
        self.browser.execute_script("arguments[0].scrollIntoView();", trailer)
        time.sleep(2)
        trailer.click()

    @allure.step('Verify trailer is getting play or not')
    def verify_trailerplay(self):
        time.sleep(2)
        clas = self.browser.find_element(*self.play_trailer).get_attribute('class')
        print(clas)
        return clas

    def refresh(self):
        time.sleep(2)
        self.browser.refresh()

    """movie details-34"""

    @allure.step('To verify title in photo section')
    def verify_phototitle(self):
        time.sleep(20)
        lst = self.browser.find_element(*self.phototitle)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.phototitle))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verifyphototitle = self.browser.find_element(*self.phototitle).is_displayed()
        return verifyphototitle

    @allure.step('To verify slide arrow in photo section')
    def verify_photoslidearrow(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.slidearrow)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.slidearrow))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verifyphotoarrow = self.browser.find_element(*self.slidearrow).is_displayed()
        return verifyphotoarrow

    @allure.step('To verify view port in photo section')
    def verify_photoviewport(self):
        time.sleep(10)
        lst = self.browser.find_element(*self.viewport)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.viewport))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verifyphotoviewport = self.browser.find_element(*self.viewport).is_displayed()
        return verifyphotoviewport

    """movie details-35"""

    @allure.step('To verify User should be able to navigate between photos by clicking the arrows')
    def verify_photoslidearrow(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.slidearrow)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.slidearrow))
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

    @allure.step('To Verify Director name in move details page')
    def verify_directorname(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.directorname)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.directorname))
        verify = self.browser.find_element(*self.directorname).is_displayed()
        return verify

    @allure.step('To Verify producer name in move details page')
    def verify_producername(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.producername)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.producername))
        verify = self.browser.find_element(*self.producername).is_displayed()
        return verify

    @allure.step('To Verify exec. producer name in move details page')
    def verify_execproducername(self):
        time.sleep(15)
        lst = self.browser.find_element(*self.execproducername)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.execproducername))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verify = self.browser.find_element(*self.execproducername).is_displayed()
        return verify
