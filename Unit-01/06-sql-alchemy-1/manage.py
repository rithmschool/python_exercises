from app import app,db 

from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

# connect flask_migrate to our application and SQLAlchemy instance
migrate = Migrate(app, db)

# Initialize the Manager with our application
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()