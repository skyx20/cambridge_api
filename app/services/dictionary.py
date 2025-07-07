from .parser import Parser
from .fetcher import Fetcher
from app.models.word import Word
from typing import Literal
from requests.exceptions import ConnectionError

class Dictionary:
    "Search in the dict by words variants like uk, us, or bussines"
    "default: uk."
    def __init__(self, variant:Literal["uk", "us", "be"]='uk'):
        self.variant = variant
        self._parser = None
        self._bridge = Fetcher()
        self._word_list :list[Word] = []

    def get_word_list(self):
        return self._word_list

    def search_meaning(self, word) -> Word:
        try:
            resp = self._bridge.get_word_page(word)
        except ConnectionError as e:
            return e
        else:
            self._parser = Parser(resp.text)
            self._parser.select_dictionary(self.variant)
            word = self._parser.parse_meanings()
            
        self._add_word(word)
        return word

    
    def _add_word(self, word: Word) -> None:
        self._word_list.append(word)
        
    def __str__(self):
        return f'Cambridge definitions for {self.variant} words'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.variant})'

