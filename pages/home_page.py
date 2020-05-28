import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *


class homePageObj:
    URL = "https://mgm-roar-dev.practicallogix.com/"
    recently_watched = (By.XPATH, "//h2[contains(text(),'Recently Watched')]")
    # title_text = (By.XPATH, "//div[@class='movie-detail']/p[1]")
    title_text = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div[3]/following-sibling::div//ul["
                            "@class='movies-list d-flex active']/li[1]//mgm-movie-poster[1]//div[1]//div[1]//div["
                            "3]//p[1]")
    play_nextMoviname = (By.XPATH, "//h2[contains(text(),'Action / Adventure')]/parent::div/parent::div/parent::div"
                                   "/following-sibling::div//ul[@class='movies-list d-flex active']/li[3]//div["
                                   "@class='desk-on']//div[3]/p[1]")
    # movie_cards = (By.XPATH, "//div[@class='home']/mgm-block-picker[2]/mgm-movies-block[1]/div[1]["
    #                          "@class='movies-block-container dark_background']")
    movie_cards = (By.XPATH, "//div[@class='home']/mgm-block-picker[2]/mgm-movies-block[1]//div["
                             "@class='movie-poster']//div[@class='movie-poster-alias']/img")
    recent_watchedScroll = (By.XPATH, "//div[@class='card-section']/ng-scrollbar/div[1]/div["
                                      "1]/following-sibling::scrollbar-x[1]")
    # next_arrow = (By.XPATH, "//mgm-block-picker[2]/mgm-movies-block[1]/div[1]/div[2]/mgm-navigation-arrows[1]/div["
    #                         "1]/a[1]/i[1]")
    next_arrow = (By.XPATH, "//h2[text()='Recently Watched']/ancestor::div[3]/following-sibling::div//i["
                            "@class='next-icon icon']")
    prev_arrow = (By.XPATH, "//div[@class='navigation-arrow']/a/i[@class='previous-icon icon']")
    action_adventure = (By.XPATH, "//h2[contains(text(),'Action / Adventure')]")
    watch_movie = (By.XPATH, "//h2[contains(text(),'Action / Adventure')]/parent::div/parent::div/parent::div"
                             "/following-sibling::div//ul[@class='movies-list d-flex active']/li[2]//button[contains("
                             "text(),'Watch movie')]")
    # watch_movie = (By.XPATH, "//h2[contains(text(),'Action / Adventure')]/parent::div/parent::div/parent::div"
    #                          "/following-sibling::div//ul[@class='movies-list d-flex ng-star-inserted active']/li["
    #                          "2]//button[contains(text(),'Watch movie')]")
    watchmovie_name = (By.XPATH, "//h2[contains(text(),'Action / Adventure')]/parent::div/parent::div/parent::div"
                                 "/following-sibling::div//ul[@class='movies-list d-flex active']/li[2]//div["
                                 "@class='desk-on']//div[3]/p[1]")
    close_button = (By.XPATH, "//div[@class='close tele-close']//img[@class='close-btn-image']")
    play_begining = (By.XPATH, "//button[@class='watch-again-btn btn-view']")
    # poster_image = (By.XPATH, "//div//img[@class='image-loaded']")
    poster_image = (By.XPATH, "//div[@class='movies-block-container dark_background']//ul[@class='movies-list d-flex "
                              "active']//li[1]//mgm-movie-poster[1]//div[1]//div[1]//div[1]//div[1]")
    movie_generes = (By.XPATH, "//div[@class='home']/mgm-block-picker[2]/mgm-movies-block[1]//li[1]//div["
                               "@class='movie']/following-sibling::div[2]/span[1]")
    cardhover_option1 = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div["
                                   "3]/following-sibling::div//ul[@class='movies-list d-flex active']/li[1]//button["
                                   "contains(text(),'ADD TO LIST')]")
    cardhover_option2 = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div["
                                   "3]/following-sibling::div//ul[@class='movies-list d-flex active']/li[1]//button["
                                   "contains(text(),'Watch movie')]")
    cardhover_option3 = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div["
                                   "3]/following-sibling::div//ul[@class='movies-list d-flex active']/li[1]//button["
                                   "contains(text(),'Watch trailer')]")
    cardhover_option4 = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div["
                                   "3]/following-sibling::div//ul[@class='movies-list d-flex active']/li[1]//button["
                                   "contains(text(),'View details')]")
    alert = (By.XPATH, "//div[@class='atl-title-label uppercase']")
    watch_popup = (By.XPATH, "//div[@id='bitmovin-player']")
    mgm_img = (By.XPATH, "//a[@class='logo-img']//img")
    movie_added = (By.XPATH, "//h2[contains(text(),'Oscar-winning "
                             "Films')]/parent::div/parent::div/parent::div/following-sibling::div//ul["
                             "@class='movies-list d-flex active']/li[1]//button[contains(text(),'ADD TO LIST')]")
    # myList_seeall = (By.XPATH, "//a[contains(text(),'SEE ALL')]")
    myList_seeall = (By.XPATH, "//a[contains(text(),'SEE LISTS')]")
    automation_mylist = (By.XPATH, "//a[contains(text(),'Automation List')]")
    # delete_btn = (By.XPATH, "//button[contains(text(),'DELETE')]")
    delete_btn = (By.XPATH, "//span[contains(text(),'DELETE')]")
    mylist_tab = (By.XPATH, "//ul[@class='menu-items']//a[@id='My Lists']")
    autoRand_list = (By.XPATH, "//a[contains(text(),'" + new_List_name + "')]")
    delete_permission = (By.XPATH, "//button[@class='cui-btn cui-btn-primary ng-star-inserted']")
    # footer
    privacy_policy = (By.XPATH, "//a[contains(text(),'Privacy Policy')]")
    terms_use = (By.XPATH, "//a[contains(text(),'Terms of use')]")
    footer_logo = (By.XPATH, "//img[@class='d-none d-md-inline']")
    support = (By.XPATH, "//a[@class='support-link']")
    address = (By.XPATH, "//span[@class='contact-address']")
    youtube_icon = (By.XPATH, "//div[@class='inner-container']//i[@class='icon YouTube']")
    fb_icon = (By.XPATH, "//div[@class='inner-container']//i[@class='icon FaceBook']")
    twitter_icon = (By.XPATH, "//div[@class='inner-container']//i[@class='icon Twitter']")
    insta_icon = (By.XPATH, "//div[@class='inner-container']//i[@class='icon Instagram']")
    copyright = (By.XPATH, "//div[@class='col-md-12 copy-right']//p[1]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify Recently watched Heading is displayed ')
    def verify_recentlywatched(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.recently_watched))
        recently = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        return self.browser.find_element(*self.recently_watched).text

    @allure.step('Verify Title text of movie in recently watched ')
    def verify_titleText(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.title_text))
        first = self.browser.find_element(*self.title_text)  # Title 1
        print(first.text)
        ActionChains(self.browser).move_to_element(first).perform()
        time.sleep(2)
        return first.is_displayed()

    @allure.step('Verify movie cards in recently watched ')
    def verify_moviecards(self):
        # return self.browser.find_element(*self.movie_cards).get_attribute("hover-class")
        return self.browser.find_element(*self.poster_image).is_displayed()

    @allure.step('Verify horizontal watched scroll in recently watched ')
    def verify_scroll(self):
        scroll = self.browser.find_elements(*self.recent_watchedScroll)
        return scroll[1].is_displayed()

    @allure.step('Verify Right navigation arrow is displayed in recently watched')
    def verify_rightarrow(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.recently_watched))
        recently = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        right_nav = self.browser.find_element(*self.next_arrow)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(right_nav).perform()
        return right_nav.is_displayed()

    @allure.step('click on Right navigation arrow in recently watched')
    def click_rightarrow(self):
        time.sleep(2)
        self.browser.find_element(*self.next_arrow).click()

    @allure.step('Verify Left navigation arrow is displayed in recently watched')
    def verify_leftarrow(self):
        left_nav = self.browser.find_element(*self.prev_arrow)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(left_nav).perform()
        return left_nav.is_displayed()

    @allure.step('click on Left navigation arrow in recently watched')
    def click_prevarrow(self):
        # time.sleep(3)
        # self.browser.find_element(*self.prev_arrow).click()
        prev = self.browser.find_element(*self.prev_arrow)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(prev).click(prev).perform()

    @allure.step('Click on watch movie from Action /Adventure cards ')
    def click_watchmovie(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.action_adventure))
        adventures = self.browser.find_element(*self.action_adventure)
        self.browser.execute_script("arguments[0].scrollIntoView();", adventures)
        time.sleep(5)
        watch = self.browser.find_element(*self.watch_movie)
        ActionChains(self.browser).move_to_element(watch).perform()
        time.sleep(3)
        watch.click()
        time.sleep(13)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(20)  # 60

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(15)  # 60

    @allure.step('get the movie name, which you are going to play.')
    def play_moviename(self):
        global movie_name
        movie_name = self.browser.find_element(*self.watchmovie_name).text
        # print(movie_name)
        return movie_name

    @allure.step('CLick on close image to close movie')
    def click_crossimg(self):
        self.browser.find_element(*self.close_button).click()

    @allure.step('Get the movie name that has been added in recently watched playlist ')
    def recent_moviename(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.recently_watched))
        global recent_movie
        recently = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        time.sleep(3)
        first = self.browser.find_element(*self.title_text)  # title 1
        print(first.text)
        time.sleep(1)
        recent_movie = first.text
        return recent_movie

    @allure.step('Get the 2nd Movie name in recently watched section')
    def play_2movieCard_name(self):
        time.sleep(2)
        second = self.browser.find_element(*self.play_nextMoviname)  # title 2
        print(second.text)
        time.sleep(1)
        recent_movie = second.text
        return recent_movie

    def RecentlyWatchedPosterImage(self):
        image = self.browser.find_element(*self.poster_image)
        image.location_once_scrolled_into_view
        a = image.is_displayed()
        return a

    @allure.step('Movie Title Element')
    def verifyMovieTitle(self):
        first = self.browser.find_element(*self.title_text)  # title 1
        print(first.text)
        return first.text

    @allure.step('Movie Genre Element')
    def MovieGenre(self):
        return self.browser.find_element(*self.movie_generes).text

    @allure.step('Verify Add to List option in recently watched movie card')
    def addTolist(self):
        time.sleep(1)
        card1 = self.browser.find_element(*self.cardhover_option1)
        ActionChains(self.browser).move_to_element(card1).perform()
        return self.browser.find_element(*self.cardhover_option1).text

    @allure.step('Verify Watch movie option in recently watched movie card')
    def watchMoviesoption(self):
        time.sleep(1)
        card2 = self.browser.find_element(*self.cardhover_option2)
        ActionChains(self.browser).move_to_element(card2).perform()
        return self.browser.find_element(*self.cardhover_option2).text

    @allure.step('Verify Watch Trailer option in recently watched movie card')
    def watchTraileroption(self):
        time.sleep(1)
        card3 = self.browser.find_element(*self.cardhover_option3)
        ActionChains(self.browser).move_to_element(card3).perform()
        return self.browser.find_element(*self.cardhover_option3).text

    @allure.step('Verify View Details option in recently watched movie card')
    def viewDetailsoption(self):
        time.sleep(1)
        card4 = self.browser.find_element(*self.cardhover_option4)
        ActionChains(self.browser).move_to_element(card4).perform()
        return self.browser.find_element(*self.cardhover_option4).text

    @allure.step('Click on add to List ')
    def click_addList(self):
        time.sleep(2)
        self.browser.find_element(*self.cardhover_option1).click()

    @allure.step('Verify Alert that consist success message ')
    def verifyAlert(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10, ignored_exceptions).until(EC.presence_of_element_located(self.alert))
        alert = self.browser.find_element(*self.alert).text
        print(alert)
        return alert

    @allure.step('Clicking button in recently watched on cards hover -> watch movie ')
    def click_recwatch_movie(self):
        time.sleep(2)
        self.browser.find_element(*self.recently_watched).click()
        time.sleep(2)
        card2 = self.browser.find_element(*self.cardhover_option2)
        ActionChains(self.browser).move_to_element(card2).perform()
        time.sleep(3)
        card2.click()
        time.sleep(13)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(7)  # 60

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(7)  # 60

    @allure.step('Choose and click in Resume watching and Playt from begining')
    def choose_click(self):
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(30)

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(30)

    @allure.step('Verify pop up for watch trailer is opening ')
    def watch_movie_popup(self):
        time.sleep(2)
        styl = self.browser.find_element(*self.watch_popup).get_attribute('style')
        print(styl)
        return styl

    @allure.step('CLick on View Details button ')
    def click_viewdetails(self):
        time.sleep(3)
        card4 = self.browser.find_element(*self.cardhover_option4)
        ActionChains(self.browser).move_to_element(card4).perform()
        time.sleep(3)
        card4.click()

    @allure.step('Verify Page title ')
    def verify_pagetitle(self):
        time.sleep(2)
        title = self.browser.title
        print(title)
        return title

    @allure.step('Click on image button of MGM image')
    def click_mgmimg(self):
        self.browser.get(self.URL)
        time.sleep(30)
        # time.sleep(5)
        # self.browser.refresh()
        # time.sleep(30)
        # self.browser.find_element(*self.mgm_img).click()

    @allure.step('Click on watch trailer button in hover of cards ')
    def click_recwatch_trailer(self):
        time.sleep(2)
        self.browser.find_element(*self.recently_watched).click()
        time.sleep(2)
        card3 = self.browser.find_element(*self.cardhover_option3)
        ActionChains(self.browser).move_to_element(card3).perform()
        time.sleep(3)
        card3.click()
        time.sleep(13)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(10)  # 60

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(15)  # 60

    @allure.step('Click on watch trailer button in hover of cards ')
    def watchrecwatch_trailer(self):
        styl = self.browser.find_element(*self.watch_movie_popup).get_attribute('style')
        print(styl)
        return styl

    @allure.step('Verify on click right navigation arrow the 1st movie card is displayed ')
    def verify_1card_slide(self):
        first = self.browser.find_element(*self.title_text)  # title 1
        print(first.text)
        time.sleep(1)
        return first.is_displayed()

    @allure.step('Click Second Right nav arrow ')
    def click_secnav_arrow(self):
        try:
            condition = self.browser.find_element(*self.next_arrow)  # sec_next_arrow
            time.sleep(1)
            condition1 = condition.is_displayed()
        except:
            condition1 = False

        if condition1 == True:
            time.sleep(2)
            right_nav = self.browser.find_element(*self.next_arrow)  # sec_next_arrow
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(right_nav).click(right_nav).perform()

    @allure.step('Verify Right nav arrow got disabled when we are on last ')
    def verify_right_disbaled(self):
        try:
            isPresent = self.browser.find_element(*self.next_arrow).is_displayed()  # third_next_arrow
            if isPresent:
                return True

        except:
            return False

    @allure.step('Verify Left nav arrow got disabled when we are on first ')
    def verify_left_disbaled(self):
        try:
            isPresent = self.browser.find_element(*self.prev_arrow).is_displayed()
            if isPresent:
                return True

        except:
            return False

    @allure.step('CLick on Automaion List to veriy movie added ')
    def clickAutomationlist(self):
        time.sleep(2)
        self.browser.find_element(*self.myList_seeall).click()
        time.sleep(5)
        self.browser.find_element(*self.automation_mylist).click()

    @allure.step('Verify Movie is added in Automaion List  ')
    def verifyMovie_list(self, movie):
        time.sleep(17)
        movie_name = self.browser.find_element_by_xpath(
            "//div[@class='desk-on']//p[@class='movie-title light-color'][contains(text(),'" + str(movie) + "')]")
        return movie_name.text

    @allure.step('Delete movie from list')
    def delete_movie(self, movie):
        time.sleep(7)
        self.browser.find_element_by_xpath("//div[1][div[div[p[contains(text(),'" + str(
            movie) + "')]]]]/ancestor::div[1]/preceding-sibling::div[1]//input").click()
        # self.browser.execute_script("arguments[0].click();", check)
        time.sleep(2)
        self.browser.find_element(*self.delete_btn).click()
        time.sleep(4)
        self.browser.find_element(*self.delete_permission).click()

    @allure.step('Click and verify  newly created list ')
    def click_verify_new_list(self):
        time.sleep(5)
        self.browser.find_element(*self.mylist_tab).click()
        time.sleep(17)
        self.browser.find_element(*self.autoRand_list).click()

    # Footer
    @allure.step('Verify Privacy policy should be displayed in footer')
    def verify_Privacypolicy(self):
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.privacy_policy))
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        return self.browser.find_element(*self.privacy_policy).is_displayed()

    @allure.step('Verify terms of use should be present in footer')
    def verify_termsUse(self):
        time.sleep(1)
        return self.browser.find_element(*self.terms_use).is_displayed()

    @allure.step('Verify mgm logo in footer')
    def verify_footerLogo(self):
        time.sleep(1)
        return self.browser.find_element(*self.footer_logo).is_displayed()

    @allure.step('Verify support link should be displayed in footer')
    def verify_supportLink(self):
        time.sleep(1)
        return self.browser.find_element(*self.support).is_displayed()

    @allure.step('Verify Address should be displayed in footer')
    def verify_address(self):
        time.sleep(2)
        return self.browser.find_element(*self.address).is_displayed()

    @allure.step('Verify Youtube icon should be displayed in footer')
    def verify_youtubeIcon(self):
        time.sleep(2)
        return self.browser.find_element(*self.youtube_icon).is_displayed()

    @allure.step('Verify Facebook icon should be displayed in footer')
    def verify_fbIcon(self):
        return self.browser.find_element(*self.fb_icon).is_displayed()

    @allure.step('Verify Twitter should be displayed in footer')
    def verify_twitterIcon(self):
        time.sleep(1)
        return self.browser.find_element(*self.twitter_icon).is_displayed()

    @allure.step('Verify Insta icon should be displayed in footer')
    def verify_instaIcon(self):
        time.sleep(2)
        return self.browser.find_element(*self.insta_icon).is_displayed()

    @allure.step('Verify Copyright should be displayed in footer')
    def verify_copyright(self):
        time.sleep(1)
        return self.browser.find_element(*self.copyright).is_displayed()


