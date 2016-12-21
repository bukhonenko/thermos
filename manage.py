from thermos import app, db
from thermos.models import User
from flask_script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username='alex', email='alex@gmail.com', password='test'))
    db.session.add(User(username='luke', email='luke@gmail.com', password='test'))
    db.session.commit()
    print 'Initialized the database!'


@manager.command
def dropdb():
    if prompt_bool("Are you sure to lose your data?"):
        db.drop_all()
        print('Dropped and lost!')

if __name__ == '__main__':
    manager.run()
