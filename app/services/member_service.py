from app.schemas.borrow_schema import Borrow
from app.schemas.member_schema import Member
from app.schemas.book_schema import Book
from ._imports import *
from app.models.member_model import MemberSearch, MemberCreate, MemberUpdate
from datetime import date

import uuid


def search_member(db: Session, filters: MemberSearch, start=0, limit=10,
                  order: Union[List[str], None] = None,
                  columns: Union[List[str], None] = None):
    members, count = crud.member.get_multi(
        db, filters=filters.__dict__, skip=start,
        limit=limit, orders=order, columns=columns)

    for member in members:
        # member.borrows
        member.books_borrowed = len(member.borrows)
        for borrow in member.borrows:
            borrow.book

    return members, count


def borrows(db: Session, member_code: str, book_code: str):
    member: Member = crud.member.get_by_code(db, member_code)
    book: Book = crud.book.get_by_code(db, book_code)
    if book and member:
        # check if member borrow more than 2 or
        # if book is borrowed by other member
        if len(member.borrows) >= 2 or len(book.borrowed_by) > 0:
            raise borrow_limit_exception
        # check if member is penalized
        if member.penalized_until and member.penalized_until > date.today():
            raise member_penalized_exception
        borrow = Borrow()
        borrow.book = book
        borrow.member = member
        borrow.date = date.today()
        db.add(borrow)
        db.commit()
        db.refresh(borrow)
        return borrow

    else:
        raise not_found_exception


def returns(db: Session, member_code: str, book_code: str):
    member: Member = crud.member.get_by_code(db, member_code)
    book: Book = crud.book.get_by_code(db, book_code)
    borrow: Borrow = db.query(Borrow).filter(Borrow.book == book,
                                             Borrow.member == member,
                                             Borrow.is_returned == False).first()
    # check if this user borrow this book
    if borrow:
        # check if returned after 7 days
        if date.today() > borrow.date + timedelta(days=7):
            # add penalty
            member.penalized_until = date.today()+timedelta(days=3)
            db.add(member)

        borrow.is_returned = True
        db.add(borrow)
        db.commit()
        db.refresh(borrow)
        return borrow
    else:
        return not_found_exception
