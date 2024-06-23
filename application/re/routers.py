from fastapi import APIRouter
from fastapi.responses import RedirectResponse, Response

from application.db.repository import URLRepository
from application.db.session import session
from short.application import ctrl

from .background import count_access

router = APIRouter(
    prefix="/r"
)

@router.get("/{slug}", tags=["redirect"], summary="Redirect by Slug")
async def redirect(slug: str):
    if slug:
        url_crtl = ctrl.Short(URLRepository(session))
        url = url_crtl.url(slug=slug)
        print(url.long_url)
        if not url:
            return Response(status_code=404)

        return RedirectResponse(url=url.long_url, background=count_access)
        # this type of background do not accept passing param to function.
        # 😢

    return