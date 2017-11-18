# from flask import Flask, render_template,redirect, request, session, flash
# app =Flask(__name__)
# app.secret_key = 'keepitsecretkeepitsafe'
# @app.route('/')
# def index():
#     return render_template('index.html')
# @app.route('/process',methods =['POST'])
# def process():
#     if len(request.form['name'])<1:
#         flash("name cannot be empty!")
#     else:
#         flash("Success! Your name is {}".format(request.form['name']))
#     return redirect('/')
# app.run(debug=True)


from flask import Flask, render_template,redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app =Flask(__name__)
app.secret_key = 'SecretSecretSecret'
@app.route('/', methods=['GET'])
def index():
    return render_template('index1.html')
@app.route('/process',methods =['POST'])
def submit():
    if len(request.form['email'])<1:
        flash("email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)
