import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'b\'\xc5>`\xe3C\x19\x13\xdc\xeaV\xefT\x9d\xa4x\xae\''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT=True
    DEBUG=True

    mysql_db_host = os.environ.get("MYSQL_DB_HOST")
    mysql_db_uname = os.environ.get("MYSQL_DB_USERNAME")
    mysql_db_passwd = os.environ.get("MYSQL_DB_PASSWORD")
    mysql_db = os.environ.get("MYSQL_DATABASE")
    mysql_db_port = os.environ.get("MYSQL_DB_PORT")

    post_db_host = os.environ.get("POSTGRES_DB_HOST")
    post_db_uname = os.environ.get("POSTGRES_DB_USERNAME")
    post_db_passwd = os.environ.get("POSTGRES_DB_PASSWORD")
    post_db = os.environ.get("POSTGRES_DATABASE")
    post_db_port = os.environ.get("POSTGRES_DB_PORT")

    """ SQLAlchemy """
    MYSQL_URI = 'mysql+pymysql://' + mysql_db_uname + ':' + mysql_db_passwd + '@' + mysql_db_host + ':' + mysql_db_port + '/' + mysql_db
    POSTGRES_URI = 'postgresql+psycopg2://' + post_db_uname + ':' + post_db_passwd + '@' + post_db_host + ':' + post_db_port + '/' + post_db

    SQLALCHEMY_BINDS = {
        'mysql_db':  MYSQL_URI,
        'post_db': POSTGRES_URI
    }

