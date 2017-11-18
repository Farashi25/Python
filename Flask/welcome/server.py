from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def welcome():
    return render_template('welcome.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/About')
def About():
    return render_template('About.html')
app.run(debug = True)