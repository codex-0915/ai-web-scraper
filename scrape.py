import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
AUTH = 'USER:PASS'
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'

def scrape_website(website, unblock_website=False):
    """
    Scrapes a website using Selenium WebDriver.

    Parameters:
        website (str): The URL of the website to scrape.

    Returns:
        None
    """
    print("Launching chrome browser...")

    if unblock_website:
        print('Connecting to Scraping Browser...')
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
        with Remote(sbr_connection, options=ChromeOptions()) as driver:
            driver.get(website)
            # CAPTCHA handling
            print('Waiting for CAPTCHA to solve...')
            solve_res = driver.execute('executeCdpCommand', {
                'cmd': 'Captcha.waitForSolve',
                'params': {'detectTimeout': 10000},
            })
            print('CAPTCHA solve status: ', solve_res['value']['value'])
            print('Navigated! Scraping page content...')
            html = driver.page_source
            # print(html)

    else:
        # Update chromedriver depending on your OS and chrome version, to download the latest version, visit "https://googlechromelabs.github.io/chrome-for-testing/#stable"
        chrome_driver_path = "./chromedriver.exe"
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
        
        try:
            driver.get(website)
            print("Page loaded...")
            html = driver.page_source
            time.sleep(10)

            # return html
        finally:
            driver.quit()

    return html