from ._imports import *
# from app.libs.auth import get_hash, verify_hash
from app.schemas.member_schema import Member
from app.services import member_service as service
from app.models.member_model import MemberSearch
import uuid


class TestMemberAsync(TestsAsync):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        # self.loop.close()
        return super().tearDown()

    def test_search_member(self):
        db = SessionLocalAppTest()
        result = service.search_member(db, filters=MemberSearch())
        self.assertGreater(len(result[0]), 0)
        for member in result[0]:
            self.assertIsInstance(member, Member)

        db.close()
