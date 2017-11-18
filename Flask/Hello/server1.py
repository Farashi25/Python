from flask import Flask, render_template
app=Flask(__name__)
@app.route('/assignment')
def assignment():
    return render_template('assignment.html')
app.run(debug=True)