from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import configparser
import time

try:
  start_time = datetime.datetime.now()
  config = configparser.ConfigParser()
  config.read("Config1.ini")
  url = 'https://demo.altevics.ru'
  driver = webdriver.Chrome()
  driver.get(url)
  driver.maximize_window()

  user = config.get('AUTHORIZATION_PARAMS', 'user')
  password = config.get('AUTHORIZATION_PARAMS', 'password')
  print('user: ', user)
  print('password: ', password)
  user_string = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Логин']"))).send_keys(user)
  password_string = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Пароль']"))).send_keys(password)
  button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='regular_enter']"))).click()
  IT_inquiries = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tile-content__card')][1]"))).click()

  Job_support = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tile-content__card')][1]"))).click()
  time.sleep(10)
except Exception as ex:
 print(ex)
finally:
  driver.close()
  driver.quit()
