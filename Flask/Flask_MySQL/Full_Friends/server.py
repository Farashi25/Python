from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')



@app.route('/')
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
    query = "INSERT INTO users (first_name, last_name, occupation, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, :email, :password, NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
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
