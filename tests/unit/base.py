import unittest
from tests.utils import SessionLocalAppTest
from app.schemas.member_schema import Member
from app.schemas.borrow_schema import Borrow
import alembic.config
import alembic.command
# from app.libs.deps import config


class TestsAsync(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...
        db = SessionLocalAppTest()
        db.query(Member).update({Member.penalized_until: None})
        db.query(Borrow).delete()
        db.commit()
        db.close()

    def assertHasAttr(self, obj, intendedAttr):
        testBool = hasattr(obj, intendedAttr)

        # python >=3.8 only, see below for older pythons
        self.assertTrue(testBool, msg='obj lacking an attribute. obj: %s, intendedAttr: %s' % (
            obj, intendedAttr))
