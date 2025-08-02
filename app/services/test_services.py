from re import search
from .fetcher import Fetcher
from .parser import Parser
from app.utils.utils import get_html_page
from pprint import pp, pprint
from app.utils.utils import get_html_page
from app.services.fetcher import Fetcher
from app.services.parser import Parser
from app.services.dictionary import Dictionary
from fastapi.responses import JSONResponse 
from fastapi.exceptions import HTTPException

if __name__ == "__main__":
    # f = Fetcher()
    # # page = f.get_word_page('option')
    # # p = Parser(page)
    # page = get_html_page('get')
    # p = Parser(page)
    # p.select_dictionary('uk')
    # w = p.parse_meanings()
    # pprint(w.to_json())
  
    def search_word(word: str, dict_variant = "uk"):
        d = Dictionary(dict_variant)
        try:
            # Testing
            page = get_html_page('stirred')
            p = Parser(page)
            p.select_dictionary('uk')
            w = p.parse_meanings()

            # w = d.search_meaning(word)
            pp(w.to_dict())
        except Exception as e:
            raise HTTPException(status_code=404, detail=e.__str__())
        else:
            word_data = w.to_dict()
            
            return JSONResponse(word_data, status_code=200)
    
    pprint(search_word('get'))