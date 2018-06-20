import os

SECRET_KEY = '\x91\x90\x05\t:,\xe1ym\xaa\xe9uFf\x8d\xd1s+\x11j\x10\x7f\xf2\x1f'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'rbtc18136839'
BLOG_DATABASE_NAME = 'flask_blog'
DB_HOST = os.getenv('IP', '127.0.0.1')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True