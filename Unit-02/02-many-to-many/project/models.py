from project import db

EmployeeDepartment = db.Table('employees_departments',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('department_id', db.Integer, db.ForeignKey('departments.id', ondelete='cascade')),
	db.Column('employee_id', db.Integer, db.ForeignKey('employees.id', ondelete='cascade')))

class Department(db.Model):

	__tablename__ = "departments"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	employees = db.relationship("Employee", 
		secondary=EmployeeDepartment,
		backref=db.backref("departments"))
	
	def __init__(self, name):
		self.name = name

class Employee(db.Model):

	__tablename__ = "employees"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

	def __init__(self, name):
		self.name = name




