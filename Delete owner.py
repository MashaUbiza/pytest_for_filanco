from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import configparser

try:
  start_time = datetime.datetime.now()
  config = configparser.ConfigParser()
  config.read("config.ini")

  driver = webdriver.Chrome()
  driver.maximize_window()
  panel_url = config.get('AUTHORIZATION_PARAMS', 'panel_url')
  owner_url = panel_url + "/handbook/owner"

  driver.get(owner_url)
  print('panel_url: ', panel_url)
  print(owner_url)
  if owner_url == panel_url:
    raise ValueError('Страница не загрузилась!')

  user = config.get('AUTHORIZATION_PARAMS', 'user')
  password = config.get('AUTHORIZATION_PARAMS', 'password')
  print('user: ', user)
  print('password: ', password)

  search_string = driver.find_element(By.NAME, "username")

  search_string.send_keys(user)
  search_string = driver.find_element(By.NAME, "password")
  search_string.send_keys(password)


  button_element = driver.find_element(By.ID, "kc-login").click()


  name_oowner = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ng-tns-c80-3')]"))).click()
  time.sleep(40)
  name_oowner1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Один Прекрасный Человек']"))).click()
  button1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@label='OK']"))).click()
  time.sleep(10)
  button2 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='plates-table__menu-button']"))).click()
  delete_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Удалить жильца']"))).click()
  choose_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Удалить']"))).click()
  time.sleep(5)

  modalka = driver.find_element(By.XPATH, "//div[text()='Жилец удален']").text
  if modalka != 'Жилец удален':
    raise ValueError('Жилец не удалён!')

  finish_time = datetime.datetime.now()
  spent_time = finish_time - start_time
  print(spent_time)
except Exception as ex:
 print(ex)
finally:
  driver.close()
  driver.quit()
