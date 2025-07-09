from fastapi import APIRouter
from app.services.dictionary import Dictionary
from fastapi.responses import JSONResponse 
from fastapi.exceptions import HTTPException 

router = APIRouter(
    prefix="/search",
    tags=["search"]
)

@router.get("/{word}/",)
async def search_word(word: str, dict_variant='uk'):
    d = Dictionary(dict_variant)
    try:
        w = d.search_meaning(word)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.__str__())
    else:
        word_data = w.to_dict()
        return JSONResponse(word_data, status_code=200)

