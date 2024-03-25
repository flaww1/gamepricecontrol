import os

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or '35464'
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqldb://root:@localhost/gamepricecontrol') 
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = 'salt'

   # mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('APP_MAIL_USERNAME', 'gpricecontrol@gmail.com')
    MAIL_PASSWORD = os.environ.get('APP_MAIL_PASSWORD', 'gamepricecontrol12345')

    # mail accounts
    MAIL_DEFAULT_SENDER = 'gpricecontrol@gmail.com'
