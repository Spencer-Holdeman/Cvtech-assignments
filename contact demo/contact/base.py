from flask import render_template, Blueprint, request, session, redirect
from . import db

base = Blueprint('base', __name__)

class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

@base.route('/', methods=['POST', 'GET'])
def hello():
    # db.session.query(Users).delete()
    # db.session.commit()
    if request.method == 'POST':
        user_data = request.form
        email = user_data.get('email')
        password = user_data.get('password')
        username = user_data.get('username')
        account_info: list = [email, password, username]
        print(account_info)
        user = Users(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        session['email'] = email
        session['password'] = password
        session['username'] = username
        print('here: hello(inside if)')
        return redirect('saved')
    print('here: hello(outside if)')
    return render_template('index.html')

@base.route('/saved')
def saved():
    if 'email' in session:
        print('here: saved(inside if)')
        return render_template('saved.html', users=Users.query.all())
    print('here: saved(outside if)')
    return 'you have not logged in'

@base.route('/logout')
def logout():
    print('here: logout')
    session.pop('username', None)
    session.pop('password', None)
    session.pop('email', None)
    return redirect('/')

@base.route('/logoutuser')
def logoutuser():
    print('here: logoutuser')
    session.pop('username', None)
    session.pop('password', None)
    session.pop('email', None)
    db.session.query(Users).delete()
    db.session.commit()
    return render_template('index.html')