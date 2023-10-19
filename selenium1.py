from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Edge()
driver.get("https://www.cathaybk.com.tw/cathaybk/")
driver_wait = WebDriverWait(driver,5,1)
driver.save_screenshot("cathyBank.png")
driver.close()