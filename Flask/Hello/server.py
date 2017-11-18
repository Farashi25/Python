from flask import Flask, render_template, request, redirect
from datetime import datetime

app=Flask(__name__)
@app.route('/')
def Test():
    return render_template('Test.html', name ='Farashi', time = 5, phrase = "hello")


@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    print  name, email
    return redirect('/')
app.run(debug=True)
