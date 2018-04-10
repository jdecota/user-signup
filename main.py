from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config ['DEBUG']
    

@app.route('/')
def index():
    return render_template('form.html')

#@app.route('/inputs', methods = ['POST'])
#def inputs():
  #  username = request.form['username']                             #Define placeholders
  #  password = request.form['password']
  #  verify_password = request.form['verify_password']
  #  email = request.form['email']

  #  username_error = request.form['username_error']
  #  password_error = request.form['password_error']
  #  verify_pass_error = request.form['verify_pass_error']
  #  email_error = request.form['email_error']  

app.run()
    

