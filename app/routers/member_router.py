from fastapi.encoders import jsonable_encoder
from ._imports import *
from app.models.member_model import MemberCreate, MemberUpdate, MemberSearch
from app.services import member_service as service

import sys

router = APIRouter(
    prefix="/member",
    tags=["Member"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"},
               400: {"description": "Bad Request"}},
)


@router.get('/', responses=http_response(200, ResultModel))
async def search_member(
        *,
        filters: MemberSearch = Depends(),
        start: int = 0,
        limit: int = 10,
        order: Union[List[str], None] = Query(
            default=None, description='<column_name> <desc/asc>. ex: name desc'),
        db: Session = Depends(get_db),
        response: Response,
):
    try:
        objs, count = service.search_member(
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

@router.post('/{member_code}/borrow/{book_code}', responses=http_response(200, ResultModel))
async def borrow_book(
        *,
        book_code:str,
        member_code:str,
        db: Session = Depends(get_db),
        response: Response
):
    try:
        obj = service.borrows(
            db, member_code, book_code)
        # return jsonable_encoder(member)
        return {'data': obj}
        # return ResultModel(data={'member': member}, count=count)
    except Exception as e:
        # print_debug(e)
        print(e)
        status_code, message = handle_exception(e)
        response.status_code = status_code
        return ResultModel(message=message)