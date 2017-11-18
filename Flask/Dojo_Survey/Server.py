from flask import Flask, render_template, request,redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app=Flask(__name__)
app.secret_key = 'KeepItPrivate'

@app.route('/')
def welcome():
    return render_template('dojo1.html')

@app.route('/result', methods =['POST'])
def submit():
    flag = True
    if len(request.form['email'])<1:
        flash("email cannot be blank!")
        flag = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        flag = False
    if len(request.form['name'])<1:
        flash("name cannot be empty!")
        flag = False
        
    if flag == False:
        return redirect('/')
    else:
        if flag:
            name = request.form['name']
            language = request.form['language']
            location = request.form['location']
            email = request.form['email']
            return render_template('dojo2.html', name = name, language = language, location = location, email = email )


app.run(debug = True)

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
