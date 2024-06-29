from ._imports import *
from app.models.book_model import BookSearch

import uuid


def search_book(db: Session, filters: BookSearch, start=0, limit=10,
                  order: Union[List[str], None] = None,
                  columns: Union[List[str], None] = None):
    books, count = crud.book.get_multi(
        db, filters=filters.__dict__, skip=start,
        limit=limit, orders=order, columns=columns)
    
    # for member in books:
    #     # member.borrows
    #     member.books_borrowed = len(member.borrows)
    #     for borrow in member.borrows:
    #         borrow.book

    return books, count
