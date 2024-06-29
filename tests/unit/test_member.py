from datetime import date, timedelta
from app.schemas.book_schema import Book
from app.schemas.borrow_schema import Borrow
from ._imports import *
# from app.libs.auth import get_hash, verify_hash
from app.schemas.member_schema import Member
from app.services import member_service as service
from app.models.member_model import MemberSearch
import uuid


class TestMemberAsync(TestsAsync):
    def setUp(self) -> None:
        self.db = SessionLocalAppTest()
        return super().setUp()

    def tearDown(self) -> None:
        # self.loop.close()
        self.db.close()
        return super().tearDown()

    def test_search_member(self):
        # db = SessionLocalAppTest()
        result = service.search_member(self.db, filters=MemberSearch())
        self.assertGreater(len(result[0]), 0)
        for member in result[0]:
            self.assertIsInstance(member, Member)

        # db.close()

    def test_borrow_book_exception(self):
        # test book not exist
        with self.assertRaises(Exception) as e:
            result = service.borrows(
                self.db, member_code='M001', book_code='XXX-1')
        self.assertIsInstance(e.exception, HTTPException)
        self.assertEqual(404, e.exception.status_code)

        # test member not exist
        with self.assertRaises(Exception) as e:
            result = service.borrows(
                self.db, member_code='M005', book_code='JK-45')
        self.assertIsInstance(e.exception, HTTPException)
        self.assertEqual(404, e.exception.status_code)

        # both not exist
        with self.assertRaises(Exception) as e:
            result = service.borrows(
                self.db, member_code='M005', book_code='XXX-1')
        self.assertIsInstance(e.exception, HTTPException)
        self.assertEqual(404, e.exception.status_code)

        # member currently borrow 2 books
        member1 = self.db.query(Member).filter(Member.id == 1).first()
        book1 = self.db.query(Book).filter(Book.id == 1).first()
        borrow1 = Borrow()
        borrow1.book = book1
        borrow1.member = member1
        borrow1.date = date.today()
        book2 = self.db.query(Book).filter(Book.id == 2).first()
        borrow2 = Borrow()
        borrow2.book = book2
        borrow2.member = member1
        borrow2.date = date.today()

        self.db.add(borrow1)
        self.db.add(borrow2)
        self.db.commit()

        with self.assertRaises(Exception) as e:
            result = service.borrows(
                self.db, member_code='M001', book_code='TW-11')
        self.assertIsInstance(e.exception, HTTPException)
        self.assertEqual(401, e.exception.status_code)

        # book currently borrowed by other member
        member2 = self.db.query(Member).filter(Member.id == 2).first()
        with self.assertRaises(Exception) as e:
            result = service.borrows(
                self.db, member_code='M002', book_code='JK-45')
        self.assertIsInstance(e.exception, HTTPException)
        self.assertEqual(401, e.exception.status_code)

        # member is penalized
        member3 = self.db.query(Member).filter(Member.id == 3).first()
        member3.penalized_until = date.today()+timedelta(days=3)
        self.db.add(member3)
        self.db.commit()
        with self.assertRaises(Exception) as e:
            result = service.borrows(
                self.db, member_code='M003', book_code='TW-11')
        self.assertIsInstance(e.exception, HTTPException)
        self.assertEqual(401, e.exception.status_code)

    def test_borrow_book(self):
        result = service.borrows(
            self.db, member_code='M001', book_code='JK-45')
        self.assertEqual(result.date, date.today())
        self.assertFalse(result.is_returned)
        self.assertEqual(result.member.code, 'M001')
        self.assertEqual(result.book.code, 'JK-45')
