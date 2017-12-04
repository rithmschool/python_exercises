# Blueprints 

### Part I - Questions

1. Describe the MVC pattern.
 Model- Where you create the Class that maps to the database
 View - What the user sees
 Controller - The logic of what to do: handles what data to get from the database, what actions to perform, and what view to give user
2. In the MVC pattern, does the model communicate directly with the view?
No, the Controller is the part that handles the logic
3. What is the purpose of blueprints?
The purpose of blueprints is to organize the app in a way that can scale as the project gets bigger
4. How does using blueprints help us organize bigger applications?
Instead of having a very long app.py file where it's difficult to find where info is located (since it includes forms, classes, and routing for all sections in one place), the sections are organized by folders named after the class name so that it is easy to find what you are looking for. It also helps with prefixing the url. 

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
