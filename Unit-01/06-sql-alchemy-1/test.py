from snack import Snack
from app import app, snack_list
import unittest

class TestSnackMethods(unittest.TestCase):

    def setUp(self):
        snack_list.append(Snack('snickers', 'chocolate'))
        snack_list.append(Snack('skittles', 'candy'))

    def tearDown(self):
        snack_list.clear()
        Snack.id = 1

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/snacks', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_new(self):
        tester = app.test_client(self)
        response = tester.get('/snacks/new', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        tester = app.test_client(self)
        response = tester.get('/snacks/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_show(self):
        tester = app.test_client(self)
        response = tester.get('/snacks/1/edit', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_creating_snack(self):
      tester = app.test_client(self)
      tester.post('/snacks',
                        data=dict(name="hersheys", kind="chocolate"), follow_redirects = True)
      self.assertEqual(snack_list[2].id, 3)
      self.assertEqual(snack_list[2].name, 'hersheys')
      self.assertEqual(snack_list[2].kind, 'chocolate')
      self.assertEqual(len(snack_list), 3)

    def test_editing_snack(self):
      tester = app.test_client(self)
      tester.post('/snacks/1?_method=PATCH',
                        data=dict(name="almond_snickers", kind="almonds_and_chocolate"), follow_redirects = True)
      self.assertEqual(snack_list[0].name, 'almond_snickers')
      self.assertEqual(snack_list[0].kind, 'almonds_and_chocolate')
      self.assertEqual(len(snack_list), 2)

    def test_deleting_snack(self):
      tester = app.test_client(self)
      tester.post('/snacks/1?_method=DELETE', follow_redirects = True)
      tester.post('/snacks/2?_method=DELETE', follow_redirects = True)
      self.assertEqual(len(snack_list), 0)

if __name__ == '__main__':
    unittest.main()
