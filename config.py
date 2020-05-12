import os

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or '35464'
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqldb://root:@localhost/gamepricecontrol') 
    #SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+mysqlconnector://root:@localhost/gamepricecontrol')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False