import allure, time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from resources.variables import *
from pathlib import Path
from os import path
import os


class tvpageObj:
    tv_menu = (By.XPATH, "//ul[@class='menu-items']//a[@id='Television']")
    header_backimage = (By.XPATH, "//div[@class='back-btn d-none']/following-sibling::div[@class='overlay']")
    header = (By.XPATH, "//div[@class='television-logo']/img")
    title_overview = (By.XPATH, "//p[contains(text(),'TITLE OVERVIEW')]")
    tv_synopsis = (By.XPATH, "//div[@class='col-7 right active']/p[1]")
    trailer_title = (By.XPATH, "//div[contains(text(),'Trailer')]")
    photos_title = (By.XPATH, "//div[@class='title'][contains(text(),'Photos')]")
    cast_crew = (By.XPATH, "//h1[contains(text(),'Cast, Production and Crew')]")
    title_logo = (By.XPATH, "//img[@class='images image-loaded']")
    seasons_episode = (By.XPATH, "//div[@class='season']/span[1]")
    season_dropdown = (By.XPATH, "//div[@class='dropdown-filter']")
    addTolist_drpdown = (By.XPATH, "//div[@class='add-to-list']/button[1]")
    drpdown_seasnOption = (By.XPATH, "//div[@class='dropdown-list-header']/following-sibling::div[2]/div")
    season1 = (By.XPATH, "//div[contains(text(),'SEASON 1')]")
    addlist_button = (By.XPATH, "//div[@class='atl-newlistbox']/button[1]")
    allseason_option = (By.XPATH, "//div[@class='dropdown-option'][contains(text(), 'ALL SEASONS')]")
    watch_trailer = (By.XPATH, "//button[contains(text(),'Watch trailer')]")
    episodes_tab = (By.XPATH, "//div[@class='col-lg-3 episode visible']/p[1]")
    episode_img = (By.XPATH, "//div[@class='episode-card']/div[1]/div[1]/img[1]")
    episode_number = (By.XPATH, "//div[contains(text(),'EPISODE 1')]")
    episode_name = (By.XPATH, "//div[contains(text(),'Rites Of Passage')]")
    episode_synopsis = (By.XPATH, "//div[@class='synopsis']")
    # episode1_detailed = (By.XPATH, "//span[contains(text(),'Episode 0001 :')]")
    episode1_detailed = (By.XPATH, "//div[@class='col-7 right active']/p[1]/span[1]")
    epiDetailed_img = (By.XPATH, "//img[@class='images image-loaded']")
    episode_playIcon = (By.XPATH, "//i[@class='icons']")
    epi_synopsis = (By.XPATH, "//p[contains(.,'Rites Of Passage Synopsis')]")
    chkbox_forfooter = (By.XPATH, "//input[@id='select-all']")
    share_btn = (By.XPATH, "//button[@class='share-btn']")
    play_begining = (By.XPATH, "//button[@class='watch-again-btn btn-view']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Open Telivisions Page')
    def open_television(self):
        time.sleep(2)
        self.browser.find_element(*self.tv_menu).click()

    def refresh(self):
        time.sleep(2)
        self.browser.refresh()

    @allure.step('Verify Header of tv detailed page ')
    def verify_tvdetailed_header(self):
        time.sleep(2)
        return self.browser.find_element(*self.header).is_displayed()

    @allure.step('Verify Title overview on TV detailed page')
    def verify_titleoverview(self):
        time.sleep(2)
        title = self.browser.find_element(*self.title_overview)
        self.browser.execute_script("arguments[0].scrollIntoView();", title)
        time.sleep(2)
        return self.browser.find_element(*self.title_overview).text

    @allure.step('Verify Synopsis of Television in detailed page ')
    def verify_tvsynopsis(self):
        time.sleep(2)
        return self.browser.find_element(*self.tv_synopsis).is_displayed()

    @allure.step('Verify Synopsis of TV in detailed page by Level ')
    def verify_tvsynopsis_bylevel(self):
        time.sleep(2)
        synopsis = self.browser.find_element(*self.tv_synopsis)
        self.browser.execute_script("arguments[0].scrollIntoView();", synopsis)
        time.sleep(2)
        return synopsis.is_displayed()

    @allure.step('Verify synopsis for episode in tv detailed page')
    def verify_epiSynopsis_detailed(self):
        time.sleep(2)
        return self.browser.find_element(*self.epi_synopsis).is_displayed()

    @allure.step('Verify Trailer title should be displayed on tv detailed page')
    def verify_trailerTitle(self):
        time.sleep(2)
        trailer = self.browser.find_element(*self.trailer_title)
        self.browser.execute_script("arguments[0].scrollIntoView();", trailer)
        time.sleep(3)
        return trailer.is_displayed()

    @allure.step('Verify Photo title should be displayed on tv detailed page')
    def verify_photoTitle(self):
        time.sleep(2)
        photo = self.browser.find_element(*self.photos_title)
        self.browser.execute_script("arguments[0].scrollIntoView();", photo)
        time.sleep(3)
        return photo.is_displayed()

    @allure.step('Verify Cast, Crew and Production title should be displayed on tv detailed page')
    def verify_castcrewTitle(self):
        time.sleep(2)
        cast = self.browser.find_element(*self.cast_crew)
        self.browser.execute_script("arguments[0].scrollIntoView();", cast)
        time.sleep(3)
        return cast.is_displayed()

    @allure.step('Verify Hero image in TV detailed page ')
    def verify_heroImage(self):
        time.sleep(2)
        header = self.browser.find_element(*self.header)
        self.browser.execute_script("arguments[0].scrollIntoView();", header)
        time.sleep(3)
        return self.browser.find_element(*self.header_backimage).is_displayed()

    @allure.step('Verify Title treatment logo in tv detailed page')
    def verify_titletreatment_logo(self):
        time.sleep(2)
        logo = self.browser.find_element(*self.title_logo)
        self.browser.execute_script("arguments[0].scrollIntoView();", logo)
        time.sleep(3)
        return self.browser.find_element(*self.title_logo).is_displayed()

    @allure.step('Verify Numbers of seasons and episodes on tv detailed page ')
    def verify_seasons_episodes(self):
        time.sleep(2)
        return self.browser.find_element(*self.seasons_episode).is_displayed()

    @allure.step('Verify All seasons dropdown on tv detailed page ')
    def verify_seasonsDrpdown(self):
        time.sleep(2)
        return self.browser.find_element(*self.season_dropdown).is_displayed()

    @allure.step('Click on season dropdown')
    def click_seasondrpdown(self):
        time.sleep(2)
        self.browser.find_element(*self.seasons_episode).click()

    @allure.step('Verify Add to List dropdown on tv detailed page ')
    def verify_addListDrpdown(self):
        time.sleep(2)
        return self.browser.find_element(*self.addTolist_drpdown).is_displayed()

    @allure.step('Clicking on add to list button on tb detailed page ')
    def click_addTolist_btn(self):
        time.sleep(2)
        self.browser.find_element(*self.addTolist_drpdown).click()

    @allure.step('Clicking on add button to adding tv in list ')
    def click_addButton(self):
        time.sleep(2)
        self.browser.find_element(*self.addlist_button).click()

    @allure.step('Verify IN season drop down by default All season should be selected')
    def verify_selectedDrpdown(self):
        time.sleep(2)
        season = self.browser.find_element(*self.seasons_episode)
        self.browser.execute_script("arguments[0].scrollIntoView();", season)
        time.sleep(3)
        return self.browser.find_element(*self.season_dropdown).text

    @allure.step('Select Season 1 from dropdown ')
    def select_season1Drpdown(self):
        time.sleep(4)
        season = self.browser.find_element(*self.seasons_episode)
        self.browser.execute_script("arguments[0].scrollIntoView();", season)
        time.sleep(3)
        self.browser.find_element(*self.season_dropdown).click()
        time.sleep(4)
        self.browser.find_element(*self.season1).click()

    @allure.step('Count total numbers of season present in drop down option on tv page ')
    def count_totaldrpdwn_option(self):
        time.sleep(2)
        self.browser.find_element(*self.season_dropdown).click()
        time.sleep(3)
        count = self.browser.find_elements(*self.drpdown_seasnOption)
        print(len(count))
        time.sleep(2)
        return len(count)

    @allure.step('Select All season option from dropdown ')
    def select_allseason_option(self):
        time.sleep(2)
        self.browser.find_element(*self.season_dropdown).click()
        time.sleep(2)
        self.browser.find_element(*self.allseason_option).click()

    @allure.step('Verify Watch trailer button in header with season level')
    def verify_trailerBtn(self):
        time.sleep(3)
        return self.browser.find_element(*self.watch_trailer).is_displayed()

    @allure.step('Verify Episode tab should be displayed when season is selected')
    def verify_episodeTab(self):
        time.sleep(2)
        season = self.browser.find_element(*self.season_dropdown)
        self.browser.execute_script("arguments[0].scrollIntoView();", season)
        time.sleep(3)
        drpdown = self.browser.find_element(*self.season_dropdown).text
        try:
            if drpdown == "SEASON 1":
                return self.browser.find_element(*self.episodes_tab).is_displayed()
            else:
                return False
        except:
            return False

    @allure.step('Click on episode tab to see episode ')
    def click_episodeTab(self):
        time.sleep(2)
        self.browser.find_element(*self.episodes_tab).click()

    @allure.step('Verify Image on cards of episode at episode level')
    def verify_episodeImg(self):
        time.sleep(2)
        return self.browser.find_element(*self.episode_img).is_displayed()

    @allure.step('Verify Episode number on cards of episode at episode level')
    def verify_episodeNumber(self):
        time.sleep(2)
        return self.browser.find_element(*self.episode_number).text

    @allure.step('Verify Episode Name on cards of episode at episode level')
    def verify_episodeName(self):
        time.sleep(2)
        return self.browser.find_element(*self.episode_name).is_displayed()

    @allure.step('Verify Episode Synopsis on cards of episode at episode level')
    def verify_episodeSynopsis(self):
        time.sleep(2)
        return self.browser.find_element(*self.episode_synopsis).is_displayed()

    @allure.step('Clicking on Episode 1 card to open detailed page for episode 1')
    def click_episode1card(self):
        time.sleep(2)
        self.browser.find_element(*self.episode_number).click()

    @allure.step('Verify Detailed page of episode 1 ')
    def verify_episode1Detailed(self):
        time.sleep(2)
        season = self.browser.find_element(*self.epiDetailed_img)
        self.browser.execute_script("arguments[0].scrollIntoView();", season)
        time.sleep(2)
        epi_1 = self.browser.find_element(*self.episode1_detailed).text
        print(epi_1)
        time.sleep(1)
        return epi_1

    @allure.step('Verify Episode should landscape image')
    def verify_detailed_episodeImage(self):
        time.sleep(2)
        return self.browser.find_element(*self.epiDetailed_img).is_displayed()

    @allure.step('Verify Episode should show play icon on image')
    def verify_episode_playIcon(self):
        time.sleep(2)
        return self.browser.find_element(*self.episode_playIcon).is_displayed()

    @allure.step('Clikcing on button play to  watch episode in popup')
    def click_episodePlayed(self):
        time.sleep(2)
        self.browser.find_element(*self.episode_playIcon).click()
        time.sleep(10)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(10)  # 60

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(10)

    @allure.step('Verify Trailer by Level on tv detailed page')
    def verify_trailerBylevel(self):
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.trailer_title))
        time.sleep(2)
        trailer = self.browser.find_element(*self.trailer_title)
        self.browser.execute_script("arguments[0].scrollIntoView();", trailer)
        time.sleep(3)
        return trailer.is_displayed()

    @allure.step('CLick on title overview link ')
    def click_titleOverview(self):
        time.sleep(2)
        title = self.browser.find_element(*self.title_overview)
        self.browser.execute_script("arguments[0].scrollIntoView();", title)
        time.sleep(2)
        title.click()

    @allure.step('Verify Photo title should be displayed by level on tv detailed page')
    def verify_photoBylevel(self):
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.photos_title))
        time.sleep(2)
        photo = self.browser.find_element(*self.photos_title)
        self.browser.execute_script("arguments[0].scrollIntoView();", photo)
        time.sleep(3)
        return photo.is_displayed()

    @allure.step('Click on check cox on telivision page')
    def clicking_checkbox(self):
        time.sleep(3)
        self.browser.find_element(*self.chkbox_forfooter).click()

    @allure.step('Verify Share button from popup')
    def verify_tvshareButton(self):
        time.sleep(2)
        try:
            return self.browser.find_element(*self.share_btn).is_displayed()
        except:
            return False








