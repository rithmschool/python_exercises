from app import app
from db import create_snack
from flask_testing import TestCase
import unittest
import psycopg2

class BaseTestCase(TestCase):
    def create_app(self):
        conn = psycopg2.connect("dbname=flask-sql-snacks-test")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS snacks (id serial PRIMARY KEY, name text, kind text);")
        conn.commit()
        conn.close()
        return app

    def setUp(self):
        create_snack("hershey", "chocolate")

    def tearDown(self):
        conn = psycopg2.connect("dbname=flask-sql-snacks-test")
        cur = conn.cursor()
        cur.execute("DROP TABLE snacks;")
        conn.commit()
        conn.close()

    def test_index(self):
        response = self.client.get('/snacks', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'hershey chocolate', response.data)

    def test_show(self):
        response = self.client.get('/snacks/1')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(
            '/snacks',
            data=dict(name="New", kind="Snack"),
            follow_redirects=True
        )
        self.assertIn(b'New Snack', response.data)

    def test_edit(self):
        response = self.client.get(
            '/snacks/1/edit'
        )
        self.assertIn(b'hershey', response.data)
        self.assertIn(b'chocolate', response.data)

    def test_update(self):
        response = self.client.post(
            '/snacks/1?_method=PATCH',
            data=dict(name="updated", kind="information"),
            follow_redirects=True
        )
        self.assertIn(b'updated information', response.data)
        self.assertNotIn(b'hershey chocolate', response.data)

    def test_delete(self):
        response = self.client.post(
            '/snacks/1?_method=DELETE',
            follow_redirects=True
        )
        self.assertNotIn(b'hershey chocolate', response.data)


if __name__ == '__main__':
    unittest.main()
