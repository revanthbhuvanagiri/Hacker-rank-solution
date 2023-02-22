from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("Revanth")

search_button = driver.find_element(By.LINK_TEXT,"No thanks")
search_button.submit()