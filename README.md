# AI Web Scraper

This application scrapes the site based on the URL from user input, grabbing the DOM content, and allowing users to create a prompt where AI can grab that information from the website given. This app is created using Python language and tools such Selenium, BeatifulSoup, LangChain, & more!

## Commands

Create a python virtual environment

```
# For Windows OS
python -m venv ai
```

```
# For Other OS
python3 -m venv ai
```

Activate the virtual environment

```
# For Unix Terminal
source ai/Scripts/activate
```

```
# Or (depending on where the activate command is located)
source ai/bin/activate
```

```
# For Powershell
.\ai\Scripts\activate.ps1
```

```
# For Command Prompt
.\ai\Scripts\activate.bat
```

Run the website

```
# Run the streamlit website
streamlit run main.py
```

## TODO

### Plans / Steps

- [x] Create a simple streamlit user interface
- [x] Grab data to be scraped from the website (use Selenium)
- [x] Add unblocking of websites / captchas / ip bans (optional, use free credits from [BrightData](brightdata.com))
- [x] Create a sample .env file for the website unblocker
- [x] Test if website unblocker works
- [x] Clean the data to be passed to the LLMs
- [ ] Pass data to LLMs (ChatGPT? GPT-4? Llama3?)
- [ ] Parse the data from the LLM to get meaningful response/info
