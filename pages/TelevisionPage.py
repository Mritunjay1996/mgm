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




class Telvision:
    URL = "https://mgm-roar-dev.practicallogix.com/"
    header_title = (By.XPATH, "//div[@class='banner-text']/h2")
    header_image = (By.XPATH, "//div[@class='header']/div/img")
    header_searchbox = (By.XPATH, "//div[@class='banner-text']/div/input")
    filter_genre = (By.XPATH, "//div[text()=' Genre ']")
    filter_rating = (By.XPATH, "//div[text()=' rating ']")
    filter_year = (By.XPATH, "//div[text()='Year']")
    grid = (By.XPATH, "//div[@class='gray-grid']")
    view_button_grid = (By.XPATH, "//div[@class='white-grid']")
    view_button_list = (By.XPATH, "//div/i[@class='material-icons']")
    sort_button = (By.XPATH, "//div[@class='sort-filter']")
    count_text = (By.XPATH, "//div/h2[@class='count-text']")
    select_all_checkbox = (By.XPATH, "//label[text()='Select All']/parent::mgm-checkbox-selectall/div")
    title_card_checkbox = (By.XPATH, "//div[@class='checkbox-shell-dark']")
    title_card_checkbox1 = (By.XPATH, "(//div[@class='checkbox-shell-dark'])[2]")
    header_television = (By.XPATH, "//ul[@class='menu-items']//a[text()='Television']")
    search_button = (By.XPATH, "//div[@class='banner-text']//button[@class='search-btn']/i")
    search_list_section = (By.XPATH, "//div[@class='search-list-section']")
    searched_movie_fargo = (By.XPATH, "//p[text()=' Fargo ']")
    movie_teen_wolf = (By.XPATH, "//p[text()=' Teen Wolf ']")
    genre_action = (By.XPATH, "//div[text()=' Genre ']/parent::div/div[2]/span[text()='Action']")
    verify_genre_action = (By.XPATH, "//li/span[text()='Action']")
    genre_crime = (By.XPATH, "//div[text()=' Genre ']/parent::div/div[2]/span[text()='Crime']")
    verify_genre_crime = (By.XPATH, "//li/span[text()='Crime']")
    genre_drama = (By.XPATH, "//div[text()=' Genre ']/parent::div/div[2]/span[text()='Drama']")
    verify_genre_drama = (By.XPATH, "//li/span[text()='Drama']")
    movie_vikings = (By.XPATH, "//p[text()=' Vikings (series) ']")
    rating_tv14 = (By.XPATH, "//div[text()=' rating ']/parent::div/div[2]/span[text()='TV-14']")
    verify_rating_tv14 = (By.XPATH, "//li/span[text()='TV-14']")
    clear_filter = (By.XPATH, "//li[@class='clear-filter']/span")
    rating_NA = (By.XPATH, "//div[text()=' rating ']/parent::div/div[2]/span[text()='TV-PG']")
    verify_rating_pg = (By.XPATH, "//li/span[text()='TV-PG']")
    movie_mr_mom = (By.XPATH, "//p[text()=' Mr. Mom ']")
    movie_mr_mom_series = (By.XPATH, "//p[text()=' Mr. Mom (series) ']")
    slider_left_button = (By.XPATH, "(//div[@class='slider']//span[@role='slider'])[1]")
    slider_right_button = (By.XPATH, "(//div[@class='slider']//span[@role='slider'])[2]")
    slider_submit_button = (By.XPATH, "//button[@class='slider-button']")
    clear_search = (By.XPATH, "//button[@class='search-btn']/span")
    Mr_Mom_add_to_list_button = (By.XPATH, "//div[@class='button-hover']//button[text()='ADD TO LIST']")
    Mr_Mom_watch_trailer_button = (By.XPATH, "//div[@class='button-hover']//button[text()='Watch trailer']")
    Mr_Mom_view_detail_button = (By.XPATH, "//div[@class='button-hover']//button[text()='View details']")
    player_popup = (By.XPATH, "//div[@id='bitmovin-player']")
    player_popup1 = (By.XPATH, "//div[@class='player-container']")
    movie_close_btn = (By.XPATH, "//mgm-video-player-popup//img[@class='close-btn-image']")
    Demo = (By.XPATH, "//a[text()='Demo']")
    spectre = (By.XPATH, "//p[text()=' Spectre ']")
    synopsis_mr_mom = (By.XPATH, "//p[@class='synopsis-title ng-star-inserted']")
    add_to_list_added_button = (By.XPATH, "//div[@class='atl-add-btn']//span[text()=' Added! ']")
    list_view_title = (By.XPATH, "//div[@class='search-list-section']//div[text()='Title']")
    list_view_directed_by = (By.XPATH, "//div[@class='search-list-section']//div[text()='Directed By']")
    list_view_main_cast = (By.XPATH, "//div[@class='search-list-section']//div[text()='Main Cast']")
    list_view_synopsis = (By.XPATH, "//div[@class='search-list-section']//div[text()='Synopsis']")
    cards_checkbox = (By.XPATH, "//ul[@class='search-list ng-star-inserted']/li[1]//div[@class='checkbox-shell-dark']")
    title_name = (By.XPATH, "//div[@class='title-card-list ng-star-inserted']//p")
    checked_list_popup = (By.XPATH, "//div[@class='item-list']/parent::div")
    checked_list_popup_number_selected_list = (By.XPATH, "//div[@class='item-list']//span")
    checked_list_popup_download_csv = (By.XPATH, "//div[@class='item-list']//span[text()='DOWNLOAD.CSV']")
    checked_list_popup_share_list_button = (By.XPATH, "//div[@class='item-list']//span[text()='SHARE LIST']")
    popup_share_title_button = (By.XPATH, "//span[contains(text(),'SHARE TITLE')]")
    checked_list_popup_add_to_list_button = (By.XPATH, "//div[@class='item-list']//span[text()='ADD TO LIST']")
    verify_year = (By.XPATH, "//li/span[text()='2020 - 2020']")
    logo_img = (By.XPATH, "//a[@class='logo-img']//img")


    def __init__(self, browser):
        self.browser = browser
        #self.browser = WebDriver
        global actionchains
        actionchains = ActionChains(self.browser)
        
    @allure.step('Verify header title is displayed')
    def HeaderTitle(self):
        return self.browser.find_element(*self.header_title).is_displayed()

    @allure.step('Verify header image is displayed')
    def HeaderImage(self):
        return self.browser.find_element(*self.header_image).is_displayed()

    @allure.step('Verify header search box is displayed')
    def HeaderSearchbox(self):
        return self.browser.find_element(*self.header_searchbox).is_displayed()

    @allure.step('Verify filter genre is displayed')
    def FilterGenre(self):
        return self.browser.find_element(*self.filter_genre).is_displayed()

    @allure.step('Verify filter rating is displayed')
    def FilterRatig(self):
        return self.browser.find_element(*self.filter_rating).is_displayed()

    @allure.step('Verify filter year is displayed')
    def FilterYear(self):
        return self.browser.find_element(*self.filter_year).is_displayed()

    @allure.step('Verify view button grid is displayed')
    def ViewButtonGrid(self):
        return self.browser.find_element(*self.view_button_grid).is_displayed()

    @allure.step('Verify View button list is displayed')
    def ViewButtonList(self):
        return self.browser.find_element(*self.view_button_list).is_displayed()

    @allure.step('Verify Sort button is displayed')
    def SortButton(self):
        return self.browser.find_element(*self.sort_button).is_displayed()

    @allure.step('Verify Select all checkbox is displayed')
    def SelectAllCheckbox(self):
        return self.browser.find_element(*self.select_all_checkbox).is_displayed()

    @allure.step('Verify title cards checkbox is displayed')
    def TitleCardsCheckBox(self):
        return self.browser.find_element(*self.title_card_checkbox).is_displayed()

    @allure.step('Click television')
    def ClickTelevisionHeader(self):
        self.browser.find_element(*self.header_television).click()

    @allure.step('Enter television name in search box')
    def SearchTelevisionShow(self, showname):
        self.browser.find_element(*self.header_searchbox).send_keys(showname)

    @allure.step('Click search button')
    def ClickSearchButton(self):
        self.browser.find_element(*self.search_button).click()

    @allure.step('Verify searched list section is displayed')
    def SearchListSection(self):
        time.sleep(3)
        return self.browser.find_element(*self.search_list_section).is_displayed()

    @allure.step('Verify correct searched television show is displayed')
    def SearchedTelevisionShow(self):
        return self.browser.find_element(*self.searched_movie_fargo).is_displayed()

    @allure.step('Click filter genre')
    def ClickGenre(self):
        self.browser.find_element(*self.filter_genre).click()

    @allure.step('Click genre action')
    def ClickGenreAction(self):
        self.browser.find_element(*self.genre_action).click()

    @allure.step('Verify action movies')
    def MovieVikings(self):
        return self.browser.find_element(*self.movie_vikings).is_displayed()

    @allure.step('Click filter rating')
    def ClickFilterRating(self):
        self.browser.find_element(*self.filter_rating).click()
        
    @allure.step('Click rating 14')
    def ClickRating14(self):
        self.browser.find_element(*self.rating_tv14).click()
        
    @allure.step('Click clear filter')
    def ClickClearFilter(self):
        self.browser.find_element(*self.clear_filter).click()

    @allure.step('Click rating NA')
    def ClickRatingNA(self):
        self.browser.find_element(*self.rating_NA).click()

    @allure.step('Verify movie MR Mom is displayed')
    def MovieMrMom(self):
        return self.browser.find_element(*self.movie_mr_mom).is_displayed()

    @allure.step('Click filter year')
    def ClickFilterYear(self):
        self.browser.find_element(*self.filter_year).click()

    @allure.step('Select year from slider')
    def ClickSelectYear(self):
        drag = self.browser.find_element(*self.slider_left_button)
        drop = self.browser.find_element(*self.slider_right_button)
        actionchains = ActionChains(self.browser)
        actionchains.drag_and_drop(drag, drop).perform()

    @allure.step('Click Slider submit button')
    def ClickSliderSubmitButton(self):
        time.sleep(5)
        self.browser.find_element(*self.slider_submit_button).click()

    @allure.title('Click genre Crime')
    def ClickGenreCrime(self):
        self.browser.find_element(*self.genre_crime).click()

    @allure.title('Click genre Drama')
    def ClickGenreDrama(self):
        self.browser.find_element(*self.genre_drama).click()

    @allure.step('Verify movie Teen Wolf is displayed')
    def MovieTeenWolf(self):
        return self.browser.find_element(*self.movie_teen_wolf).is_displayed()

    @allure.step('Click clear search button')
    def ClearSearch(self):
        self.browser.find_element(*self.clear_search).click()

    @allure.step('Verify Movie card add to list button is displayed')
    def MovieCardHoverAddToList(self):
        btn = self.browser.find_element(*self.Mr_Mom_add_to_list_button)
        btn.location_once_scrolled_into_view
        actionchains.move_to_element(btn).perform()
        return btn.is_displayed()

    @allure.step('Verify Movie card View Details button is displayed')
    def MovieCardHoverViewDetails(self):
        return self.browser.find_element(*self.Mr_Mom_view_detail_button).is_displayed()

    @allure.step('Verify Movie card Watch Trailer button is displayed')
    def MovieCardHoverWatchTrailer(self):
        return self.browser.find_element(*self.Mr_Mom_watch_trailer_button).is_displayed()

    @allure.step('Click Watch Trailer button')
    def ClickWatchTrailer(self):
        self.browser.find_element(*self.Mr_Mom_watch_trailer_button).click()

    @allure.step('Verify Player Pop Up is displayed')
    def PlayerPopUp(self):
        time.sleep(15)
        popup = self.browser.find_element(*self.player_popup1).is_displayed()
        time.sleep(3)
        self.browser.find_element(*self.movie_close_btn).click()
        return popup

    @allure.step('Click View Details Button')
    def ClickViewDetailsButton(self):
        self.browser.find_element(*self.Mr_Mom_view_detail_button).click()

    @allure.step('Vrify Movie is displayed')
    def VerifyMrMomSynopsis(self):
        movie = self.browser.find_element(*self.synopsis_mr_mom)
        movie.location_once_scrolled_into_view
        time.sleep(7)
        return movie.is_displayed()

    @allure.step('Click Add to list')
    def ClickAddToList(self):
        self.browser.find_element(*self.Mr_Mom_add_to_list_button).click()

    @allure.step('Verify add to list added button is displayed')
    def AddToListAddedButton(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.add_to_list_added_button))
        return self.browser.find_element(*self.add_to_list_added_button).is_displayed()

    @allure.step('Click list view button')
    def ClickListViewButton(self):
        self.browser.find_element(*self.view_button_list).click()

    @allure.step('Verify title is displayed')
    def Title(self):
        title = self.browser.find_element(*self.list_view_title)
        #actionchains.move_to_element(title).perform()
        self.browser.execute_script("arguments[0].scrollIntoView();", title)
        return title.is_displayed()

    @allure.step('Verify Directed by is displayed')
    def DirectedBy(self):
        return self.browser.find_element(*self.list_view_directed_by).is_displayed()

    @allure.step('Verify main cast is displayed')
    def MainCast(self):
        return self.browser.find_element(*self.list_view_main_cast).is_displayed()
    
    @allure.step('Verify synopsis is displayed')
    def Synopsis(self):
        return self.browser.find_element(*self.list_view_synopsis).is_displayed()

    def ClickGridViewButton(self):
        self.browser.find_element(*self.grid).click()
        
    def CardsCheckbox(self):
        return self.browser.find_element(*self.cards_checkbox).is_displayed()

    def ClickTitleName(self):
        self.browser.find_element(*self.title_name).click()

    def ClickTitleCardCheckbox(self):
        self.browser.find_element(*self.title_card_checkbox1).click()

    @allure.step('Verify Check list Pop-Up is visible')
    def CheckedListPopUp(self):
        return self.browser.find_element(*self.checked_list_popup).is_displayed()

    @allure.step('Verify Numbers of list selected')
    def CheckedListPopUpSelectedList(self):
        return self.browser.find_element(*self.checked_list_popup_number_selected_list).is_displayed()

    @allure.step('Verify Downloadd Csv button visible')
    def CheckedListPopUpDownloadCsv(self):
        return self.browser.find_element(*self.checked_list_popup_download_csv).is_displayed()

    @allure.step('Verify Share Button Visible')
    def CheckedListPopUpShareButton(self):
        return self.browser.find_element(*self.checked_list_popup_share_list_button).is_displayed()

    @allure.step('Verify share list is displayed')
    def verify_sharetitleFooter(self):
        time.sleep(2)
        return self.browser.find_element(*self.popup_share_title_button).is_displayed()

    @allure.step('Verify Add to list Button Visible')
    def CheckedListPopUpAddToListButton(self):
        return self.browser.find_element(*self.checked_list_popup_add_to_list_button).is_displayed()

    def VerifyRating(self):
        return self.browser.find_element(*self.verify_rating_pg).is_displayed()

    def VerifyGenreDrama(self):
        return self.browser.find_element(*self.verify_genre_drama).is_displayed()

    def VerifyRatingTv14(self):
        return self.browser.find_element(*self.verify_rating_tv14).is_displayed()

    def VerifyYear(self):
        return self.browser.find_element(*self.verify_year).is_displayed()

    def VerifyGenreAction(self):
        return self.browser.find_element(*self.verify_genre_action).is_displayed()

    def VerifyGenreCrime(self):
        return self.browser.find_element(*self.verify_genre_crime).is_displayed()

    def connection_testcases(self):
        self.browser.get(self.URL)
        time.sleep(30)

        # time.sleep(2)
        # self.browser.refresh()
        # time.sleep(20)
        # self.browser.find_element(*self.logo_img).click()
        # time.sleep(10)
        # self.browser.refresh()
        # time.sleep(30)

