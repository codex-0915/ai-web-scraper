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

- [ ] Create a simple streamlit user interface
- [ ] Grab data to be scraped from the website (use Selenium)
- [ ] Pass data to LLMs (ChatGPT? GPT-4? Llama3?)
- [ ] Parse the data from the LLM to get meaningful response/info
