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
  tab_TC = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Транспортные средства']"))).click()
  button_edit = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//p-tieredmenu[contains(@class, 'ng-tns-c84-28')]"))).click()
  time.sleep(10)
  # type = WebDriverWait(driver, 20).until(
  #   EC.element_to_be_clickable((By.XPATH, "//div[@id='vehicleType']"))).click()
  # type1 = WebDriverWait(driver, 20).until(
  #   EC.element_to_be_clickable((By.XPATH, "//ul//li[@aria-label='Автомобиль']"))).click()
  # number_TC = WebDriverWait(driver, 20).until(
  #   EC.element_to_be_clickable((By.XPATH, "//div[@id='number']//input"))).send_keys('12345')
  # brand = WebDriverWait(driver, 10).until(
  #   EC.element_to_be_clickable((By.XPATH, "//div[@id='model']//input"))).send_keys('марка машины')
  # button_end = WebDriverWait(driver, 10).until(
  #   EC.element_to_be_clickable((By.XPATH, "//span[text()='Сохранить все изменения']"))).click()
  # time.sleep(5)
  # modalka = driver.find_element(By.XPATH, "//div[text()='Данные успешно добавлены.']").text
  # if modalka != 'Данные успешно добавлены.':
  #   raise ValueError('Транспортное средство не добавлено!')
  # finish_time = datetime.datetime.now()
  # spent_time = finish_time - start_time
  # print(spent_time)
except Exception as ex:
 print(ex)
finally:
  driver.close()
  driver.quit()
