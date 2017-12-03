# Blueprints 

### Part I - Questions

1. Describe the MVC pattern.
The MVC pattern separates concerns into data retrieval and manipulation, information and pages passed to the client, and the controller which contains the business logic and serves as a go between for the view and the model.
2. In the MVC pattern, does the model communicate directly with the view?
No, the controller is responsible for handling the results of the queries and passing them in a usable format to the view. 
2. What is the purpose of blueprints?
Blueprints abstract complex routing and accessing templates.
3. How does using blueprints help us organize bigger applications?
Blueprints help with the separation of concerns and structuring relationships between different resources.

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
