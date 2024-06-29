from ._imports import *
from app.models.member_model import MemberSearch, MemberCreate, MemberUpdate

import uuid


def search_member(db: Session, filters: MemberSearch, start=0, limit=10,
                  order: Union[List[str], None] = None,
                  columns: Union[List[str], None] = None):
    members, count = crud.member.get_multi(
        db, filters=filters.__dict__, skip=start,
        limit=limit, orders=order, columns=columns)
    
    for member in members:
        member.borrows
        for book in member.borrows:
            print(book)

    return members, count
