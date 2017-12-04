from flask import render_template, url_for, redirect, request, flash, Blueprint
from project.users.forms import UserForm, DeleteForm
from project.users.models import User
from project import db

users_blueprint= Blueprint(
	'users',
	__name__,
	template_folder = 'templates/users'
	)

@users_blueprint
