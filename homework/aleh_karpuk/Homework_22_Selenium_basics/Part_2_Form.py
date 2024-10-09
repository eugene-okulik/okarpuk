from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.get('https://demoqa.com/automation-practice-form')

first_name = 'Aleh'
last_name = 'Karpuk'
e_mail = 'okarpuk@example.com'
mobile_number = '1234567890'
date_of_birth = '1 Jun 1985'
subjects_name = 'Math'
current_address = 'Test city, Test street, 1 - 999'

first_name_field = chrome_driver.find_element(By.XPATH, '//input[@id="firstName"]')
last_name_field = chrome_driver.find_element(By.XPATH, '//input[@id="lastName"]')
e_mail_field = chrome_driver.find_element(By.XPATH, '//input[@id="userEmail"]')
male_gender_radiobutton = chrome_driver.find_element(By.XPATH, '//input[@id="gender-radio-1"]')
mobile_field = chrome_driver.find_element(By.XPATH, '//input[@id="userNumber"]')
date_of_birth_field = chrome_driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]')
subjects_field = chrome_driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
hobbies_sport_checkbox = chrome_driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-1"]')
hobbies_music_checkbox = chrome_driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-3"]')
current_address_field = chrome_driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')

state_dropdown = Select(chrome_driver.find_element(By.ID, 'state'))
city_dropdown = Select(chrome_driver.find_element(By.ID, 'city'))

submit_button = chrome_driver.find_element(By.XPATH, '//button[@id="submit"]')

first_name_field.send_keys(first_name)
last_name_field.send_keys(last_name)
e_mail_field.send_keys(e_mail)
male_gender_radiobutton.click()
mobile_field.send_keys(mobile_number)
date_of_birth_field.send_keys(date_of_birth)
subjects_field.send_keys(subjects_name)
hobbies_sport_checkbox.click()
hobbies_music_checkbox.click()
current_address_field.send_keys(current_address)
state_dropdown.select_by_visible_text("Haryana")
city_dropdown.select_by_visible_text("Karnal")
submit_button.click()


sleep(5)






# print(result_text.get_attribute("innerText"))