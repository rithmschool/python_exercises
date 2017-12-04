# Blueprints 

### Part I - Questions

1. Describe the MVC pattern.

MVC stands for model, view and controller which describes an architectural design pattern for web applications. The model describes the data schema. The view is the template is what the user sees and is rendered to HTML. The controller is where all the logic happens. It talks witht he model to get data and updates the view/ 

2. In the MVC pattern, does the model communicate directly with the view?

No it does not. The controller is the intermediate which glues communication between the model and template.

2. What is the purpose of blueprints?

Blueprints helps organize our web app

3. How does using blueprints help us organize bigger applications?

Using blueprints can help us register and affiliate it with a certain subdomain. For example, we can assoiate user_blueprint with '/users'. In addition, we can assoiate templates with their respective controller/resource. redirect(url_for('users.index'))

### Part II - Exercise

1. Refactor your users and messages app to use blueprints.  Make sure to have a separate file for `models.py`, `views.py`, and `forms.py`. You should have a working 1 to Many application with blueprints when this exercise is complete!

2. Include the following flash messages (it's important you make sure these are exact so the tests will pass)
    - when a user is created, send a flash message of "User Created!"
    - when a user is updated, send a flash message of "User Updated!"
    - when a user is deleted, send a flash message of "User Deleted!"
    - when a message is created, send a flash message of "Message Created!"
    - when a message is updated, send a flash message of "Message Updated!"
    - when a message is deleted, send a flash message of "Message Deleted!"

3. If you have not added any styling or testing to your users and messages app, be sure to do so!
