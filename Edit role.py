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
  role_url = panel_url + "/handbook/roles-accesses"

  driver.get(role_url)
  print('panel_url: ', panel_url)
  print(role_url)

  user = config.get('AUTHORIZATION_PARAMS', 'user')
  password = config.get('AUTHORIZATION_PARAMS', 'password')
  print('user: ', user)
  print('password: ', password)

  search_string = driver.find_element(By.NAME, "username")

  search_string.send_keys(user)
  search_string = driver.find_element(By.NAME, "password")
  search_string.send_keys(password)


  button_element = driver.find_element(By.ID, "kc-login").click()
  name_role = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ng-tns-c79-6')]"))).click()
  time.sleep(10)

  name_role1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//li[text()='Любой специалист']"))).click()
  # time.sleep(10)
  button1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@label='ОК']"))).click()
  time.sleep(5)
  # button2 = WebDriverWait(driver, 20).until(
  #   EC.element_to_be_clickable((By.XPATH, "//td[text()='Любой специалист']"))).click()
  # time.sleep(5)



  # button_end= WebDriverWait(driver, 10).until(
  #    EC.element_to_be_clickable((By.XPATH, "//span[text()='Создать Роль']"))).click()

  # modalka = driver.find_element(By.XPATH, "//div[text()='Роль успешно создана']").text
  # print("Test result; ", modalka =='Роль успешно создана')
  # finish_time = datetime.datetime.now()
  # spent_time = finish_time - start_time
  # print(spent_time)
except Exception as ex:
 print(ex)
finally:
  driver.close()
  driver.quit()
