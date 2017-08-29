from app import app,db, Snack
from flask_testing import TestCase
import unittest

class BaseTestCase(TestCase):
    def create_app(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///testing.db'
        return app

    def setUp(self):
        db.create_all()
        snack1 = Snack("Hershey", "Chocolate")
        snack2 = Snack("Skittles", "Candy")
        snack3 = Snack("Chips Ahoy", "Cookie")
        db.session.add_all([snack1, snack2, snack3])
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    def test_index(self):
        response = self.client.get('/snacks', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hershey Chocolate', response.data)
        self.assertIn(b'Skittles Candy', response.data)
        self.assertIn(b'Chips Ahoy Cookie', response.data)

    def test_show(self):
        response = self.client.get('/snacks/1')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(
            '/snacks',
            data=dict(name="New", kind="Student"),
            follow_redirects=True
        )
        self.assertIn(b'New Student', response.data)

    def test_edit(self):
        response = self.client.get(
            '/snacks/1/edit'
        )
        self.assertIn(b'Hershey', response.data)
        self.assertIn(b'Chocolate', response.data)

    def test_update(self):
        response = self.client.patch(
            '/snacks/1',
            data=dict(name="updated", kind="information"),
            follow_redirects=True
        )
        self.assertIn(b'updated information', response.data)
        self.assertNotIn(b'Hershey Chocolate', response.data)

    def test_delete(self):
        response = self.client.delete(
            '/snacks/1',
            follow_redirects=True
        )
        self.assertNotIn(b'Hershey Chocolate', response.data)


if __name__ == '__main__':
    unittest.main()