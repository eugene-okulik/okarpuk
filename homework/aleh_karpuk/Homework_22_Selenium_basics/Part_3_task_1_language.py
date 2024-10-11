from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from  time import sleep


chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.get('https://www.qa-practice.com/elements/select/single_select')


select_language_field = chrome_driver.find_element(By.XPATH, '//select[@name="choose_language"]')


dropdown = Select(select_language_field)
dropdown.select_by_value('5')


sleep(5)
