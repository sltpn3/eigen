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

    def test_borrow_book_member_not_found(self):
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
