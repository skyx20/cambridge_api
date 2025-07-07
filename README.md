Cambridge Api
=============

## A simple api for getting meanings from cambridge dictionary for english learnears 

### Overview
This project is a Python-based program that extracts word meanings, guide words, and usage examples from the Cambridge Dictionary. Wrapped in FastAPI, it exposes the data as a JSON API. The core of the program uses requests for HTTP handling, BeautifulSoup for HTML parsing, and structured Word objects for clean data management. it was built as part of a chrome extension, another front-end project for quick access to the meanings. Check it out here: somelink

supports mono dictionary for now...


  
### How to install.
install all the dependencies in your virtual enviroment
```bash
    pip install -r requirements.txt
```
### How to run
```bash
    fastapi dev main.py # for development
    fastapi run main.py # for production
```
### Disclaimer
The dictionary data provide by this project is sourced from a publicly available online dictionary. All data provided by this api is for non-profit personal or educational purposes and is intended for reference and learning purposes only. I do not claim ownership of the data nor do I guarantee its accuracy or completeness.

This project is not intended for commercial use, and I will not be held responsible for any infringement of commercial rights that may arise from the use of this data. Users of this project are solely responsible for their own use of the data and should ensure that they comply with all applicable laws and regulations.


