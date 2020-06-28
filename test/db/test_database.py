from unittest import TestCase, main
from db.database import Database


class DatabaseClassTest(TestCase):

    def test__init_db_creates_tables(self):
        self.assertEqual(True, False)

    def test__init_db_only_creates_tables_once(self):
        self.assertEqual(True, False)

    def test__get_session_returns_a_new_session(self):
        self.assertEqual(True, False)

    def test__returns_a_different_session_every_time(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    main()
