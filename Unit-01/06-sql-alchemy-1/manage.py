from app import app,db 

# let's import the Manager class from flask_script 
# which comes with flask_migrate. We will use this 
# for adding a terminal command to run our migrations. 
from flask_script import Manager

# from flask_migrate we need the Migrate class to initialize 
# our application and db variable from SQLAlchemy. 
# We also need MigrateCommand to work with the Manager class 
# to determine what command will run our migrations.
from flask_migrate import Migrate, MigrateCommand

# connect flask_migrate to our application and SQLAlchemy instance
migrate = Migrate(app, db)

# Initialize the Manager with our application
manager = Manager(app)

# Add a command line command called 'db' which will 
# allow us to use all the built in commands to flask_migrate
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()