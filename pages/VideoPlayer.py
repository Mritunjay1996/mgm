from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.webdriver import WebDriver
import allure
from pathlib import Path
import csv
import time

from selenium.webdriver import ActionChains

class videoplayer:

    close_button = (By.XPATH, "//div/img[@class='close-btn-image']")
    PlayPause_button = (By.XPATH, "(//div//span[text()='Play/Pause'])[1]")
    VolumeMute_button = (By.XPATH, "//div//span[text()='Volume/Mute']")
    setting_button = (By.XPATH, "//div//span[text()='Settings']")
    fullscreen_button = (By.XPATH, "//div//span[text()='Fullscreen']")
    playout_popup = (By.XPATH, "//div[@class='modal-body']")
    watchnow_button = (By.XPATH, "//div[@class='btn-container']/button[text()=' Watch Now ']")

    def __init__(self, browser):
        self.browser = browser
        #self.browser = WebDriver

    def ClickWatchNowButton(self):
        time.sleep(10)
        self.browser.find_element(*self.watchnow_button).click()
        time.sleep(5)

    def PlayerPopup(self):
        time.sleep(15)
        return self.browser.find_element(*self.playout_popup).is_displayed()

    def PlayPauseButton(self):
        play = self.browser.find_element(*self.PlayPause_button)
        play.location_once_scrolled_into_view
        time.sleep(5)
        global actionchains
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(play).perform()
        btn = play.is_displayed()
        return btn


    def VolumeMuteButton(self):
        play = self.browser.find_element(*self.VolumeMute_button)
        play.location_once_scrolled_into_view
        time.sleep(5)
        global actionchains
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(play).perform()
        btn = play.is_displayed()
        return btn

    def SettingButton(self):
        return self.browser.find_element(*self.setting_button).is_displayed()

    def FullscreenButton(self):
        return self.browser.find_element(*self.fullscreen_button).is_displayed()

    def CloseButon(self):
        return self.browser.find_element(*self.close_button).is_displayed()

    def ClickCloseButton(self):
        time.sleep(15)
        self.browser.find_element(*self.close_button).click()