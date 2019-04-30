import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
    ##INSTRUCTION: Set up for your machine
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://esthermuingai:honeybee@localhost/eventsbuddy'
    DEBUG = True

class TestConfig(Config):
    ##INSTRUCTION: Set up for your machine
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://esthermuingai:honeybee@localhost/eventsbuddy_test'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
    pass


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}