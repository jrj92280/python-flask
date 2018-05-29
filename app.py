from flask_runner import Manager

from app import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()

# gunicorn -b 0.0.0.0:5000 app:app --log-file=- -R
