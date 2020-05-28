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


class movieListingObj:
    movie_menu = (By.XPATH, "//ul[@class='menu-items']//a[@id='Movies']")
    header_title = (By.XPATH, "//h2[@class='banner-title']")
    header_search = (By.XPATH, "//input[@placeholder='Search Movie Title, Actor, or Genre']")
    header_background = (By.XPATH, "//img[@class='w-100 page-banner ng-star-inserted image-loaded']")
    filter_genre = (By.XPATH, "//div[contains(text(),'Genre')]")
    filter_rating = (By.XPATH, "//div[contains(text(),'rating')]")
    filter_year = (By.XPATH, "//div[@class='dropdown-text']")
    view_grid = (By.XPATH, "//div[@class='grid-icon grid']")
    view_grid1 = (By.XPATH, "//div[@class='gray-grid']")
    view_list = (By.XPATH, "//div[@class='list-icon list']")
    sorting_btn = (By.XPATH, "//div[@class='sort-filter']")
    results_found = (By.XPATH, "//h2[@class='count-text']")
    select_all = (By.XPATH, "//label[@class='select-txt ng-star-inserted']")
    title_cards = (By.XPATH, "//ul[@class='search-list ng-star-inserted']/li[1]//div[@class='desk-on']//div["
                             "@class='movie-detail']/p[1]")
    cards_checkbox = (By.XPATH, "//ul[@class='search-list ng-star-inserted']/li[1]//div["
                                "@class='checkbox-shell-dark']")
    search_click = (By.XPATH, "//div[@class='banner-text']//i[@class='fa-search']")
    search_cross = (By.XPATH, "//span[@class='clear-text ng-star-inserted']")
    all_titles = (By.XPATH, "//div[@class='desk-on']//div[@class='movie-detail']/p[1]")
    pagination_arrow = (By.XPATH, "//li[@class='pagination-next ng-star-inserted']//a[@class='ng-star-inserted']")
    action_genre = (By.XPATH, "//div[@class='desk-on']//div[@class='movie-detail']/span[1]")
    select_action = (By.XPATH, "//div[@class='filter-section ng-star-inserted']//span[text()='Action']")
    select_rating = (By.XPATH, "//div[@class='dropdown-default ng-star-inserted']/span[1]")
    select_multiRating = (By.XPATH, "//div[@class='dropdown-default ng-star-inserted']/span[text()='NC-17']")
    # clear_filter = (By.XPATH, "//span[@class='close-icon']")
    selected_rating = (By.XPATH, "//li[@class='tag ng-star-inserted']//span[contains(text(),'G')]")
    # selected_multirating = (By.XPATH, "//li[@class='tag ng-star-inserted']//span[contains(text(),'NC-17')]")
    selected_multirating = (By.XPATH, "//li[2]//span[contains(text(),'NC-17')]")
    cross_icon = (By.XPATH, "//ul[@class='tags-list ng-star-inserted']/li[1]/span[2]")
    selected_year = (By.XPATH, "//ul[@class='tags-list ng-star-inserted']/li[1]/span[1]")
    clear_all = (By.XPATH, "//span[contains(text(),'Clear All')]")
    left_slider = (By.XPATH, "//span[@class='ng5-slider-span ng5-slider-pointer ng5-slider-pointer-min']")
    submit_button = (By.XPATH, "//button[@class='slider-button']")
    combine_year = (By.XPATH, "//ul[@class='tags-list ng-star-inserted']/li[3]/span[1]")
    action_selected = (By.XPATH, "//li[@class='tag ng-star-inserted']//span[contains(text(),'Action')]")
    adventure_selected = (By.XPATH, "//li[@class='tag ng-star-inserted']//span[contains(text(),'Adventure')]")
    grid_chkbox1 = (By.XPATH, "//ul[@class='search-list ng-star-inserted']/li[1]//div[@class='checkbox-shell-dark']")
    grid_chkbox2 = (By.XPATH, "//ul[@class='search-list ng-star-inserted']/li[2]//div[@class='checkbox-shell-dark']")
    list_title = (By.XPATH, "//div[@class='col-lg-3 inner-container']")
    list_directedBy = (By.XPATH, "//div[@class='col-lg-2']")
    list_maincast = (By.XPATH, "//div[@class='col-lg-3']")
    list_synopsis = (By.XPATH, "//div[@class='col-lg-4']")
    select_option2genre = (By.XPATH, "//div[@class='filter-section ng-star-inserted']//span[4]")
    cardhover_option1 = (By.XPATH, "//li[1]//div[@class='desk-on']//button[contains(text(),'ADD TO LIST')]")
    cardhover_option2 = (By.XPATH, "//li[1]//div[@class='desk-on']//button[contains(text(),'Watch movie')]")
    cardhover_option3 = (By.XPATH, "//li[1]//div[@class='desk-on']//button[contains(text(),'Watch trailer')]")
    cardhover_option4 = (By.XPATH, "//li[1]//div[@class='desk-on']//button[contains(text(),'View details')]")
    popup_cross = (By.XPATH, "//div[@class='close tele-close']//img[@class='close-btn-image']")
    watch_popup = (By.XPATH, "//div[@id='bitmovin-player']")
    play_begining = (By.XPATH, "//button[@class='watch-again-btn btn-view']")
    alert = (By.XPATH, "//div[@class='atl-title-label uppercase']")
    list_name = (By.XPATH, "//span[contains(text(),'Automation List')]")
    add_button = (By.XPATH, "//button[@class='cui-btn cui-btn-primary cui-btn-o-1 addList']")
    success_created = (By.XPATH, "//div[@class='atl-add-btn']//span[@class='ie11fix uppercase']")
    viewlist_movie = (By.XPATH, "//p[@class='movieName']")
    # list_chbox1 = (By.XPATH, "//li[@class='totalField ng-star-inserted'][1]/div[1]/mgm-checkbox-single/div[1]")
    list_chbox1 = (By.XPATH, "//li[1]/div[1]/mgm-checkbox-single/div[1]")
    addTOlist = (By.XPATH, "//span[contains(text(),'ADD TO LIST')]")
    action_sel_filter = (By.XPATH, "//li[@class='tag ng-star-inserted']//span[contains(text(),'Action')]")
    download = (By.XPATH, "//button[span[contains(text(),'DOWNLOAD.CSV')]]")
    share_title = (By.XPATH, "//button[span[contains(text(),'SHARE TITLE')]]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click on Movie menu to open movie listing page')
    def open_moviePage(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.movie_menu))
        self.browser.find_element(*self.movie_menu).click()

    @allure.step('Verify Header title on movie listing page ')
    def verify_headerTitle(self):
        time.sleep(2)
        return self.browser.find_element(*self.header_title).text

    @allure.step('Verify Header search on movie listing page ')
    def verify_searchBox(self):
        return self.browser.find_element(*self.header_search).is_displayed()

    @allure.step('Verify Background image on movie listing page ')
    def verify_backImage(self):
        time.sleep(2)
        return self.browser.find_element(*self.header_background).is_displayed()

    @allure.step('Verify Filter Genre on movie listing page ')
    def verify_filterGenre(self):
        return self.browser.find_element(*self.filter_genre).is_displayed()

    @allure.step('Verify Filter Rating on movie listing page ')
    def verify_filterRating(self):
        return self.browser.find_element(*self.filter_rating).is_displayed()

    @allure.step('Verify Filter year on movie listing page')
    def verify_filterYear(self):
        return self.browser.find_element(*self.filter_year).is_displayed()

    @allure.step('Verify View Grid button on movie listing page ')
    def verify_viewGrid(self):
        return self.browser.find_element(*self.view_grid).is_displayed()

    @allure.step('Clicking on button -> View grid')
    def click_viewGrid(self):
        time.sleep(2)
        self.browser.find_element(*self.view_grid1).click()

    @allure.step('Verify View List button on movie listing page ')
    def verify_viewList(self):
        time.sleep(2)
        return self.browser.find_element(*self.view_list).is_displayed()

    @allure.step('Clicking on button -> view List')
    def click_viewList(self):
        time.sleep(2)
        self.browser.find_element(*self.view_list).click()

    @allure.step('Verify sorting button on movie listing gpage')
    def verify_sortingButton(self):
        return self.browser.find_element(*self.sorting_btn).is_displayed()

    @allure.step('Verify N result found on movie listing page ')
    def verify_resultsFound(self):
        time.sleep(1)
        result = self.browser.find_element(*self.results_found)
        self.browser.execute_script("arguments[0].scrollIntoView();", result)
        time.sleep(2)
        return self.browser.find_element(*self.results_found).text

    @allure.step('Verify select all checkbox on movie listing page ')
    def verify_selectAll(self):
        return self.browser.find_element(*self.select_all).text

    @allure.step('Verify Title Cards on movie listing page ')
    def verify_titleCards(self):
        time.sleep(2)
        return self.browser.find_element(*self.title_cards).is_displayed()

    @allure.step('Verify Checkbox corresponding to title cards on movie listing page')
    def verify_checkboxCards(self):
        time.sleep(2)
        return self.browser.find_element(*self.cards_checkbox).is_displayed()

    @allure.step('Enter search value in search box to find results ')
    def input_searchvalue(self, inpt):
        time.sleep(1)
        result = self.browser.find_element(*self.results_found)
        self.browser.execute_script("arguments[0].scrollIntoView();", result)
        time.sleep(2)
        self.browser.find_element(*self.header_search).send_keys(inpt)

    @allure.step('Click on search button to search ')
    def click_searchBtn(self):
        time.sleep(3)
        self.browser.find_element(*self.search_click).click()

    @allure.step('Verify search result is correct after searching')
    def verify_searchResult(self):
        time.sleep(2)
        return self.browser.find_element(*self.title_cards).text

    @allure.step('Click on cross button to clear search results ')
    def click_searchCross(self):
        time.sleep(1)
        result = self.browser.find_element(*self.results_found)
        self.browser.execute_script("arguments[0].scrollIntoView();", result)
        time.sleep(2)
        self.browser.find_element(*self.search_cross).click()

    @allure.step('Count total numbers of movie title in movie page ')
    def count_totalMovie(self):
        time.sleep(3)
        global count
        count = self.browser.find_elements(*self.all_titles)
        print(len(count))
        return len(count)

    @allure.step('pagination if movie is more than 42 ')
    def verify_Pagination(self):
        time.sleep(2)
        try:
            arrow = self.browser.find_element(*self.pagination_arrow)
            self.browser.execute_script("arguments[0].scrollIntoView();", arrow)
            time.sleep(2)
            return self.browser.find_element(*self.pagination_arrow).is_displayed()
        except:
            return False

    @allure.step('Pagination if movie is less than 42')
    def lessthan_42movies(self):
        return "There is less than 42 movies in list."

    @allure.step('CLick on genre dropdown to select ')
    def click_genreDropdown(self):
        time.sleep(2)
        self.browser.find_element(*self.filter_genre).click()
        time.sleep(2)
        return self.browser.find_element(*self.select_action).text

    @allure.step('CLick on genre dropdown to select multiples ')
    def click_multigenreDropdown(self):
        time.sleep(2)
        self.browser.find_element(*self.filter_genre).click()
        time.sleep(2)
        return self.browser.find_element(*self.select_option2genre).text

    @allure.step('Select 3rd  option in Genre dropdown ')
    def select_multignere(self):
        time.sleep(2)
        self.browser.find_element(*self.select_option2genre).click()

    @allure.step('Select Action option in Genre dropdown ')
    def select_Actiongnere(self):
        time.sleep(2)
        self.browser.find_element(*self.select_action).click()

    @allure.step('Verify selected genre showing above movie cards.')
    def verify_selecetdGenre(self):
        time.sleep(2)
        return self.browser.find_element(*self.action_selected).text

    @allure.step('Verify Multiple selected genre for genre filter ')
    def verify_muliselectedGenre(self):
        time.sleep(2)
        return self.browser.find_element(*self.adventure_selected).text

    @allure.step('Click on rating dropdown to select')
    def click_1ratingDropdown(self):
        time.sleep(2)
        self.browser.find_element(*self.filter_rating).click()
        time.sleep(2)
        return self.browser.find_element(*self.select_rating).text

    @allure.step('Select 1st rating showing in dropdown ')
    def select_1Dropdown(self):
        time.sleep(2)
        self.browser.find_element(*self.select_rating).click()

    @allure.step('Click on rating dropdown to select multiple')
    def click_2ratingDropdown(self):
        time.sleep(2)
        self.browser.find_element(*self.filter_rating).click()
        time.sleep(2)
        return self.browser.find_element(*self.select_multiRating).text

    @allure.step('Select 1st rating showing in dropdown ')
    def select_2Dropdown(self):
        time.sleep(2)
        self.browser.find_element(*self.select_multiRating).click()

    @allure.step('Verify selected dropdown is showing above movie cards with active filter')
    def verify_selSingle_rating(self):
        time.sleep(2)
        arrow = self.browser.find_element(*self.selected_rating)
        self.browser.execute_script("arguments[0].scrollIntoView();", arrow)
        time.sleep(2)
        return self.browser.find_element(*self.selected_rating).text

    @allure.step('Verify selected dropdown is showing above movie cards with active filter')
    def verify_selMulti_rating(self):
        time.sleep(2)
        return self.browser.find_element(*self.selected_multirating).text

    @allure.step('Click on cross icon to clear filter')
    def click_crossIcon(self):
        time.sleep(2)
        self.browser.find_element(*self.clear_all).click() #cross_icon

    @allure.step('Click on year dropdown filter to select')
    def click_yearDropdown(self):
        time.sleep(2)
        self.browser.find_element(*self.filter_year).click()

    @allure.step('Select year from slider to apply filter')
    def select_yearSlider(self):
        time.sleep(3)
        left = self.browser.find_element(*self.left_slider)
        self.browser.implicitly_wait(10)
        # Moving the left slider
        ActionChains(self.browser).click_and_hold(left).move_by_offset(80, 0).release().perform()

    @allure.step('click on submit button ')
    def click_submitButton(self):
        time.sleep(2)
        self.browser.find_element(*self.submit_button).click()

    @allure.step('Verify Year filter after selected from year dropdown')
    def verify_selectedYear(self):
        txt = self.browser.find_element(*self.selected_year)
        print(txt.text)
        return txt.is_displayed()

    @allure.step('Verify Year filter after selected from year dropdown with combination of genre , rating')
    def verify_selected_combineYear(self):
        txt = self.browser.find_element(*self.combine_year)
        print(txt.text)
        return txt.is_displayed()

    @allure.step('Verify Grid is selected using Checkbox corresponding to title cards on 1st movie ')
    def verify_gridchkbx1(self):
        time.sleep(2)
        try:
            return self.browser.find_element(*self.cards_checkbox).is_displayed()
        except:
            return False

    @allure.step('Verify Grid is selected using Checkbox corresponding to title cards on 2nd movie')
    def verify_gridchkbx2(self):
        time.sleep(2)
        try:
            return self.browser.find_element(*self.cards_checkbox).is_displayed()
        except:
            return False

    @allure.step('Verify title heading that shows after selecting list view ')
    def verify_lisTitle(self):
        time.sleep(2)
        return self.browser.find_element(*self.list_title).is_displayed()

    @allure.step('Verify Directed by heading should show after selecting list view ')
    def verify_directedBY(self):
        time.sleep(2)
        return self.browser.find_element(*self.list_directedBy).is_displayed()

    @allure.step('Verify Main cast heading should show after selecting list view ')
    def verify_mainCast(self):
        time.sleep(2)
        return self.browser.find_element(*self.list_maincast).is_displayed()

    @allure.step('Verify synopsis heading that shows after selecting list view ')
    def verify_listSynopsis(self):
        time.sleep(2)
        return self.browser.find_element(*self.list_synopsis).is_displayed()

    @allure.step('Verify movie cards hover button -> Add TO List')
    def verify_cardHover1(self):
        time.sleep(1)
        card1 = self.browser.find_element(*self.cardhover_option1)
        self.browser.execute_script("arguments[0].scrollIntoView();", card1)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(card1).perform()
        time.sleep(2)
        return card1.text

    @allure.step('Verify movie cards hover button -> Watch Movie')
    def verify_cardHover2(self):
        time.sleep(2)
        card2 = self.browser.find_element(*self.cardhover_option2)
        ActionChains(self.browser).move_to_element(card2).perform()
        time.sleep(2)
        return card2.text

    @allure.step('Verify movie cards hover button -> Watch Trailer')
    def verify_cardHover3(self):
        time.sleep(2)
        card3 = self.browser.find_element(*self.cardhover_option3)
        ActionChains(self.browser).move_to_element(card3).perform()
        time.sleep(2)
        return card3.text

    @allure.step('Verify movie cards hover button -> View Details')
    def verify_cardHover4(self):
        time.sleep(2)
        card4 = self.browser.find_element(*self.cardhover_option4)
        ActionChains(self.browser).move_to_element(card4).perform()
        time.sleep(2)
        return card4.text

    @allure.step('Click on watch movie option to play movie ')
    def click_watchmovie(self):
        time.sleep(2)
        card2 = self.browser.find_element(*self.cardhover_option2)
        ActionChains(self.browser).move_to_element(card2).perform()
        time.sleep(2)
        card2.click()
        time.sleep(13)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(10)

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(10)

    @allure.step('Click on watch trailer option to play trailer ')
    def click_watchtrailer(self):
        time.sleep(2)
        card3 = self.browser.find_element(*self.cardhover_option3)
        ActionChains(self.browser).move_to_element(card3).perform()
        time.sleep(2)
        card3.click()
        time.sleep(13)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(10)

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(10)

    @allure.step('Click on view details option to play trailer ')
    def click_viewDetails(self):
        time.sleep(2)
        card4 = self.browser.find_element(*self.cardhover_option4)
        ActionChains(self.browser).move_to_element(card4).perform()
        time.sleep(2)
        card4.click()
        time.sleep(17)

    @allure.step('Click on addToList option to play trailer ')
    def click_addtoList(self):
        time.sleep(2)
        card1 = self.browser.find_element(*self.cardhover_option1)
        ActionChains(self.browser).move_to_element(card1).perform()
        time.sleep(2)
        card1.click()
        time.sleep(17)

    @allure.step('Click on close icon to close popup')
    def click_closepopup(self):
        time.sleep(2)
        self.browser.find_element(*self.popup_cross).click()

    @allure.step('Verify pop up for watch trailer is opening ')
    def verify_watch_popup(self):
        time.sleep(2)
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.popup_cross))
        styl = self.browser.find_element(*self.watch_popup).get_attribute('style')
        print(styl)
        return styl

    @allure.step('Verify Page title ')
    def verify_pagetitle(self):
        time.sleep(2)
        title = self.browser.title
        print(title)
        return title

    def refresh(self):
        time.sleep(2)
        self.browser.refresh()

    @allure.step('Verify Alert that consist success message ')
    def verifyAlert(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10, ignored_exceptions).until(EC.presence_of_element_located(self.alert))
        alert = self.browser.find_element(*self.alert).text
        print(alert)
        return alert

    @allure.step('Click on list name to add movie into list')
    def click_listToadd(self):
        time.sleep(2)
        self.browser.find_element(*self.list_name).click()

    @allure.step('click on add to list button to add movie ')
    def click_Addlist_button(self):
        time.sleep(2)
        self.browser.find_element(*self.add_button).click()

    @allure.step('Verify success message after clicking on addTo list button ')
    def verify_success_msg(self):
        # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.success_created)) #ignored_exceptions
        return self.browser.find_element(*self.success_created).is_displayed()

    @allure.step('Verify movie name showing in list view ')
    def verify_movieName(self):
        time.sleep(2)
        return self.browser.find_element(*self.viewlist_movie).text

    @allure.step('click list movie name to redirected on detailed pag')
    def click_listMoviename(self):
        time.sleep(2)
        self.browser.find_element(*self.viewlist_movie).click()

    @allure.step('Click on list check box 1 to verify footer')
    def click_listchkbox1(self):
        time.sleep(2)
        chkbox1 = self.browser.find_element(*self.list_chbox1)
        self.browser.execute_script("arguments[0].scrollIntoView();", chkbox1)
        time.sleep(2)
        chkbox1.click()

    @allure.step('Verify add to list button  displayed in footer')
    def verify_addTolist(self):
        # time.sleep(2)
        return self.browser.find_element(*self.addTOlist).is_displayed()

    @allure.step('Verify add to list button  displayed in footer')
    def verify_shareTitle(self):
        # time.sleep(2)
        return self.browser.find_element(*self.share_title).is_displayed()

    @allure.step('Verify download.csv button  displayed in footer')
    def verify_downloadCSV(self):
        # time.sleep(2)
        return self.browser.find_element(*self.download).is_displayed()

    @allure.step('click Add to List tab in footer popup')
    def click_footer_addList(self):
        time.sleep(1)
        return self.browser.find_element(*self.addTOlist).click()

    @allure.step('Verify Search results is relevant with using genre filter ')
    def verify_genrefilter_results(self):
        time.sleep(3)
        return self.browser.find_element(*self.action_sel_filter).is_displayed()
        # action = []
        # action = self.browser.find_elements(*self.action_genre)
        # time.sleep(2)
        # print(action[1].text)
        # time.sleep(1)
        # print(str(action.text))
        # d = "Action,"
        # time.sleep(2)
        # for aaa in action:
        #     if all(x in d for x in action.text):
        #         return True
        # else:
        #     return False


