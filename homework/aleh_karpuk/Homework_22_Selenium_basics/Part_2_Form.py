from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.get('https://demoqa.com/automation-practice-form')


first_name = 'Aleh'
last_name = 'Karpuk'
e_mail = 'okarpuk@example.com'
mobile_number = '1234567890'
date_of_birth = '1 Jul 1985'
subjects_name = 'Math'
current_address = 'Test city, Test street, 1 - 999'
state_entry = 'Haryana'
city_entry = 'Karnal'


first_name_field = chrome_driver.find_element(By.XPATH, '//input[@id="firstName"]')
last_name_field = chrome_driver.find_element(By.XPATH, '//input[@id="lastName"]')
e_mail_field = chrome_driver.find_element(By.XPATH, '//input[@id="userEmail"]')
male_gender_radiobutton = chrome_driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
mobile_field = chrome_driver.find_element(By.XPATH, '//input[@id="userNumber"]')
date_of_birth_field = chrome_driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]')
subjects_field = chrome_driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
hobbies_sport_checkbox = chrome_driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
hobbies_music_checkbox = chrome_driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
current_address_field = chrome_driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
state_dropdown = chrome_driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
city_dropdown = chrome_driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
submit_button = chrome_driver.find_element(By.XPATH, '//button[@id="submit"]')


first_name_field.send_keys(first_name)
last_name_field.send_keys(last_name)
e_mail_field.send_keys(e_mail)
male_gender_radiobutton.click()
mobile_field.send_keys(mobile_number)

entered_value = date_of_birth_field.get_attribute('value')
for _ in range((len(entered_value))-1): # если удалить дату полностью, то получим белый экран (БАГ). Пришлось так.
    date_of_birth_field.send_keys(Keys.BACKSPACE)

date_of_birth_field.send_keys(date_of_birth)
date_of_birth_field.send_keys(Keys.ESCAPE)
subjects_field.send_keys(subjects_name)
subjects_field.send_keys(Keys.ENTER)
chrome_driver.execute_script("arguments[0].scrollIntoView(true);", hobbies_sport_checkbox) # без прокрутки периодически падает, т.к. не видит элемент
hobbies_sport_checkbox.click()
hobbies_music_checkbox.click()
current_address_field.send_keys(current_address)
current_address_field.send_keys(Keys.ESCAPE)
state_dropdown.send_keys(state_entry)
state_dropdown.send_keys(Keys.ENTER)
city_dropdown.send_keys(city_entry)
city_dropdown.send_keys(Keys.ENTER)
submit_button.click()


main_table = chrome_driver.find_element(By.XPATH, '//div[@class="table-responsive"]')

rows = main_table.find_elements(By.TAG_NAME, 'tr')
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        print(cell.text)
