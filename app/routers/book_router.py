from fastapi.encoders import jsonable_encoder
from ._imports import *
from app.models.book_model import BookSearch
from app.services import book_service as service

import sys

router = APIRouter(
    prefix="/book",
    tags=["Book"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"},
               400: {"description": "Bad Request"}},
)


@router.get('/', responses=http_response(200, ResultModel))
async def search_book(
        *,
        filters: BookSearch = Depends(),
        start: int = 0,
        limit: int = 10,
        order: Union[List[str], None] = Query(
            default=None, description='<column_name> <desc/asc>. ex: name desc'),
        db: Session = Depends(get_db),
        response: Response,
):
    try:
        objs, count = service.search_book(
            db, filters, start, limit, order, None)
        # return jsonable_encoder(member)
        return {'data': objs}
        # return ResultModel(data={'member': member}, count=count)
    except Exception as e:
        # print_debug(e)
        print(e)
        status_code, message = handle_exception(e)
        response.status_code = status_code
        return ResultModel(message=message)
