import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")
unblock_website = False

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(url, unblock_website)
    print(result)
