from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.variables import *
import csv
from pathlib import Path
import os
import allure, time


class mailinatorPageObj:
    url = "https://www.mailinator.com/"
    search_box = (By.XPATH, "//input[@id='addOverlay']")
    goBtn = (By.XPATH, "//button[@id='go-to-public']")
    # mail_subName = (By.XPATH, "//a[contains(text(),'Lists shared with you')]")
    # mail_subName = (By.XPATH, "//table[@class='table table-striped jambo_table']//tbody//td[4]")
    mail_subName = (By.XPATH, "//a[contains(text(), 'View my MGM ROAR list')]")
    attachment = (By.XPATH, "//td[contains(text(),'Attachments:')]")
    from_mail = (By.XPATH, "//b[contains(text(),'noreply@practicallogix.com')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Open Url for mailinator')
    def openMailinator(self):
        # Open a new window
        self.browser.execute_script("window.open('');")
        time.sleep(3)
        # Switch to the new window and perform any task over that window
        self.browser.switch_to.window(self.browser.window_handles[1])
        time.sleep(1)
        self.browser.get(self.url)
        time.sleep(3)

    @allure.step('Enter email into mailinator to search appointment ')
    def enterEmailinmailinator(self, em):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.search_box))
        self.browser.find_element(*self.search_box).send_keys(em)

    @allure.step('Click on go to public ')
    def clickGopublic(self):
        time.sleep(2)
        self.browser.find_element(*self.goBtn).click()

    @allure.step('Click on initial mail')
    def click_initialMail(self):
        WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.mail_subName))
        self.browser.find_element(*self.mail_subName).click()

    @allure.step('Verify mail recieved from')
    def verify_sender(self):
        time.sleep(3)
        return self.browser.find_element(*self.from_mail).text

    @allure.step('Verify mail contains attachment ')
    def verify_attachment(self):
        time.sleep(2)
        return self.browser.find_element(*self.attachment).is_displayed()

    @allure.step('Close mailinator window')
    def close_mailinator(self):
        # Close the tab with URL B
        self.browser.close()
        # Switch back to the first tab with URL A
        self.browser.switch_to.window(self.browser.window_handles[0])

    @allure.step("Get elements of csv file ")
    def Get_csvElements(self):
        time.sleep(2)
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
        print(path_to_download_folder)
        with open(path_to_download_folder + "\mgm-lions-den-titles.csv", 'r', encoding="utf8") as file:
            spamreader = csv.reader(file, delimiter=' ', quotechar='|')
            fields = next(spamreader)
            title = (' '.join(field for field in fields))
            global text
            text = title.split(',')

    @allure.step('Verify element in csv file -> LIST NAME')
    def verify_csv_listname(self):
        time.sleep(1)
        return str(text[0]).replace('"', "")

    @allure.step('Verify element in csv file -> IP Title Description')
    def verify_csv_Iptitle(self):
        time.sleep(1)
        return str(text[1]).replace('"', "")

    @allure.step('Verify element in csv file -> IP Type')
    def verify_csv_IpType(self):
        time.sleep(1)
        return str(text[2]).replace('"', "")

    @allure.step('Verify element in csv file -> Release or air date')
    def verify_csv_release(self):
        time.sleep(1)
        return str(text[4]).replace('"', "")

    @allure.step('Verify element in csv file -> Genre + Sub-genre')
    def verify_csv_genre(self):
        time.sleep(1)
        return str(text[7]).replace('"', "")

    @allure.step('Verify element in csv file -> Synopsis')
    def verify_csv_synopsis(self):
        time.sleep(1)
        return str(text[8]).replace('"', "")

    @allure.step('Verify element in csv file -> Rating')
    def verify_csv_rating(self):
        time.sleep(1)
        return str(text[5]).replace('"', "")

    @allure.step('Verify element in csv file -> Main Cast')
    def verify_csv_mainCast(self):
        time.sleep(1)
        return str(text[9]).replace('"', "")

