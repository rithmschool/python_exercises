from flask import render_template, url_for, redirect, request, flash, Blueprint
from project.messages.forms import MessageForm, DeleteForm
from project.messages.models import Message
from project import db

messages_blueprint= Blueprint(
	'messages',
	__name__,
	template_folder = 'templates/messages'
	)