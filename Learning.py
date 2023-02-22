from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def browser_function():
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://target_website.com")