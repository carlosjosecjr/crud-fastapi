import random
import string

from fastapi import APIRouter, Depends, HTTPException, status

from application.api.schemas import CreateURLRequest, CreateURLResponse, ShortURLCreated
from application.db.repository import URLRepository
from application.db.session import session
from application.middleware.jwt import token_handler
from settings import MAX_SLUG_SIZE
from short.application import ctrl

router = APIRouter(prefix="/api")


@router.post(
    "/short/create",
    response_model=CreateURLResponse,
    tags=["short"],
    summary="Create Short Link",
)
async def create_link(
    create_url: CreateURLRequest, token: any = Depends(token_handler)
):
    slug: str = create_url.custom_slug
    usr = token.get("user_id")

    url_ctrl = ctrl.Short(storage=URLRepository(session))

    if not create_url.custom_slug:
        slug: str = url_ctrl.slug()

    u = url_ctrl.create_link(usr, str(create_url.long_url), slug)
    print(u)

    return CreateURLResponse(
        message="created",
        status_code=201,
        short=ShortURLCreated(
            long_url=create_url.long_url, short_url=f"http://localhost:8000/re/{slug}"
        ),
    )


@router.delete("/short/{slug}", tags=["short"], summary="Delete Short Link")
async def delete_slug(slug: str, token: any = Depends(token_handler)):
    usr = token.get("user_id")

    url_ctrl = ctrl.Short(storage=URLRepository(session))
    url = url_ctrl.delete_link(slug, usr)

    return {
        "message": "short link deleted",
        "status_code": 200,
        "url": {
            "id": url.id,
            "long_url": url.long_url,
            "slug": url.short_url,
            "created_at": url.created_at,
        },
    }


@router.get("/stats", tags=["stats"], summary="Get All Short Link Stats")
async def all_stats(token: any = Depends(token_handler)):
    pass


@router.get("/stats/{slug}", tags=["stats"], summary="Get Stats By Slug")
async def stats(slug: str, token: any = Depends(token_handler)):
    pass
