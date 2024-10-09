from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.get('https://www.qa-practice.com/elements/input/simple')
input_data = 'Test_input'
text_string = chrome_driver.find_element(By.XPATH, '//input[@placeholder="Submit me"]')
text_string.send_keys(input_data)
text_string.send_keys(Keys.ENTER)
result_text = chrome_driver.find_element(By.XPATH, '//p[@id="result-text"]')
print(result_text.get_attribute("innerText"))
