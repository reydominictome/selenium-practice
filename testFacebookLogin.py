from re import search
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class FacebookLoginAndCreatePost(unittest.TestCase):
    base_url="https://www.facebook.com/"
    email = ""
    password = ""

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging']) # Does not display logs
        chromeOptions.add_argument("headless")  # Does not show the browser
        chromeOptions.add_experimental_option("detach", True) # Prevent the browser from closing

        self.driver = webdriver.Chrome(options=chromeOptions, executable_path="C:/SeleniumDrivers/chromedriver.exe")
        self.driver.implicitly_wait(50)

    def test_facebook_login(self):
        """Should login to Facebook and create a post"""
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()

        self.assertIn("Facebook - Log In or Sign Up", driver.title, "Should be in Facebook Login Page")

        driver.find_element_by_id('email').send_keys(self.email)
        driver.find_element_by_id('pass').send_keys(self.password)

        login_button = driver.find_element_by_name('login')
        login_button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()