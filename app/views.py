from flask import render_template, flash, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from .models import User

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    nickname = request.form.get('signup_nickname')
    email = request.form.get('signup_email')
    password = request.form.get('signup_password')
    confirm = request.form.get('signup_password_2')
    if not all([nickname, email, password, confirm]) or (password != confirm):
        return render_template('sign.html', error='Something goes wrong!')
    user = User(
        nickname=nickname,
        email=email,
        password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return render_template('sign.html', message='Welcome!')
        
        
@app.route('/signin', methods=['POST'])
def signin():
    if session.get('auth_user_id'):
        return render_template('sign.html', message="You're authorized already! <br> <a href='/signout'>Log Out</a>")
    email = request.form.get('signin_email')
    password = request.form.get('signin_password')
    user = User.query.filter_by(email=email).first()
    if user is None:
        return render_template('sign.html', error='User doesn\'t exists')
    if check_password_hash(user.password, password):
        session['auth_user_id'] = user.id
        return render_template('sign.html', message='Hello again!')
    return render_template('sign.html', error='Wrong e-mail or password!')


@app.route('/signout')
def signout():
    if 'auth_user_id' in session:
        del session['auth_user_id']
    return render_template('sign.html', message='Goodbye!')
        
@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    return render_template('gallery.html')
