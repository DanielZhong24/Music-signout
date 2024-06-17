from flask import Flask , request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
db = SQLAlchemy()
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    from app.model.UserModel import User
    return User.query.get(int(user_id))
def create_app():
    #app is the flask app website
    app = Flask(__name__)
    app.config.from_object(Config)

    #db is the database
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'
    #check active page
    def is_active_page(page):
        return 'active' if request.path == page else ''
    @app.after_request
    def add_header(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    app.jinja_env.globals.update(is_active_page=is_active_page)
    with app.app_context():
        '''
        from app.view.newfolder.viewNew import new_bp
        app.resgister_blueprint(new_bp)
        '''
        from app.controller.AuthController import auth_bp
        from app.controller.StudentController import student_bp
        from app.controller.InstrumentController import instrument_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(student_bp)
        app.register_blueprint(instrument_bp)

        db.create_all()

    return app
