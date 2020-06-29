from unittest import TestCase, main
from unittest.mock import MagicMock
from sqlalchemy.orm.session import Session
from db.database import Database


class DatabaseClassTest(TestCase):
    db: Database

    def setUp(self) -> None:
        self.db = Database()
        Database.Base.metadata.create_all = MagicMock()

    def tearDown(self) -> None:
        Database.db_initialised = False
        self.db.Session = None

    def test__init_db_creates_tables(self):
        self.db.init_db()
        self.assertEqual(Database.Base.metadata.create_all.called, True)

    def test__init_db_only_creates_tables_once(self):
        self.db.init_db()
        self.db.init_db()
        Database.Base.metadata.create_all.assert_called_once()
        self.assertEqual(Database.Base.metadata.create_all.call_count, 1)

    def test__get_session_returns_a_new_session(self):
        session = self.db.get_session()
        self.assertIsInstance(session, Session)

    def test__get_session_creates_single_session(self):
        session1 = self.db.get_session()
        session2 = self.db.get_session()
        self.assertEqual(session1, session2)
        self.assertIs(session1, session2)


if __name__ == '__main__':
    main()
