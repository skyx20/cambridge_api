# Cambridge Api

## A simple api to get meanings of english words from cambridge dictionary for english language learnears

### Overview

This project is a Python-based program that extracts word meanings, guide words, and usage examples from the Cambridge Dictionary. Wrapped in FastAPI, it exposes the data as a JSON API. The core of the program uses requests for HTTP handling, BeautifulSoup for HTML parsing, and structured Word objects for clean data management. it was built as part of a chrome extension, another front-end project for quick access to the meanings. Check it out here: [Building]()

_supports only mono dictionary for now..._

### How to install.

- Clone the repo:
  `git clone https://github.com/skyx20/cambridge_api.git `
- create and activate your virtual enviroment and install all the dependencies.
  `pip install -r requirements.txt`

### How to run

```bash
    fastapi dev app/main.py # for development
```

### API

if you want to know how the api works and the data it retrieves, FastAPI provide an interactive api documentation, just run the app and go to the default api docs link: `http://127.0.0.1:8000/docs`. Or look for it in the console if you have that port unavailable.
for more information on how to use the docs, see the official [FastAPI Docs](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs)

<p align="center">
  <img src="./app/assets/images/fastapi-docs.png" width="450"/>
<p>

<br>

### Json pattern

```python
{
  "word": "word",
  "ipa": null,
  "audios": null,
  "meanings": [
    {
      "posType": "posType", #if a word isn't part of a guide word, this would be null
      "guideWordDefs": [
        {
          "guideWord": "guideWord",
          "meanings": [
            {
              "definition": "definition",
              "cerfLevel": "cerfLevel",
              "examples": [
                "Some examples"
              ]
            }
          ]
        },
      ]
    }]
}
```

Example:

```python
{
  "word": "mind",
  "ipa": null,
  "audios": null,
  "meanings": [
    {
      "posType": "noun",
      "guideWordDefs": [
        {
          "guideWord": "BE ANNOYED",
          "meanings": [
            {
              "definition": "(used in questions and negatives) to be annoyed or worried by something",
              "cerfLevel": "A2",
              "examples": [
                "Do you think he'd mind if I borrowed his book?",
                "I don't mind having a dog in the house so long as it's clean.",
                "I wouldn't mind (= I would like) something to eat, if that's OK",
              ]
            }
          ]
        },
      ]
    }]
}
```

### To-do:

- [ ] Add support for Audio pronunciation and IPA
- [ ] Add support for translations

### Known Issues

- [ ] The api can return whatever internal exepction is raised,

### Contribute

If you want contribute to this repo, just make a new fork or open a new issue to let me know.

### Disclaimer

The dictionary data provide by this project is sourced from a publicly available online dictionary. All data provided by this api is for non-profit personal or educational purposes and is intended for reference and learning purposes only. I do not claim ownership of the data nor do I guarantee its accuracy or completeness.

This project is not intended for commercial use, and I will not be held responsible for any infringement of commercial rights that may arise from the use of this data. Users of this project are solely responsible for their own use of the data and should ensure that they comply with all applicable laws and regulations.
