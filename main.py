import os
import time
from dotenv import load_dotenv, dotenv_values
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

load_dotenv(override= True)

URL = "https://internshala.com/student/dashboard"
EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("PASSWORD")

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_option)
driver.get(url= URL)

# time.sleep(2)
email_field = driver.find_element(By.ID, value= "email")
email_field.send_keys(EMAIL)

password_field = driver.find_element(By.ID, value="password")
password_field.send_keys(PASSWORD)

# time.sleep(2)
login_button = driver.find_element(By.ID, value="login_submit")
login_button.click()

intership_session = driver.find_element(By.LINK_TEXT, value="Internships")
intership_session.click()

close_pop_ups = driver.find_element(By.ID, value="close_popup") 
close_pop_ups.click()

seleting = driver.find_element(By.ID, value='categoryOptions').click()
selecting_value = Select(driver.find_element(By.ID, value='select_category'))
# selecting_value.select_by_value("python%2Fdjango")
texts = [i.text for i in selecting_value.options]
print(texts)

