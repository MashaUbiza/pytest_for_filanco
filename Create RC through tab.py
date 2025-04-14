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

  user_string = driver.find_element(By.NAME, "username").send_keys(user)
  password_string = driver.find_element(By.NAME, "password").send_keys(password)
  button_element = driver.find_element(By.ID, "kc-login").click()
  name_oowner = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ng-tns-c80-3')]"))).click()
  name_oowner1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Один1 Прекрасный1 Человек1']"))).click()
  button1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@label='OK']"))).click()
  time.sleep(3)
  oowner = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//td[text()=' Один1 Прекрасный1 Человек1']"))).click()
  button_add = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Добавить объект']"))).click()
  type = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='targetTable']"))).click()
  type1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Квартира']"))).click()
  RC = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='cachedTargetQuarterId']//span"))).click()
  RC1 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Зоопарк']"))).click()
  address = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='cachedTargetHouseId']"))).click()
  address1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Тест 29']"))).click()
  flat = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='targetId']"))).click()
  flat1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='3']"))).click()
  status = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='ownStatus']"))).click()
  status1 = WebDriverWait(driver, 20).until(
  EC.element_to_be_clickable((By.XPATH, "//span[text()='Собственник']"))).click()
  button_end = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Сохранить все изменения']"))).click()
  time.sleep(5)
  modalka = driver.find_element(By.XPATH, "//div[text()='Данные успешно добавлены.']").text
  if modalka != 'Данные успешно добавлены.':
    raise ValueError('Связанный объект не добавлен!')
  finish_time = datetime.datetime.now()
  spent_time = finish_time - start_time
  print(spent_time)
except Exception as ex:
 print(ex)
finally:
  driver.close()
  driver.quit()
