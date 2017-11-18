from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def Form():
  return render_template("Form.html")
@app.route('/users', methods=['POST'])
def create_user():
   name = request.form['name']
   print  name
   return redirect('/')
app.run(debug=True)
