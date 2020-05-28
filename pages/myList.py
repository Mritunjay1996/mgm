import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from resources.variables import *
from pathlib import Path
from os import path
import os
import csv


class myListObj:
    list_name = (By.XPATH, "//span[@class='view-title']")
    share_button = (By.XPATH, "//span[@class='share-icon']")
    delete_button = (By.XPATH, "//span[contains(text(), 'Delete')]")
    delete_1text = (By.XPATH, "//h3[@classs='header']")
    delete_list = (By.XPATH, "//li[@class='sub-title ng-star-inserted']")
    delete_2text = (By.XPATH, "//p[@class='directions ng-star-inserted']")
    dlt_btn = (By.XPATH, "//button[@class='cui-btn cui-btn-primary ng-star-inserted']")
    cncl_btn = (By.XPATH, "//button[@class='cui-btn cui-btn-secondary']")
    list_check = (By.XPATH, "//input[@id='select-all']")
    add_list = (By.XPATH, "//button[@id='dropdownForm1']")
    delete_close = (By.XPATH, "//div[@class='close-x desk-close']//img[@class='close-btn-image']")
    close_popup = (By.XPATH, "//div[@class='modal-header-popup desk-close']//img[@class='close-btn-image']")
    static_topText = (By.XPATH, "//div[@class='share-header']")
    pop_list = (By.XPATH, "//div[@class='share-body ng-star-inserted']")
    static_2Text = (By.XPATH, "//div[@class='share-list']")
    email_textbox = (By.XPATH, "//input[@id='email']")
    share_btn = (By.XPATH, "//button[@class='share-btn']")
    autoRand_list = (By.XPATH, "//a[contains(text(),'" + new_List_name + "')]") #new_List_name
    download = (By.XPATH, "//span[contains(text(),'DOWNLOAD.CSV')]")
    share_popup = (By.XPATH, "//span[contains(text(),'SHARE LIST')]")
    share_title = (By.XPATH, "//span[contains(text(),'SHARE TITLE')]")
    mylist_tab = (By.XPATH, "//ul[@class='menu-items']//a[@id='My Lists']")
    # family_chkvox = (By.XPATH, "//div[a[contains(text(),'Family')]]//parent::div[1]/input[1]")
    # family_chkvox = (By.XPATH, "//div[a[contains(text(),'Blockbusters')]]//parent::div[1]/input[1]")
    family_chkvox = (By.XPATH, "//div[div[p[contains(text(),'Special Lists Made For You')]]]/following-sibling::div["
                               "1]/div[1]//div[@class='checkbox-shell-dark']/input[1]")
    demo_check = (By.XPATH, "//div[p[text()='Your Lists']]/following-sibling::div[1]/div[3]//mgm-checkbox-single["
                            "1]/div[1]/input[1]")
    delete_popup = (By.XPATH, "//span[contains(text(),'DELETE')]")
    movie_1chkbox =(By.XPATH, "//ul[@class='movie-card']/li[1]/div[1]/mgm-checkbox-single/div[1]/input[1]")
    addTOlist = (By.XPATH, "//span[contains(text(),'ADD TO LIST')]")
    newly_name_chkbx = (By.XPATH, "//a[contains(text(),'" + delete_listtt + "')]//parent::div["
                                                                            "1]/preceding-sibling::mgm-checkbox"
                                                                            "-single/div/input[1]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify List name in list table ')
    def verify_listName(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.list_name))
        return self.browser.find_element(*self.list_name).text

    @allure.step('Click share button in right top ')
    def click_shareButton(self):
        time.sleep(1)
        self.browser.find_element(*self.share_button).click()

    @allure.step('Click on delete button from popup')
    def click_deleteButton(self):
        time.sleep(3)
        self.browser.find_element(*self.delete_button).click()

    @allure.step('Verify Add to List tab in footer popup')
    def verify_addList(self):
        time.sleep(1)
        return self.browser.find_element(*self.add_list).is_displayed()

    @allure.step('Verify Close button in opened Pop after clicking on share button ')
    def verify_closeBtn(self):
        time.sleep(3)
        return self.browser.find_element(*self.close_popup).is_displayed()

    @allure.step('Verify Static top Text in in share in share popup ')
    def verify_staticToptext(self):
        time.sleep(1)
        return self.browser.find_element(*self.static_topText).is_displayed()

    @allure.step('Verify List name and numbers of title in it ')
    def verify_lisTitle(self):
        time.sleep(1)
        return self.browser.find_element(*self.pop_list).is_displayed()

    @allure.step('Verify Static text in middle in share popup ')
    def verify_staticTextmiddle(self):
        time.sleep(1)
        return self.browser.find_element(*self.static_2Text).is_displayed()

    @allure.step('Verify Email textbox in share popup ')
    def verify_emailTextbox(self):
        time.sleep(1)
        return self.browser.find_element(*self.email_textbox).is_displayed()

    @allure.step('Verify Share button in share popup ')
    def verify_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.share_btn).is_displayed()

    @allure.step('Enter email id in share list popup ')
    def enter_email(self, em):
        time.sleep(2)
        self.browser.find_element(*self.email_textbox).send_keys(em)

    @allure.step('Click on button to share list on email')
    def click_buttonToshare(self):
        time.sleep(1)
        self.browser.find_element(*self.share_btn).click()
        time.sleep(5)

    @allure.step('Verify Static top Text  in delete popup ')
    def verify_deleteToptext(self):
        time.sleep(1)
        return self.browser.find_element(*self.delete_1text).is_displayed()

    @allure.step('Verify List name and numbers of title in delete pop up ')
    def verify_deleteTitle(self):
        time.sleep(1)
        return self.browser.find_element(*self.delete_list).is_displayed()

    @allure.step('Verify Static text in middle in delete popup ')
    def verify_deleteTextmiddle(self):
        time.sleep(1)
        return self.browser.find_element(*self.delete_2text).is_displayed()

    @allure.step('Verify Delete button in delete popup')
    def verify_deleteBtnPop(self):
        time.sleep(1)
        return self.browser.find_element(*self.dlt_btn).is_displayed()

    @allure.step('Click on delete button to delete that list')
    def click_grant_delete(self):
        self.browser.find_element(*self.dlt_btn).click()

    @allure.step('Verify Cancel button in delete button popup')
    def verify_cancel_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.cncl_btn).is_displayed()

    @allure.step('Verify Close button displayed in Popup after clicking on top delete button ')
    def verify_delete_close(self):
        time.sleep(3)
        return self.browser.find_element(*self.delete_close).is_displayed()

    @allure.step('Click on cancel button to close popup in my list detailed page')
    def click_cancelButton(self):
        time.sleep(2)
        self.browser.find_element(*self.cncl_btn).click()

    @allure.step('Click and verify  newly created list ')
    def click_new_list(self):
        time.sleep(2)
        self.browser.find_element(*self.autoRand_list).click()

    @allure.step('Verify Deleted list in User created lists')
    def verify_deletedList(self):
        try:
            return self.browser.find_element(*self.autoRand_list).is_displayed()
        except:
            return False

    @allure.step('Click on list check box in header')
    def click_headerChkbox(self):
        time.sleep(2)
        self.browser.find_element(*self.list_check).click()

    @allure.step('click on download csv file in footer list detailed page')
    def click_csvdownload(self):
        # # time.sleep(2)
        # path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
        # time.sleep(1)
        # params = {'behavior': 'allow', 'downloadPath': path_to_download_folder}
        # time.sleep(1)
        # self.browser.execute_cdp_cmd('Page.setDownloadBehavior', params)
        # time.sleep(2)
        self.browser.find_element(*self.download).click()

    @allure.step('Verify CSV File is downloaded in Download Folder')
    def verify_csv_downloaded(self):
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
        print(path_to_download_folder)
        isExist = path.exists(path_to_download_folder + "\mgm-lions-den-titles.csv")
        time.sleep(3)
        os.remove(path_to_download_folder + "\mgm-lions-den-titles.csv")
        return isExist

    @allure.step('Click on share button  presented in footer ')
    def click_shareFooter(self):
        time.sleep(2)
        self.browser.find_element(*self.share_popup).click()

    @allure.step('Click on share title button present in footer')
    def click_shareTitleFooter(self):
        time.sleep(2)
        self.browser.find_element(*self.share_title).click()

    @allure.step('CLick on myList tab in list detailed page')
    def click_mylistTab(self):
        time.sleep(2)
        self.browser.find_element(*self.mylist_tab).click()

    @allure.step('Click on Family check box in curated list')
    def click_familyCheck(self):
        time.sleep(2)
        self.browser.find_element(*self.family_chkvox).click()

    @allure.step('Verify Family check box is selected in curated list')
    def verify_familyChekbox(self):
        time.sleep(2)
        return self.browser.find_element(*self.family_chkvox).is_selected()

    @allure.step('Clicking on check box in list page for multiple')
    def click_Demo_checkBox(self):
        time.sleep(2)
        chk = self.browser.find_element(*self.demo_check)
        chk.location_once_scrolled_into_view
        time.sleep(1)
        self.browser.find_element(*self.demo_check).click()

    @allure.step('Verify Delete tab in footer popup ')
    def verify_DeleteFooterpopup(self):
        time.sleep(1)
        try:
            return self.browser.find_element(*self.delete_popup).is_displayed()
        except:
            return False

    @allure.step('Click on delete in footer to delete the list')
    def deletelist_frmfooter(self):
        time.sleep(2)
        self.browser.find_element(*self.delete_popup).click()

    @allure.step('click on 1st movie card checkbox')
    def click_1moviechkbox(self):
        time.sleep(1)
        self.browser.find_element(*self.movie_1chkbox).click()

    @allure.step('clicking on add TO list button from footer ')
    def click_addTolist(self):
        time.sleep(2)
        self.browser.find_element(*self.addTOlist).click()

    @allure.step('Click on list check box in list page to delete')
    def click_listChkbox(self):
        time.sleep(2)
        chk = self.browser.find_element(*self.newly_name_chkbx)
        chk.location_once_scrolled_into_view
        time.sleep(1)
        self.browser.find_element(*self.newly_name_chkbx).click()

    @allure.step('Verify List is deleted successfully ')
    def verify_listDeleted(self):
        time.sleep(2)
        self.browser.refresh()
        time.sleep(30)
        try:
            return self.browser.find_element(*self.newly_name_chkbx).is_displayed()
        except:
            return False




