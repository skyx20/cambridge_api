Cambridge Api
=============

## A simple api for getting meanings from cambridge dictionary for english learnears 

### Overview
This project is a Python-based program that extracts word meanings, guide words, and usage examples from the Cambridge Dictionary. Wrapped in FastAPI, it exposes the data as a JSON API. The core of the program uses requests for HTTP handling, BeautifulSoup for HTML parsing, and structured Word objects for clean data management. it was built as part of a chrome extension, another front-end project for quick access to the meanings. Check it out here: somelink

supports mono dictionary for now...


  
###### How to install.
install all the dependencies in your virtual enviroment
```bash
    pip install -r requirements.txt
```
###### How to run
```bash
    fastapi dev main.py # for development
    fastapi run main.py # for production
```
## 
