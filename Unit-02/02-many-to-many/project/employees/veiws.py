from flask import Blueprint, url_for, redirect, render_template, request, flash
from project import db
from project.models import Employee

employees_blueprint = Blueprint(
	'employees',
	__name__,
	template_folder='templates/employees')