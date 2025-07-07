import requests as req
from requests.models import Response
from app.utils.utils import save_page
from fake_useragent import UserAgent


BASE_URL = "https://dictionary.cambridge.org/dictionary/english/"

class Fetcher:
    def __init__(self, user_agent=None) -> None:
        self.__url = BASE_URL
        self.user_agent = user_agent if user_agent else UserAgent().random
        self.html_content = ""

    def get_word_page(self, word: str) -> Response:
        # It makes a http get request to the cambridge dictionary to parse the html doc later on.
        endpoint = self.__url + word
        headers = {
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",               
        }

        try:
            s = req.Session()
            resp = s.get(endpoint, headers=headers, timeout=10)
            resp.raise_for_status()
        except req.exceptions.HTTPError as e:
            print(f"HTTP error: {e} - Status Code: {resp.status_code}")
        except req.exceptions.Timeout:
            print("Request timed out")
        except req.exceptions.ConnectionError:
            print("Connection error")
        except req.exceptions.RequestException as e:
            print(f"General error: {e}")
        else:
            if resp.url == BASE_URL:
                raise req.exceptions.HTTPError('word not found')
            self.html_content = resp.text
            # Using a util to save the pages for testing porpose
            # save_page(word, resp)
            return resp


if __name__ == "__main__":
    f = Fetcher()
    resp = f.get_word_page("get")
