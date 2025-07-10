from .fetcher import Fetcher
from .parser import Parser
from app.utils.utils import get_html_page
from pprint import pp, pprint

if __name__ == "__main__":
    # f = Fetcher()
    # resp = f.get_word_page('head')

    page = get_html_page('head')
    p = Parser(page)
    p.select_dictionary('us')
    w = p.parse_meanings()
    pprint(w.to_json())
