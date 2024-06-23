from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from application import api_router, login_router, redirect_router
from settings import DESCRIPTION

app = FastAPI(
    title="CRUD-FASTAPI", version="0.1.0", description=DESCRIPTION, docs_url=None)

@app.get("/", include_in_schema=False)
async def index():
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="icon" type="image/x-icon" href="https://fastapi.tiangolo.com/img/favicon.png"><title>CRUD-API</title><script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script></head><body><rapi-doc spec-url="http://localhost:8000/openapi.json" show-header="false" theme="light"></rapi-doc></body></html>'  # noqa: E501
    return HTMLResponse(content=html, status_code=200)

app.include_router(login_router)
app.include_router(api_router)
app.include_router(redirect_router)
