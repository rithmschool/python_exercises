import os

class Config(object):
    DEBUG = False
    TESTING = False
    # PORT=3001
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/flask-sql-blueprints'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # PORT = os.environ.get('PORT')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True