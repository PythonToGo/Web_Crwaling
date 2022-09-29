import time
from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def wait_until(xpath_str):
    WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://flight.naver.com/'
browser.get(url)

wait_until('//b[text() = "도착"]')
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

wait_until('//button[text() = "국내"]')
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

wait_until('//i[contains(text(), "제주국제공항")]')
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()



wait_until('//button[text() = "가는 날"]')
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

remove_date = browser.find_element(By.XPATH, '//button[text() = "날짜지우기"]')
action = ActionChains(browser)
action.move_to_element(remove_date).perform()

wait_until('//b[text()= "30"]')
day29 =browser.find_element(By.XPATH, '//b[text() = "29"]')
time.sleep(3)
day29.click()


# wait_until('//b[text() = "도착"]')
# arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
# arrival.click()
wait_until('//b[text() = "30"]')
day30  = browser.find_element(By.XPATH, '//b[text()= "30"]')
time.sleep(3)
day30.click()



wait_until('//span[@class= "항공권 검색"]')
search = browser.find_element(By.XPATH, '//span[@class= "항공권 검색"]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_select_schedule__xWQ-K"]')))

print(elem.text)

browser.quit()