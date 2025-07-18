from bs4 import BeautifulSoup
from pathlib import Path

"""
Used for testing
"""
def get_html_page(name):
    parent_path = Path(__file__).parent.parent
    file = f"{parent_path}/data/saved_pages/{name}_page.html"
    with open(file, "rb") as f:
        return f.read()


def save_page(word, word_page) -> None:
    parent_path = Path(__file__).parent.parent
    print('the parent path', parent_path)
    p_saved_pages = Path(parent_path) / "data" / "saved_pages"
    print('p_saved_pages', p_saved_pages)
    p_saved_pages.mkdir(parents=True, exist_ok=True)
    check = p_saved_pages / f"{word}_page.html"
    if not check.exists():
        check.touch()
        with open(check, "wb+") as f:
            f.write(word_page.content)

