from flask_migrate import MigrateCommand
from flask_script import Manager
from app import create_app

#this is the bone of this website
app=create_app()

#this is a app manager
manager=Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()

