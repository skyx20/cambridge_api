from fastapi import FastAPI
from app.services.dictionary import Dictionary
from fastapi.responses import JSONResponse 
from fastapi.exceptions import HTTPException 
from fastapi.responses import RedirectResponse
from .routers import search


app = FastAPI(
    debug=True,
    )
app.include_router(search.router)


@app.get("/")
async def root():
    RedirectResponse("docs")


