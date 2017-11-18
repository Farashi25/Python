from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "No ninjas here."

@app.route('/ninja')
def ninja():
    return render_template("Ninja2.html")

@app.route('/ninja/<ninja_color>')
def color(ninja_color):
    print ninja_color
    return render_template("Ninja.html",color=str(ninja_color))

app.run(debug = True)
