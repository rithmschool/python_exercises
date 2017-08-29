from project import app

if __name__ == '__main__':
    app.run(debug=True, port=3000)


# from flask import Flask, request, redirect, render_template, url_for, flash, abort
# from flask_modus import Modus
# from flask_sqlalchemy import SQLAlchemy
# import os
# from forms import NewUser, NewMessage




# @app.route('/users', methods=['GET', 'POST'])
# def index():
#     form = NewUser(request.form)
#     if request.method == 'POST':
#       if form.validate() == True:
#           user = User(form.username.data, form.email.data, 
#             form.first_name.data, form.last_name.data, form.image_url.data)
#           db.session.add(user)
#           db.session.commit()

#           flash("New User Created!")
#           return redirect(url_for('index'))
#       else:
#           return render_template('users/new.html', form=form)
    
#     users = User.query.order_by(User.id)
#     return render_template('users/index.html', users = users)

# @app.route('/users/new')
# def new():
#     form = NewUser(request.form)
#     return render_template('users/new.html', form=form)

# @app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
# def show(id):
#     user = User.query.get(id)
#     if user is None:
#         abort(404)

#     if (request.method == b'PATCH'):
#         form = NewUser(request.form)
#         user.username = form.username.data
#         user.email = form.email.data, 
#         user.first_name = form.first_name.data
#         user.last_name = form.last_name.data
#         user.image_url = form.image_url.data
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('index'))

#     if (request.method == b'DELETE'):
#         db.session.delete(user)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('users/show.html', user=user)

# @app.route('/users/<int:id>/edit')
# def edit(id):
#     user = User.query.get(id)
#     if user is None:
#         abort(404)

#     form = NewUser(obj=user)
#     return render_template('users/edit.html', id=user.id, form=form)

# @app.route('/users/<int:user_id>/messages', methods=['GET', 'POST'])
# def index_messages(user_id):
#     form = NewMessage(request.form)
#     username = User.query.get(user_id).username
#     if username is None:
#         abort(404)

#     if request.method == 'POST':
#       if form.validate() == True:
#           user_message = Message(form.message.data, user_id)
#           db.session.add(user_message)
#           db.session.commit()
#           flash("New Message Created!")
#           return redirect(url_for('index_messages', user_id=user_id))
#       else:
#           return render_template('messages/new.html', user_id=user_id, form=form)

#     user_messages = Message.query.filter(Message.user_id == user_id).all()
    
#     return render_template('messages/index.html', user_id=user_id, username=username, user_messages=user_messages)

# @app.route('/users/<int:user_id>/messages/new')
# def new_message(user_id):
#     form = NewMessage(request.form)
#     return render_template('messages/new.html', user_id=user_id, form=form)

# @app.route('/users/<int:user_id>/messages/<int:message_id>/edit')
# def edit_messages(user_id, message_id):
#     message = Message.query.get(message_id)
#     if message is None:
#         abort(404)

#     form = NewMessage(obj=message)
#     return render_template('messages/edit.html', user_id=user_id, message_id=message.id, form=form)

# @app.route('/users/<int:user_id>/messages/<int:message_id>/show', methods=['GET', 'PATCH', 'DELETE'])
# def show_message(user_id, message_id):
#     message = Message.query.get(message_id)
#     if message is None:
#         abort(404)

#     if (request.method == b'PATCH'):
#         form = NewMessage(request.form)
#         message.message = form.message.data
#         db.session.add(message)
#         db.session.commit()
#         return redirect(url_for('index_messages', user_id=user_id))

#     if (request.method == b'DELETE'):
#         db.session.delete(message)
#         db.session.commit()
#         return redirect(url_for('index_messages', user_id=user_id))
#     return render_template('messages/show.html', message=message)

# if __name__ == '__main__':
#     app.run(debug=True)













