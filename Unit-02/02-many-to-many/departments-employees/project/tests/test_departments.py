from flask_testing import TestCase
from project import app, db
from project.models import Department
import unittest
import bs4

class BaseTestCase(TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        db.create_all()
        d1 = Department("Finance")
        d2 = Department("IT")
        d3 = Department("Marketing")
        d4 = Department("Software")
        d5 = Department("Sales")
        db.session.add_all([d1,d2,d3,d4,d5])
        db.session.commit()

    def testDepartments(self):
        resp = self.client.get('/departments/')
        self.assertEquals(resp.status_code,200)

    def testDepartmentData(self):
        resp = self.client.get('/departments/')
        soup = bs4.BeautifulSoup(resp.data, "html.parser")
        departments = [p.text.strip().split('|')[0].strip() for p in soup.select("p.department")]
        for dep in Department.query.all():
            self.assertEquals(dep.name in departments, True)

if __name__ == '__main__':
    unittest.main()
