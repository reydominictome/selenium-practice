import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class MetroEventsHomePage(unittest.TestCase):
    #Localhost for the metroevents webapp
    base_url="https://www.google.com/"
    searchObject = "java"

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging']) # Does not display logs
        chromeOptions.add_argument("headless")  # Does not show the browser
        chromeOptions.add_experimental_option("detach", True) # Prevent the browser from closing

        self.driver = webdriver.Chrome(options=chromeOptions, executable_path="C:/SeleniumDrivers/chromedriver.exe")
        self.driver.implicitly_wait(50)

    def test_load(self):
        """Should be redirected to the Google Page"""
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("Google", driver.title, "Should be at the landing page")
    
    def test_search(self):
        """Should search Java successfully"""
        driver = self.driver
        driver.get(self.base_url)

        search_bar = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        
        search_bar.send_keys('java')
        search_bar.send_keys(Keys.RETURN)

        self.assertIn(self.searchObject + " - Google Search", driver.title, "Should be in the correct web page.")

    def test_search_then_image(self):
        """Should search Java successfully and head to Images"""
        driver = self.driver
        driver.get(self.base_url)

        search_bar = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search_bar.send_keys('java')
        search_bar.send_keys(Keys.RETURN)

        image_link = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        image_link.click()

        image = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[2]/a[1]/div[1]/img')
        image.click()

        button_to_website = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[3]/div[1]/a[2]')
        button_to_website.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()