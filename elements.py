import elements
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
# googlSearchBox = driver.find_element(By.ID,"APjFqb")
# googlSearchBox.send_keys("automation")
# googlSearchBox.send_keys(Keys.RETURN)
# time.sleep(2)
driver.get("https://trytestingthis.netlify.app/")


driver.find_element(By.ID,"fname").send_keys("ahsaan")
driver.find_element(By.ID,"lname").send_keys("hassan")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
time.sleep(5)

