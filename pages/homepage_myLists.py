import allure, time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from resources.variables import *


class homePagemylistsObj:
    total_lists = (By.XPATH, "//h2[contains(text(),'Your Lists')]/ancestor::div[3]/following-sibling::div[1]//ul[1]//li")
    auto_list = (By.XPATH, "//p[contains(text(),'Automation List')]")
    # myList = (By.XPATH, "//div[h2[contains(text(),'My Lists')]]")
    myList = (By.XPATH, "//div[h2[contains(text(),'Your Lists')]]")
    myList_rightNav = (By.XPATH, "(//div//a[@role='button']/i[@class='next-icon icon'])[1]")
    # myList_rightNav = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//i["
    #                              "@class='next-icon icon']")
    myList_prevNav = (By.XPATH, "//i[@class='previous-icon icon']")
    myList_seeall = (By.XPATH, "//a[contains(text(),'SEE LISTS')]")
    title_text = (By.XPATH, "//h2[contains(text(),'Your Lists')]")
    lists_cards = (By.XPATH, "//div[p[contains(text(),'Automation List')]]")
    list_page_tile = (By.XPATH, "//p[@class='yourList']")
    detail_title = (By.XPATH, "//span[@class='view-title']")
    card_titles = (By.XPATH, "//p[contains(text(),'Automation List')]/parent::div[1]/p[2]/span[1]")
    # curated_title = (By.XPATH, "//p[@class='title'][contains(text(),'Blockbusters')]")
    curated_title = (By.XPATH, "//ul[@class='movies-list d-flex active']/li[1]//div[@class='description']/p[1]")
    # curated_made = (By.XPATH, "//p[@class='title'][contains(text(),'Blockbusters')]/ancestor::a[1]/p[1]")
    curated_made = (By.XPATH, "//ul[@class='movies-list d-flex active']/li[1]//p[contains(text(),'LIST MADE FOR YOU')]")
    # curated_numTitle = (By.XPATH, "//p[@class='title'][contains(text(),'Blockbusters')]/parent::div[1]/p[2]/span[1]")
    curated_numTitle = (By.XPATH, "//ul[@class='movies-list d-flex active']/li[1]//div[@class='description']/p["
                                  "2]/span[1]")
    title = (By.XPATH, "//p[@class='yourList']")
    user_created = (By.XPATH, "//a[contains(text(),'Automation List')]")
    share_button = (By.XPATH, "//div[div[a[contains(text(),'Automation List')]]]/following-sibling::div[2]//span["
                              "@class='share']")
    delete_button = (By.XPATH, "//div[div[a[contains(text(),'Automation List')]]]/following-sibling::div[2]//span["
                               "@class='delete-icon']")
    list_check = (By.XPATH, "//div[p[text()='Your Lists']]/following-sibling::div[1]/div[2]//mgm-checkbox-single["
                            "1]/div[1]/input[1]")
    verifylist_check = (By.XPATH, "//div[p[text()='Your Lists']]/following-sibling::div[1]/div["
                                  "2]//mgm-checkbox-single[1]/div[1]")
    demo_check = (By.XPATH, "//div[p[text()='Your Lists']]/following-sibling::div[1]/div[3]//mgm-checkbox-single["
                            "1]/div[1]/input[1]")
    list_selected = (By.XPATH, "//div[@class='item-action']/span[1]")
    download = (By.XPATH, "//span[contains(text(),'DOWNLOAD.CSV')]")
    share_popup = (By.XPATH, "//span[contains(text(),'SHARE LIST')]")
    share_title = (By.XPATH, "//span[contains(text(),'SHARE TITLE')]")
    delete_popup = (By.XPATH, "//span[contains(text(),'DELETE')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify number of lists in My Lists section')
    def verify_Mylists(self):
        count = self.browser.find_elements(*self.total_lists)
        print(len(count))
        return len(count)

    @allure.step('Verify in My list Automation List is displayed')
    def verify_autoList(self):
        WebDriverWait(self.browser, 38).until(EC.presence_of_element_located(self.myList))
        lst = self.browser.find_element(*self.myList)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        time.sleep(6)
        return self.browser.find_element(*self.auto_list).is_displayed()

    @allure.step('Click on List card ')
    def click_listCard(self):
        time.sleep(3)
        list = self.browser.find_element(*self.auto_list)
        self.browser.execute_script("arguments[0].click();", list)

    @allure.step('Verify Detail Page for list is opened ')
    def verify_detailedPage(self):
        return self.browser.find_element(*self.detail_title).text

    @allure.step('Verify number of titles on list cards ')
    def verify_Numbtitles(self):
        return self.browser.find_element(*self.card_titles).is_displayed()

    @allure.step('Click on see all Button ')
    def click_seeALL(self):
        time.sleep(2)
        lst = self.browser.find_element(*self.myList)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        time.sleep(2)
        self.browser.find_element(*self.myList_seeall).click()

    @allure.step('Verify My lists Right navigation arrow')
    def verify_rightNav(self):
        ryt = self.browser.find_element(*self.myList_rightNav)
        # a.location_once_scrolled_into_view
        ActionChains(self.browser).move_to_element(ryt).perform()
        return ryt.is_displayed()
        # return btn

        # try:
        #     elem = self.browser.find_element(*self.myList_rightNav)
        # except NoSuchElementException:  # spelling error making this code not work as expected
        #     self.browser.implicitly_wait(10)
        #     ActionChains(self.browser).move_to_element(elem).perform()
        #     return elem.is_displayed()

    @allure.step('Verify My Lists Left Navigation arrow')
    def verify_LeftNav(self):
        time.sleep(3)
        ledt_nav = self.browser.find_element(*self.myList_prevNav)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(ledt_nav).perform()
        return ledt_nav.is_displayed()

    @allure.step('Click on Right navigation arrow in My Lists Section')
    def click_rightNav(self):
        time.sleep(2)
        self.browser.find_element(*self.myList_rightNav).click()

    @allure.step('Click on Left Navigation arrow in My lists section ')
    def click_leftNav(self):
        time.sleep(3)
        self.browser.find_element(*self.myList_prevNav).click()

    @allure.step('Verify Title text in My lists section ')
    def verify_Mylists_title(self):
        return self.browser.find_element(*self.title_text).is_displayed()

    @allure.step('Verify See all button in my Lists section ')
    def verify_seeAll(self):
        time.sleep(1)
        return self.browser.find_element(*self.myList_seeall).is_displayed()

    @allure.step('Verify List cards in myList section ')
    def verify_listCards(self):
        time.sleep(1)
        return self.browser.find_element(*self.lists_cards).is_displayed()

    @allure.step('Verify List page heading i.e opening after click on see all button')
    def verify_list_Heading(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.list_page_tile))
        return self.browser.find_element(*self.list_page_tile).text

    @allure.step('Verify Text List made for you on curated list cards ')
    def verify_curatedText(self):
        time.sleep(2)
        return self.browser.find_element(*self.curated_made).text

    @allure.step('Verify List title on curated list cards')
    def verify_curateList_title(self):
        return self.browser.find_element(*self.curated_title).is_displayed()

    @allure.step('Verify number of titles on curated list ')
    def verify_curatedNumtitles(self):
        return self.browser.find_element(*self.curated_numTitle).is_displayed()

    @allure.step('Verify Title of lists ')
    def verify_listsTitle(self):
        time.sleep(1)
        return self.browser.find_element(*self.title).text

    @allure.step('Verify User created List in table ')
    def verify_userCreated_list(self):
        time.sleep(1)
        return self.browser.find_element(*self.user_created).text

    @allure.step('Verify share button is displayed in list page')
    def verify_shareButton(self):
        time.sleep(1)
        return self.browser.find_element(*self.share_button).is_displayed()

    @allure.step('Verify Delete button is displayed in list page ')
    def verify_deleteButton(self):
        time.sleep(1)
        return self.browser.find_element(*self.delete_button).is_displayed()

    @allure.step('Verify Check box is displayed in list  page ')
    def verify_checkBox(self):
        time.sleep(2)
        chk = self.browser.find_element(*self.verifylist_check)
        chk.location_once_scrolled_into_view
        return chk.is_displayed()

    @allure.step('Verify Check box gets selected after clicking on check box')
    def verify_checkselected(self):
        time.sleep(1)
        return self.browser.find_element(*self.list_check).is_selected()

    @allure.step('Clicking on check box in list page')
    def click_list_checkBox(self):
        time.sleep(2)
        self.browser.find_element(*self.list_check).click()

    @allure.step('Verify Check box gets selected after clicking on check box foe multiple')
    def verify_Demoselected(self):
        time.sleep(1)
        return self.browser.find_element(*self.demo_check).is_selected()

    @allure.step('Clicking on check box in list page for multiple')
    def click_Demo_checkBox(self):
        time.sleep(3)
        self.browser.find_element(*self.demo_check).click()

    @allure.step('Verify List selected Text in opened footer popup')
    def verify_Listtext(self):
        time.sleep(1)
        return self.browser.find_element(*self.list_selected).text

    @allure.step('Verify Download.csv file  in footer popup')
    def verify_downloadCsv(self):
        time.sleep(1)
        return self.browser.find_element(*self.download).is_displayed()

    @allure.step('Verify share list  in footer popup')
    def verify_shareList(self):
        time.sleep(1)
        return self.browser.find_element(*self.share_popup).is_displayed()

    @allure.step('Verify share title from footer on movie ')
    def verify_shareTitle(self):
        time.sleep(2)
        return self.browser.find_element(*self.share_title).is_displayed()

    @allure.step('Verify Delete tab in footer popup ')
    def verify_DeleteFooterpopup(self):
        time.sleep(1)
        return self.browser.find_element(*self.delete_popup).is_displayed()

    @allure.step('Click on list name to redirect on list detailed page')
    def click_Createdlist(self):
        time.sleep(1)
        self.browser.find_element(*self.user_created).click()




