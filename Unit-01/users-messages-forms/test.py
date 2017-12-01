from app import app,db, User, Message
from flask_testing import TestCase
import unittest

class BaseTestCase(TestCase):
    def create_app(self):
        app.config['WTF_CSRF_ENABLED'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///testing.db'
        return app

    def setUp(self):
        db.create_all()
        user1 = User("Elie", "Schoppik")
        user2 = User("Tim", "Garcia")
        user3 = User("Matt", "Lane")
        db.session.add_all([user1, user2, user3])
        message1 = Message("Hello Elie!!", 1)
        message2 = Message("Goodbye Elie!!", 1)
        message3 = Message("Hello Tim!!", 2)
        message4 = Message("Goodbye Tim!!", 2)
        db.session.add_all([message1, message2, message3,message4])
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    def test_users_index(self):
        response = self.client.get('/users', content_type='html/text', follow_redirects=True)
        self.assertLess(response.status_code, 400)
        self.assertIn(b'Elie Schoppik', response.data)
        self.assertIn(b'Tim Garcia', response.data)
        self.assertIn(b'Matt Lane', response.data)

    def test_users_show(self):
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_users_create_correctly(self):
        response = self.client.post(
            '/users',
            data=dict(first_name="Awesome", last_name="Student"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Awesome', response.data)

    def test_users_create_incorrectly(self):
        response = self.client.post(
            '/users',
            data=dict(first_name="", last_name="Student"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This field is required', response.data)

    def test_users_edit(self):
        response = self.client.get(
            '/users/1/edit'
        )
        self.assertIn(b'Elie', response.data)
        self.assertIn(b'Schoppik', response.data)

    def test_users_update(self):
        response = self.client.patch(
            '/users/1?_method=PATCH',
            data=dict(first_name="updated", last_name="information"),
            follow_redirects=True
        )
        self.assertIn(b'updated information', response.data)
        self.assertNotIn(b'Elie Schoppik', response.data)

    def test_users_delete(self):
        response = self.client.delete(
            '/users/1?_method=DELETE',
            follow_redirects=True
        )
        self.assertNotIn(b'Elie Schoppik', response.data)

    #### TESTS FOR MESSAGES ####

    def test_messages_index(self):
        response = self.client.get('/users/1/messages', content_type='html/text', follow_redirects=True)
        self.assertLess(response.status_code, 400)
        self.assertIn(b'Hello Elie!!', response.data)
        self.assertIn(b'Goodbye Elie!!', response.data)

    def test_messages_show(self):
        response = self.client.get('/users/1/messages/1')
        self.assertEqual(response.status_code, 200)

    def test_messages_create_correctly(self):
        response = self.client.post(
            '/users/1/messages',
            data=dict(content="Hi Matt!!", user_id=3),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hi Matt!!', response.data)

    def test_messages_create_incorrectly(self):
        response = self.client.post(
            '/users/1/messages',
            data=dict(content=""),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This field is required', response.data)

    def test_messages_edit(self):
        response = self.client.get(
            '/users/1/messages/1/edit'
        )
        self.assertIn(b'Hello Elie!!', response.data)

        response = self.client.get(
            '/users/2/messages/4/edit'
        )
        self.assertIn(b'Goodbye Tim!!', response.data)

    def test_messages_update(self):
        response = self.client.patch(
            '/users/1/messages/1?_method=PATCH',
            data=dict(content="Welcome Back Elie!"),
            follow_redirects=True
        )
        self.assertIn(b'Welcome Back Elie!', response.data)

    def test_messages_delete(self):
        response = self.client.delete(
            '/users/1/messages/1?_method=DELETE',
            follow_redirects=True
        )
        self.assertNotIn(b'Hello Elie!!', response.data)


if __name__ == '__main__':
    unittest.main()
