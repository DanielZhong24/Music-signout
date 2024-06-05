from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    #app is the flask app website
    app = Flask(__name__)
    app.config.from_object(Config)

    #db is the database
    db.init_app(app)
    with app.app_context():
        '''
        from app.view.newfolder.viewNew import new_bp
        app.resgister_blueprint(new_bp)
        '''
        from app.controller.StudentController import student_bp
        app.register_blueprint(student_bp)


        # Print all registered routes for debugging
        print(app.url_map)

        db.create_all()

    return app
