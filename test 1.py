from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.set_page_load_timeout(10)
time.sleep(5)
driver.close()
driver.quit()
print("done")







# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# driver.get("https://www.google.com/")