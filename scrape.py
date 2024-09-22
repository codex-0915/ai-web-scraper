import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

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
        print("Connecting to Scraping Browser...")
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
        with Remote(sbr_connection, options=ChromeOptions()) as driver:
            driver.get(website)
            print("Waiting captcha to solve...")
            solve_res = driver.execute(
                "executeCdpCommand",
                {
                    "cmd": "Captcha.waitForSolve",
                    "params": {"detectTimeout": 10000},
                },
            )
            print("Captcha solve status:", solve_res["value"]["status"])
            print("Navigated! Scraping page content...")
            html = driver.page_source

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

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body

    # Check if body_content exists
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Checking for script and style tags and getting rid of those tags
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get all of the text and then separate it by new lines
    cleaned_content = soup.get_text(separator="\n")
    # Remove any unnecessary spaces and new lines inside the texts
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]