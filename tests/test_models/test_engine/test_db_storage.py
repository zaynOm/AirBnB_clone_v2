#!/usr/bin/python3
"""Module for testing db storage"""
from models.engine.db_storage import DbStorage
from models.base_model import Base
from os import environ
import unittest
from models.state import State


class Test_db_storage(unittest.TestCase):
    """Test cases for the db storage engine"""

    @staticmethod
    def run_setup_mysql_script():
        """run the sql script to make sure test database is up"""
        from MySQLdb import connect

        conn = connect(host="localhost", user="root", password="root")
        cur = conn.cursor()

        script_file = "setup_mysql_test.sql"
        with open(script_file, encoding="utf-8") as f:
            cur.execute(f.read())

    def setUp(self):
        """ """
        environ["HBNB_ENV"] = "test"
        environ["HBNB_TYPE_STORAGE"] = "db"
        environ["HBNB_MYSQL_DB"] = "hbnb_test_db"
        environ["HBNB_MYSQL_USER"] = "hbnb_test"
        environ["HBNB_MYSQL_PWD"] = "hbnb_test_pwd"
        environ["HBNB_MYSQL_HOST"] = "localhost"
        from os import getenv

        self.run_setup_mysql_script()

        self.storage = DbStorage()
        # self.storage.reload()

    # def test_all_empty(self):
    #     """"""
    #     all_objs = self.storage.all()
    #     self.assertDictEqual(all_objs, {})


    # def test_all(self):
    #     """"""
    #     s = State()
    #     self.assertIn(s, self.storage.all())
