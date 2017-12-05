from project import db

EmployeeDepartment = db.Table('employee_departments',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('department_id', db.Integer, db.ForeignKey('departments.id', ondelete='cascade')),
	db.Column('employee_id', db.Integer, db.ForeignKey('employees.id', ondelete='cascade')))

class Department(db.Model):

	__tablename__ = "departments"

	id = db.Column(db.Integer, primary_key=True)
	department_name = db.Column(db.Text)
	employees = db.relationship("Employee", 
		secondary=EmployeeDepartment,
		backref=db.backref("departments"))
	

	def __init__(self, department_name)
		self.department_name = department_name

class Employee(db.Model):

	__tablename__ = "emloyees"

	id = db.Column(db.Integer, primary_key=True)
	employee_name = db.Column(db.Text)

	def __init__(self, employee_name)
		self.employee_name = employee_name




