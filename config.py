POSTGRESQL = 'postgresql+psycopg2://postgres:Manu3155@localhost/blogposts_db'

class Config:
    DEBUG = False
    SECRET_KEY = '32devClaveSecret66'

    SQLALCHEMY_DATABASE_URI = POSTGRESQL

    CKEDITOR_PKG_TYPE = 'full'