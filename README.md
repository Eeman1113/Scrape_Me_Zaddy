# Scrape_Me_Zaddy

## Overview

**Scrape_Me_Zaddy** is a simple Python web scraping tool built using BeautifulSoup and Streamlit. This tool allows users to scrape text content from a specified HTML tag and class on a given website.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Eeman1113/Scrape_Me_Zaddy.git
   cd Scrape_Me_Zaddy
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run scrape_me_zaddy.py
   ```

4. Enter the URL, HTML tag, class, and name in the provided input fields.

5. Click the "Submit" button to initiate the scraping process.

6. The scraped text will be displayed on the Streamlit app, and a text file with the scraped content will be saved in the `subbmition` directory.

## Example

```python
from bs4 import BeautifulSoup
import requests
import streamlit as st

def scrape_me(url, tag, class_, name):
    url = url
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    code_element = soup.find(tag, class_=class_)
    code = code_element.text.strip()

    f = open(f"./subbmition/{name}.txt", "w")
    f.write(code)
    f.close()
    st.write(code)

st.markdown("<h1 style='text-align: center; '>Scrape Me Up Zaddy 擦</h1>", unsafe_allow_html=True)

with st.form("my_form"):
    Url = st.text_input("Enter URL")
    Tag = st.text_input("Enter Tag")
    Class_ = st.text_input("Enter Class")
    Name = st.text_input("Enter Name")
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        scrape_me(Url, Tag, Class_, Name)
```

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** Make sure to use this tool responsibly and in compliance with the terms of service of the websites you are scraping.
