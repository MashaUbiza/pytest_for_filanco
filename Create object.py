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
  directory_url = panel_url + "handbook/object-directory"

  driver.get(directory_url)
  print('panel_url: ', panel_url)
  print(directory_url)
  if directory_url == panel_url:
    raise ValueError('Страница не загрузилась!')

  user = config.get('AUTHORIZATION_PARAMS', 'user')
  password = config.get('AUTHORIZATION_PARAMS', 'password')
  print('user: ', user)
  print('password: ', password)

  user_string = driver.find_element(By.NAME, "username").send_keys(user)
  password_string = driver.find_element(By.NAME, "password").send_keys(password)
  button_element = driver.find_element(By.ID, "kc-login").click()

  button1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "addObject"))).click()

  new_RC = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, "div#quarterNew input"))).send_keys('Тест 657')

  address = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#address input"))).send_keys('Длинный адрес с цифрами')
  index = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#postcode input"))).send_keys('644123')
  ID = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, '********-****-****-****-************')]"))).send_keys('11111111-2222-3333-4444-555555555555')

  type_object = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#houseType > div > p-dropdown > div > span"))).click()
  type_object1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Жилой дом']"))).click()

  series = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, "div#series input"))).send_keys('123')

  date_ready = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, "div#readyFrom input"))).click()
  date_ready1 = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.XPATH, "//span[text()='10']"))).click()
  time.sleep(5)
  description = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#description textarea"))).send_keys('Любое')
  name_UK = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#companyId > div > p-dropdown > div > span"))).click()
  name_UK1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='УК Прекрасная компания']"))).click()
  manager = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#managerId > div > p-dropdown > div > span"))).click()
  manager1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Фамилия1 Имя1 Отчество1']"))).click()

  all_area = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#areaAll input"))).send_keys('1')
  living_area = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#areaLiving input"))).send_keys('2')
  MOP_area = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#areaMOP input"))).send_keys('3')
  commercial_area = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#areaCommercial input"))).send_keys('4')
  parking_area = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#areaParking input"))).send_keys('5')

  button2 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Сохранить и перейти к Шагу 2']"))).click()

  entrances = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH,"//input[@formcontrolname='entrances']"))).send_keys('5')

  floors = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='floors']"))).send_keys('5')
  apartments = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='apartments']"))).send_keys('5')
  button3 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'pi-refresh')]"))).click()

  button4 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Сохранить и перейти к Шагу 3']"))).click()

  button5 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Сохранить']"))).click()
  time.sleep(10)
  modalka = driver.find_element(By.XPATH, "//div[text()='Данные успешно добавлены.']").text

  if modalka != 'Данные успешно добавлены.':
    raise ValueError('Объект не добавлен!')
  finish_time = datetime.datetime.now()
  spent_time = finish_time - start_time
  print(spent_time)


except Exception as ex:
 print(ex)
finally:
  driver.close()
  driver.quit()
