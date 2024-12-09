
import  pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com/")
    googlSearchBox = driver.find_element(By.ID,"APjFqb")
    googlSearchBox.send_keys("automation")
    googlSearchBox.send_keys(Keys.RETURN)
    time.sleep(2)
    print("test completed")






