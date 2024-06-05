import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL') or 
        'mysql+pymysql://sql5711794:Nzq1yYlshK@sql5.freesqldatabase.com/sql5711794'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
