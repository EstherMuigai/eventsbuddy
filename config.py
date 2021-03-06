import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

##class DevConfig(Config):
    ##INSTRUCTION: Set up for your machine
    ##SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://U_NAME:PASSWORD@localhost/DB_NAME'
    DEBUG = True

## TestConfig(Config):
    ##INSTRUCTION: Set up for your machine
    ##INSTRUCTION: Set up for your machine
    ##SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://U_NAME:PASSWORD@localhost/TEST_DB_NAME

class ProdConfig(Config):
    pass


config_options = {
##'development':DevConfig,
'production':ProdConfig,
##'test':TestConfig
}