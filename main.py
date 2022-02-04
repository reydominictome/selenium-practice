import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def launchDefaultChromeBrowser():
    chromeOptions = Options()
    chromeOptions.add_experimental_option("detach", True) # Prevent the browser from closing
    chromeOptions.add_argument("headless")
    driver = webdriver.Chrome(options=chromeOptions, executable_path="C:/SeleniumDrivers/chromedriver.exe")
    driver.implicitly_wait(20)
    driver.get('https://www.google.com/')

    return driver

def launchBraveBrowser():
    chromeOptions = Options()
    chromeOptions.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging']) # Does not display logs
    chromeOptions.add_experimental_option("detach", True) # Prevent the browser from closing

    driver = webdriver.Chrome(options=chromeOptions, executable_path="C:/SeleniumDrivers/chromedriver.exe")
    driver.implicitly_wait(20) 
    driver.get('https://www.google.com/')

    return driver

driver = launchDefaultChromeBrowser()
# driver = launchBraveBrowser()


