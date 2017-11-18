from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'Wall')
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app=Flask(__name__)
app.secret_key = 'KeepItPrivate'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods =['POST'])
def submit():
    flag = True
    if len(request.form['email'])<1:
        flash("email cannot be blank!")
        flag = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        flag = False
    if len(request.form['first_name'])<1:
        flash("name cannot be empty!")
        flag = False
    if not request.form['first_name'].isalpha():
        flash("name can't contain numbers")
        flag = False
    if len(request.form['last_name'])<1:
        flash("name cannot be empty!")
        flag = False
    if len(request.form['password'])<8:
        flash('password too short')
        flag = False
    if request.form['password']!= request.form['password_confirm']:
        flash("Password does not match")
        flag = False

    if flag == False:
        return redirect('/')
    else:
        if flag:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['pwd_confirm']

            return render_template('index.html', first_name = first_name, last_name = last_name, password = password, email = email, pwd_confirm = confirm_password)



app.route('/')
def index():
    query = "SELECT * FROM users"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
    friends = mysql.query_db("SELECT * FROM users")
    print friends
    return render_template('index.html')

@app.route('/friends/<friend_id>')
def show(friend_id):
    query = "SELECT * FROM users WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    print friends
    return render_template('index.html', one_friend=friends[0])


@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name,  :email, :password, NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'password': request.form['password']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    print 'hello'
    return redirect('/')
# def create():
#     print request.form['first_name']
#     print request.form['last_name']
#     print request.form['occupation']
#     # add a friend to the database!
#     return redirect('/')
app.run(debug=True)

# from flask import Flask, render_template, request, redirect, session
# app = Flask(__name__)
# app.secret_key = 'ThisisSecret'
# @app.route('/')
# def index():
#   return render_template("dojo2.html")
# @app.route('/users', methods=['POST'])
# def create_user():
#    print "Got Post Info"
#    session['name'] = request.form['name']
#    session['email'] = request.form['email']
#    # notice how the key we are using to access the info corresponds with the names
#    # of the inputs from our html form
#    name = request.form['name']
#    email = request.form['email']
#    return redirect('/') # redirects back to the '/' route
# @app.route('/show')
# def show_user():
#   return render_template('dojo2.html', name=session['name'], email=session['email'])
# app.run(debug=True)
