import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    """
    Scrapes a website using Selenium WebDriver.

    Parameters:
        website (str): The URL of the website to scrape.

    Returns:
        None
    """
    print("Launching chrome browser...")

    # Update chromedriver depending on your OS and chrome version, to download the latest version, visit "https://googlechromelabs.github.io/chrome-for-testing/#stable"
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()