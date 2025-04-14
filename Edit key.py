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
  access_url = panel_url + "handbook/access"

  driver.get(access_url)
  print('panel_url: ', panel_url)
  print(access_url)

  user = config.get('AUTHORIZATION_PARAMS', 'user')
  password = config.get('AUTHORIZATION_PARAMS', 'password')
  print('user: ', user)
  print('password: ', password)

  search_string = driver.find_element(By.NAME, "username")

  search_string.send_keys(user)
  search_string = driver.find_element(By.NAME, "password")
  search_string.send_keys(password)


  button_element = driver.find_element(By.ID, "kc-login").click()
  search_string1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[contains(@formcontrolname, 'keyUserName')]"))).send_keys('Фамилия Имя Отчество')
  # time.sleep(5)
  button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='OK']"))).click()
  time.sleep(5)
  button1 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'pi pi-ellipsis-h')]"))).click()
  edit_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Редактировать']"))).click()
  time.sleep(5)
  button2 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout-main/div/div[2]/ng-component/app-edit-access-key-modal/p-dialog/div/div/div[2]/form/div[8]/button/span"))).click()
  time.sleep(5)
  # customer_button = driver.find_element(By.XPATH, "/html/body/app-root/app-layout-main/div/div[2]/ng-component/app-edit-access-key-modal/app-edit-access-key-user-modal/p-dialog/div/div/div[2]/form/div[2]/p-radiobutton[2]/label").click()
  # time.sleep(3)
  # modalka = driver.find_element(By.XPATH, "//div[text()='Ключ доступа создан']").text
  # print("Test result; ", modalka =='Ключ доступа создан')
  # finish_time = datetime.datetime.now()
  # spent_time = finish_time - start_time
  # print(spent_time)


except Exception as ex:
 print(ex)
finally:
  driver.close()
  driver.quit()
