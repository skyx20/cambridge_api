from .fetcher import Fetcher
from .parser import Parser
from app.utils.utils import get_html_page
from pprint import pp, pprint

if __name__ == "__main__":
    f = Fetcher()
    # page = f.get_word_page('option')
    # p = Parser(page)
    page = get_html_page('option')
    p = Parser(page)
    p.select_dictionary('uk')
    w = p.parse_meanings()
    pprint(w.to_json())
  