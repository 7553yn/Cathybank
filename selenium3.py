from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.cathaybk.com.tw/cathaybk/")
driver.implicitly_wait(5)
# product = driver.find_element(By.CLASS_NAME, "cubre-o-menu__btn")
product = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]")
product.click()
driver.implicitly_wait(5)

cards = driver.find_element(By.LINK_TEXT, "卡片介紹")
cards.click()

# 直向捲動至停發卡頁面，計算停發總數並逐一截圖
invalidCard = driver.find_element(By.XPATH,'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]/div[2]/div/div[4]/div/a/span')
action = ActionChains(driver)
action.move_to_element(invalidCard).perform()
time.sleep(3)
driver.save_screenshot('invalidCard01.png')

right = driver.find_element(By.XPATH,'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[4]')
right.click()
right.click()
right.click()
time.sleep(3)
driver.save_screenshot('invalidCard02.png')

right = driver.find_element(By.XPATH,'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[4]')
right.click()
right.click()
right.click()
time.sleep(3)
driver.save_screenshot('invalidCard03.png')

right = driver.find_element(By.XPATH,'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[4]')
right.click()
time.sleep(3)
driver.save_screenshot('invalidCard04.png')

invalidCards = len("本卡已停止申辦")
print('無效信用卡數量: ', invalidCards)
time.sleep(2)

driver.close()