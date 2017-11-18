from flask import Flask, render_template, request, session,redirect

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    try:
        session['times'] += 1
    except:
        session['times'] = 1
    return render_template("counter.html")

@app.route('/add2', methods = ['POST'])
def plustwo():
    print 'adding two...'
    session['times'] += 1
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    print 'resetting...'
    session['times'] = 0
    return redirect('/')

app.run(debug = True)
