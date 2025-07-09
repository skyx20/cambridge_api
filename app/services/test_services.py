# from .fetcher import Fetcher
from .parser import Parser
from app.utils.utils import get_html_page

if __name__ == "__main__":
    page = get_html_page('mind')
    p = Parser(page)
    p.select_dictionary('uk')
    w = p.parse_meanings()
