import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MetroEventsHomePage(unittest.TestCase):
    #Localhost for the metroevents webapp
    base_url="http://127.0.0.1:8000/webapp/"

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging']) # Does not display logs
        chromeOptions.add_argument("headless")  # Does not show the browser
        chromeOptions.add_experimental_option("detach", True) # Prevent the browser from closing

        self.driver = webdriver.Chrome(options=chromeOptions, executable_path="C:/SeleniumDrivers/chromedriver.exe")
        self.driver.implicitly_wait(50)

    def test_load(self):
        """Should be redirected to the Home Page"""
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("User", driver.title)
    
    def test_sign_in(self):
        """User should be logged in and logged out"""
        driver = self.driver
        driver.get(self.base_url)

        username = driver.find_element_by_id('sign-in-user').send_keys("sasaki")
        password = driver.find_element_by_id('sign-in-pass').send_keys("123123")
        signin_button = driver.find_element_by_id("login-btn")
        signin_button.click()

        self.assertIn("Home", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()