from fastapi import APIRouter
from app.services.dictionary import Dictionary
from fastapi.responses import JSONResponse 
from fastapi.exceptions import HTTPException 
from typing import Literal
# testing
from app.utils.utils import get_html_page
from app.services.fetcher import Fetcher
from app.services.parser import Parser

router = APIRouter(
    prefix="/search",
    tags=["search"]
)

@router.get("/{word}/{dict_variant}",)
async def search_word(word: str, dict_variant:Literal['uk', 'us', 'be']):
    d = Dictionary(dict_variant)
    try:
        word = word.lower().strip()
        w = d.search_meaning(word)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=e.__str__())
    else:
        word_data = w.to_dict()
        return JSONResponse(word_data, status_code=200)
    