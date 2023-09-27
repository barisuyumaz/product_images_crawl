from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#driver
class WebScrappingDriver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
        self.service = Service(r"C:/Users/Administrator/Desktop/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.maximize_window()

    def scrap_data(self, link):
        self.driver.get(link)
        time.sleep(4)

    def get_page_source_soup(self):
        source = self.driver.page_source
        soup = BeautifulSoup(source, "html.parser")
        return soup

    def click_By_xpath(self,xpath_value):
        self.driver.find_element(By.XPATH, xpath_value).click()

    def click_By_id(self,id_value):
        self.driver.find_element(By.ID, id_value).click()

    def take_ss(self):
        self.driver.save_screenshot("hello.png")

    def quit_driver(self):
        self.driver.quit()