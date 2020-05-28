import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *


class recaddListObj:
    lists_allLabel = (By.XPATH, "//div[@class='toggle-btn-item']//span[@class='slider-label']")
    search_box = (By.XPATH, "//input[@placeholder='Search']")
    clear_button = (By.XPATH, "//button[@class='cui-btn cui-btn-flat on-light']")
    new_created = (By.XPATH, "//span[contains(text(),'" + new_List_name + "')]")
    automation_list = (By.XPATH, "//span[contains(text(),'Automation List')]")
    # select_autolist = (By.XPATH, "//span[contains(text(),'Automation List')]/preceding-sibling::span[1]")
    select_autolist = (By.XPATH, "//span[contains(text(),'Automation List')]/ancestor::label/input")
    input_list = (By.XPATH, "//input[@placeholder='My New List Name']")
    addList_popup = (By.XPATH, "//div[@class='main']/following-sibling::mgm-add-to-list[1]")
    createList_btn = (By.XPATH, "//button[@class='cui-btn cui-btn-flat cui-btn-o-1 on-light']")
    loader_text = (By.XPATH, "//div[@class='loder-text']")
    success_created = (By.XPATH, "//div[@class='atl-add-btn']//span[@class='ie11fix uppercase']")
    success_created1 = (By.XPATH, "//div[@class='createdListItem']//span[text()=' Created! ']")
    success_created_list = (By.XPATH, "//div[@class='createdListItem ng-star-inserted']//span[@class='ie11fix uppercase']")
    # checked_box = (By.XPATH, "//span[contains(text(),'" + new_List_name + "')]/preceding-sibling::span[1]")
    checked_box = (By.XPATH, "//span[contains(text(),'" + new_List_name + "')]/ancestor::label/input")
    add_button = (By.XPATH, "//button[span[contains(text(),'Add To List(s)')]]")
    alert = (By.XPATH, "//div[@class='atl-title-label uppercase']")
    cardhover_option1 = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div["
                                   "3]/following-sibling::div//ul[@class='movies-list d-flex active']/li[1]//button["
                                   "contains(text(),'ADD TO LIST')]")
    # cardhover_option2 = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div["
    #                                "3]/following-sibling::div//ul[@class='movies-list d-flex active']/li[2]//button["
    #                                "contains(text(),'ADD TO LIST')]")
    # cardhover_option1 = (By.XPATH, "//h2[contains(text(),'Action / Adventure')]/ancestor::div["
    #                                "3]/following-sibling::div//ul[@class='movies-list d-flex active']/li[2]//button["
    #                                "contains(text(),'ADD TO LIST')]")
    cardhover_option2 = (By.XPATH, "//h2[contains(text(),'Action / Adventure')]/ancestor::div["
                                   "3]/following-sibling::div//ul[@class='movies-list d-flex active']/li[3]//button["
                                   "contains(text(),'ADD TO LIST')]")
    recently_watched = (By.XPATH, "//h2[contains(text(),'Recently Watched')]")
    action_adventure = (By.XPATH, "//h2[contains(text(),'Action / Adventure')]")
    total_movie = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div["
                             "3]/following-sibling::div//ul//div[@class='desk-on']//p[1]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify  add to List Pop is opened in recently watched section')
    def verify_addToList(self):
        time.sleep(3)
        self.browser.refresh()
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.recently_watched))
        recently = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        time.sleep(5)
        card1 = self.browser.find_element(*self.cardhover_option1)
        ActionChains(self.browser).move_to_element(card1).perform()
        card1.click()
        time.sleep(3)
        alert = self.browser.find_element(*self.alert).text
        time.sleep(1)
        print(alert)
        return alert

    @allure.step('Click on List name showing in pop up')
    def click_listName(self):
        time.sleep(2)
        self.browser.find_element(*self.automation_list).click()

    # @allure.step('Enter list name which you want to create ')
    # def enter_Listname(self, name):
    #     self.browser.find_element(*self.input_list).send_keys(name)

    @allure.step('Enter list name which you want to create ')
    def enter_Listname(self, name):
        time.sleep(3)
        self.browser.find_element(*self.input_list).send_keys(name)

    @allure.step('Click on Create List button')
    def click_createList_text(self):
        self.browser.find_element(*self.createList_btn).click()

    @allure.step('Clicking Create list button should change in creating..')
    def verify_LoaderText(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 15, ignored_exceptions).until(EC.presence_of_element_located(self.loader_text))
        loader = self.browser.find_element(*self.loader_text).text
        time.sleep(1)
        print(loader)
        return loader

    @allure.step('New List should appear in created list')
    def verify_newCreatedlist(self):
        WebDriverWait(self.browser, 25).until((EC.presence_of_element_located(self.new_created)))
        return self.browser.find_element(*self.new_created).text

    @allure.step('Verify success message after clicking on create list ')
    def verify_success_msg(self):
        # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.success_created)) #ignored_exceptions
        return self.browser.find_element(*self.success_created).is_displayed()

    @allure.step('Verify Success created text')
    def verify_success_created(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.success_created))
        return self.browser.find_element(*self.success_created).is_displayed()

    @allure.step('Verify Success created text on list page')
    def verify_success_created_list(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.success_created_list))
        return self.browser.find_element(*self.success_created_list).is_displayed()

    @allure.step('verify Checked box is checked in pop')
    def verify_checkBox(self):
        return self.browser.find_element(*self.checked_box).is_selected()

    @allure.step('click on add to list button to add movie ')
    def click_Addlist_button(self):
        time.sleep(2)
        self.browser.find_element(*self.add_button).click()

    @allure.step('Verify total number of elements in lists ')
    def verify_Listcount(self):
        count = self.browser.find_elements(*self.lists_allLabel)
        print(len(count))
        return len(count)

    @allure.step('Enter list name in search box')
    def enter_listname_search(self, name):
        time.sleep(2)
        self.browser.find_element(*self.search_box).send_keys(name)

    @allure.step('Verify searched element is displaying in list')
    def verify_searchElement(self):
        time.sleep(1)
        return self.browser.find_element(*self.new_created).text

    @allure.step('Verify on clicking of clear button filter should removed. ')
    def verify_Clearbutton(self):
        self.browser.find_element(*self.clear_button).click()
        time.sleep(3)
        count = self.browser.find_elements(*self.lists_allLabel)
        if len(count) > 1:
            return "Search cleared"
        else:
            return "Search not cleared."

    @allure.step('Click add to list button on 2nd movie card')
    def click_addtoList2Card(self):
        time.sleep(3)
        self.browser.refresh()
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.action_adventure))
        adventures = self.browser.find_element(*self.action_adventure)
        self.browser.execute_script("arguments[0].scrollIntoView();", adventures)
        time.sleep(5)
        card2 = self.browser.find_element(*self.cardhover_option2)
        ActionChains(self.browser).move_to_element(card2).perform()
        card2.click()

    @allure.step('select newly created list to add same movie in multiple')
    def select_newlyList(self):
        time.sleep(3)
        self.browser.find_element(*self.new_created).click()

    @allure.step('Click on Add to list on 2nd movie card')
    def click_2cardAdd(self):
        time.sleep(3)
        recently = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        time.sleep(3)
        card2 = self.browser.find_element(*self.cardhover_option2)
        ActionChains(self.browser).move_to_element(card2).perform()
        time.sleep(1)
        card2.click()

    @allure.step('Verify total number of movie cards in recently watched ')
    def verify_Totalmovie(self):
        count = self.browser.find_elements(*self.total_movie)
        time.sleep(2)
        print(len(count))
        return len(count)

    @allure.step('verify Select list from pop after search')
    def verify_selectList(self):
        time.sleep(3)
        return self.browser.find_element(*self.select_autolist).is_selected()




