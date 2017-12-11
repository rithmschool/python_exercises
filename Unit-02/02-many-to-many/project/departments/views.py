from flask import redirect, url_for, render_template, Blueprint, request
from project.models import Department, Employee
from project.departments.forms import NewDepartmentForm, DeleteForm
from project import db

departments_blueprint = Blueprint(
	'departments',
	__name__,
	template_folder = 'templates'
)