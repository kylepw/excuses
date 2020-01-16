import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'notsosecretkey')
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DB_SERVER = '???'

class DevelopmentConfig(Config):
    DEBUG = True
    DB_SERVER = 'localhost'

class TestingConfig(Config):
    DEBUG = True
    DB_SERVER = 'localhost'
    DATABASE_URI = 'sqlite:///:memory:'
