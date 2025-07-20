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
        w = d.search_meaning(word)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=e.__str__())
    else:
        word_data = w.to_dict()
        return JSONResponse(word_data, status_code=200)
    
    # return JSONResponse({'detail': 'word not found'}, status_code=404)
    # Testing
    # try:
        
    #     page = get_html_page('get')
    #     p = Parser(page)
    #     p.select_dictionary('uk')
    #     w = p.parse_meanings()
    # except Exception as e:
    #     raise HTTPException(status_code=404, detail=e.__str__())
    # else:
    #     word_data = w.to_dict()
    #     return JSONResponse(word_data, status_code=200)

