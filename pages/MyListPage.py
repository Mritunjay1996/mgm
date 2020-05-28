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


class MyList:
    list_made_for_you_container = (
    By.XPATH, "//p[text()='Special Lists Made For You']/ancestor::div[2]/following-sibling::div")
    list_made_for_you_heading = (By.XPATH, "//p[text()='Special Lists Made For You']")
    your_list_container = (By.XPATH, "//p[text()='Your Lists']/ancestor::div[1]/following-sibling::div")
    your_list_heading = (By.XPATH, "//p[text()='Your Lists']")
    abc = (By.XPATH, "(//div//a[@role='button']/i[@class='next-icon icon'])[1]")
    abc1 = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//i[@class='next-icon icon']")
    list_made_for_you_checkbox = (By.XPATH,
                                  "//p[text()='Special Lists Made For You']/ancestor::div[2]/following-sibling::div//div[@class='checkbox-shell-dark']")
    # list_made_for_you_Family = (By.XPATH, "//p[text()='Special Lists Made For You']/ancestor::div[2]/following-sibling::div//a[text()='Family']")
    list_made_for_you_Family = (By.XPATH, "//div[div[p[text()='Special Lists Made For You']]]/following-sibling::div["
                                          "1]/div[1]//a[1]")
    list_made_for_you_share_button = (By.XPATH, "//div[div[p[text()='Special Lists Made For "
                                                "You']]]/following-sibling::div[1]/div[1]/div[3]/button[1]/span[1]")
    checkbox_family = (By.XPATH, "//div[div[p[contains(text(),'Special Lists Made For "
                                 "You')]]]/following-sibling::div[1]/div[1]//div[@class='checkbox-shell-dark']/input["
                                 "1]")
    checkbox_woody_allen = (By.XPATH,
                            "//p[text()='Lists Made For You']/ancestor::div[2]/following-sibling::div//a[text()='Woody Allen']/parent::div//input")
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
    recently = (By.XPATH, "//h2[text()='My Lists']")
    checked_list_popup = (By.XPATH, "//div[@class='item-list']/parent::div")
    checked_list_popup_number_selected_list = (By.XPATH, "//div[@class='item-list']//span")
    checked_list_popup_download_csv = (By.XPATH, "//div[@class='item-list']//span[text()='DOWNLOAD.CSV']")
    # checked_list_popup_share_list_button = (By.XPATH, "//div[@class='item-list']//span[text()='SHARE LIST']")
    checked_list_popup_share_list_button = (By.XPATH, "//span[contains(text(),'SHARE LIST')]")
    verify_family_list_page = (By.XPATH, "//div[@class='list-name']/span[1]")
    share_pop_up = (By.XPATH, "//div[@class='share-input']")
    close_btn = (By.XPATH, "//div[@class='share-header']/ancestor::div[2]//img[@class='close-btn-image']")
    share_header = (By.XPATH, "//div[@class='share-header']")
    list_name_number = (By.XPATH, "//div[@class='sub-title']/div[1]")
    static_text = (By.XPATH, "//div[@class='share-list']")
    email_textbox = (By.XPATH, "//div/input[@id='email']")
    share_button = (By.XPATH, "//div[@class='listing']/div[4]/button")
    # footer_share_button = (By.XPATH, "//div[@class='item-list']//span[text()='SHARE LIST']")
    # footer_share_button = (By.XPATH, "//div[@class='item-list']//span[text()='SHARE LIST']")
    sort_select = (By.XPATH, "//div[@class='sort-filter']/div")
    sort_by_release_date = (By.XPATH, "//div[@class='sort-filter']/select/option[1]")
    sort_by_release_date_New_Old = (By.XPATH, "//div[@class='sort-filter']/div/span[1]")
    sort_by_release_date_Old_New = (By.XPATH, "//div[@class='sort-filter']/div/span[2]")
    sort_A_Z = (By.XPATH, "//div[@class='sort-filter']/div/span[3]")
    sort_Z_A = (By.XPATH, "//div[@class='sort-filter']/div/span[4]")
    movie_card_test1 = (By.XPATH, "//div//a[text()='test1']")

    def __init__(self, browser):
        self.browser = browser
        # self.browser = WebDriver

    @allure.step('verify List made for you is displayed')
    def ListMadeForYouContainer(self):
        container1 = self.browser.find_element(*self.list_made_for_you_container)
        container1.location_once_scrolled_into_view
        return container1.is_displayed()

    @allure.step('Verify List made for you heading is displayed')
    def ListMadeForYouHeading(self):
        return self.browser.find_element(*self.list_made_for_you_heading).is_displayed()

    @allure.step('Verify Your list container is displayed')
    def YourListContainer(self):
        container = self.browser.find_element(*self.your_list_container)
        container.location_once_scrolled_into_view
        return container.is_displayed()

    @allure.step('Verify your list heading is displayed')
    def YourListHeading(self):
        return self.browser.find_element(*self.your_list_heading).is_displayed()

    @allure.step('Verify List checkbox is visible')
    def ListCheckbox(self):
        checkbox = self.browser.find_element(*self.list_made_for_you_checkbox)
        checkbox.location_once_scrolled_into_view
        time.sleep(3)
        return checkbox.is_displayed()

    @allure.step('Verify List Name is Visible')
    def ListName(self):
        return self.browser.find_element(*self.list_made_for_you_Family).is_displayed()

    @allure.step('Verify Share button is Visible')
    def ListShareButton(self):
        return self.browser.find_element(*self.list_made_for_you_share_button).is_displayed()

    @allure.step('Click Checkbox Family List')
    def VerifyCheckBoxFamily(self):
        time.sleep(2)
        self.browser.find_element(*self.checkbox_family).click()
        time.sleep(3)
        checked = self.browser.find_element(*self.checkbox_family).is_selected()
        time.sleep(3)
        # self.browser.find_element(*self.checkbox_family).click()
        print(checked)
        return checked

    @allure.step('Click Checkbox Woody allen and select multiple lists')
    def SelectMultipleLists(self):
        checkfamily = self.browser.find_element(*self.checkbox_family).is_selected()
        if checkfamily == False:
            self.browser.find_element(*self.checkbox_family).click()

        self.browser.find_element(*self.checkbox_woody_allen).click()
        time.sleep(3)
        allen = self.browser.find_element(*self.checkbox_woody_allen).is_selected()
        print(allen)
        return allen

    @allure.step('Verify Privacy policy should be displayed in footer')
    def verify_Privacypolicy(self):
        time.sleep(3)
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
        time.sleep(1)
        return self.browser.find_element(*self.address).is_displayed()

    @allure.step('Verify Youtube icon should be displayed in footer')
    def verify_youtubeIcon(self):
        time.sleep(1)
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
        return self.browser.find_element(*self.insta_icon).is_displayed()

    @allure.step('Verify Copyright should be displayed in footer')
    def verify_copyright(self):
        time.sleep(1)
        return self.browser.find_element(*self.copyright).is_displayed()

    def Abc(self):
        c = self.browser.find_element(*self.recently)
        c.location_once_scrolled_into_view
        time.sleep(2)
        a = self.browser.find_element(*self.abc)
        a.location_once_scrolled_into_view
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(a).perform()
        # b = self.browser.find_element(*self.abc1)
        # actionchains.move_to_element(b).perform()
        btn = a.is_displayed()
        return btn

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

    @allure.step('Click Family List')
    def ClickListFamily(self):
        time.sleep(2)
        self.browser.find_element(*self.list_made_for_you_Family).click()

    @allure.step('Verify Family list page')
    def VerifyFamilyList(self):
        time.sleep(10)
        return self.browser.find_element(*self.verify_family_list_page).is_displayed()

    @allure.step('Verify share Pop-Up is visible')
    def SharePopUp(self):
        return self.browser.find_element(*self.share_pop_up).is_displayed()

    @allure.step('Verify Close button is visible')
    def ShareCloseBtn(self):
        return self.browser.find_element(*self.close_btn).is_displayed()

    @allure.step('Verify Header is visible')
    def ShareHeader(self):
        return self.browser.find_element(*self.share_header).is_displayed()

    @allure.step('Verify List name and number is visible')
    def ShareListNameAndNumber(self):
        return self.browser.find_element(*self.list_name_number).is_displayed()

    @allure.step('Verify Static text is visible')
    def ShareStaticText(self):
        return self.browser.find_element(*self.static_text).is_displayed()

    @allure.step('Verify email textbox is visible')
    def ShareEmailTextBox(self):
        return self.browser.find_element(*self.email_textbox).is_displayed()

    @allure.step('Verify share button is visible')
    def ShareButton(self):
        return self.browser.find_element(*self.share_button).is_displayed()

    @allure.step('Click list share button')
    def ClickListShareButton(self):
        self.browser.find_element(*self.list_made_for_you_share_button).click()

    def ClickFooterShareButton(self):
        time.sleep(4)
        self.browser.find_element(*self.checked_list_popup_share_list_button).click()

    def ClickSortDropdown(self):
        time.sleep(5)
        self.browser.find_element(*self.sort_select).click()

    def SortByReleaseDateNewOld(self):
        name = self.browser.find_element(*self.sort_by_release_date_New_Old).text
        return name

    def SortByReleaseDateOldNew(self):
        name = self.browser.find_element(*self.sort_by_release_date_Old_New).text
        return name

    def SortByAZ(self):
        name = self.browser.find_element(*self.sort_A_Z).text
        return name

    def SortByZA(self):
        name = self.browser.find_element(*self.sort_Z_A).text
        return name

    def ClickListTest1(self):
        scroll = self.browser.find_element(*self.movie_card_test1)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        time.sleep(3)
        scroll.click()
