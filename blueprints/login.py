from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from werkzeug.security import generate_password_hash
from dbmodels import db, User#, Madre, Figlio

login_bp = Blueprint("auth", __name__,
                      template_folder='templates',
                      url_prefix="/auth") # sarà anteposto a tutti gli URL associati al blueprint.'auth'__name__url_prefix

@login_bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        ruser = User.query.filter_by(username='test').first()
        if ruser and ruser.check_password(password):
           pass
        else:
            print(f"login failed : {username}")
            abort(401)
    else:
        try:
            return render_template('auth/index.html')
            #abort(501)
        except TemplateNotFound as error :
            print( f"TemplateNotFound Error: ")
            print( error )           
            abort(404)
        
@login_bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif len(password) < 8:
            error = 'Password must be at least 8 characters long.'

        if error is None:
            try:
              if User.query.filter_by(username='test').first() is None:
                user = User(username='test')
                user.set_password('test')
                db.session.add(user)
                db.session.commit() 
                return redirect(url_for("auth.login"))
              else:
                  error = f"User {username} is already registered."
            except Exception as error:
                print(f"ERROR: {error}")
                
        else:
            return redirect(url_for("auth.login"))

        flash(error)
    try:
        return render_template('auth/register.html')
    except TemplateNotFound as error :
        print( f"TemplateNotFound Error: ")
        print( error )
        abort(404)