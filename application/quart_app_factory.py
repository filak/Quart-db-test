import quart_flask_patch
from quart import Quart, render_template

def create_app(use_db=False):

    app = Quart(__name__)

    if use_db:
        #from flask_sqlalchemy import SQLAlchemy
        from quart_sqlalchemy import SQLAlchemy
        db = SQLAlchemy() 

        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

        class User(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String, unique=True, nullable=False)

        db.init_app(app)
        db.drop_all()
        db.create_all()        

    @app.route('/')
    async def intro():
        return await render_template('index.html')

    return app  



