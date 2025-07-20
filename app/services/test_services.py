from .fetcher import Fetcher
from .parser import Parser
from app.utils.utils import get_html_page
from pprint import pp, pprint
from app.services.dictionary import Dictionary
from fastapi.exceptions import HTTPException 
from fastapi.responses import JSONResponse 
from typing import Literal


if __name__ == "__main__":
    f = Fetcher()
    # page = f.get_word_page('option')
    # p = Parser(page)
    # page = get_html_page('option')
    # p = Parser(page)
    # p.select_dictionary('us')
    # w = p.parse_meanings()
    # pprint(w.to_json())
    word = 'option'
    dict_variant:Literal['uk', 'us', 'be'] = 'uk'
    def search_word(word: str, dict_variant:Literal['uk', 'us', 'be']):
        d = Dictionary(dict_variant)
        try:
            w = d.search_meaning(word)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=e.__str__())
        else:
            word_data = w.to_dict()
            return JSONResponse(word_data, status_code=200)
            
    search_word(word, dict_variant)