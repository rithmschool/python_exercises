from app import app, db
# need to tell migrations WHAT app to make DB changes too, and then the app's DB

from flask_script import Manager
# Cmd line applications for managing DBs, that we can now write

from flask_migrate import Migrate, MigrateCommand
# the actual dependencies to do migrations

migrate = Migrate(app, db)
# connect flask migrate to our applications and db with Migrate class 

manager = Manager(app)
# initilize manager object to call with our app

manager.add_command('db',MigrateCommand)
# add CMD line application

if __name__=='__main__':
		manager.run()
