from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.cathaybk.com.tw/cathaybk/")
driver_wait = WebDriverWait(driver,5,0.5)
product = driver_wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div")))
driver_wait = WebDriverWait(driver,5,0.5)
product.click()
print('信用卡共有:', len('lnk_Link'),'項目')
driver_wait = WebDriverWait(driver,5,0.5)
driver.save_screenshot("creditCard.png")
driver_wait = WebDriverWait(driver,5,0.5)
driver.close()