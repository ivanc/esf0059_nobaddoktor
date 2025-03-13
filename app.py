import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
from dbmodels import db, User#, Madre, Figlio
from blueprints.public import public_bp

load_dotenv() 


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)

app.register_blueprint(public_bp)


with app.app_context():
    db.create_all()
    # Crea un utente di prova (da rimuovere in produzione)
    if User.query.filter_by(username='test').first() is None:
        user = User(username='test')
        user.set_password('test')
        db.session.add(user)
        db.session.commit()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id)) 
    

app.run(debug=True)

