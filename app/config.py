import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Main settings
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'wc2tb4qamclo)at@x=1@y8o!n4(#9tp@0&=-l768u9g))9lnt)' # super random string

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
