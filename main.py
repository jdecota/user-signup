from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config ['DEBUG']  

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/welcome', methods=['POST'])
def valid():
    username = request.form['username']
    username_error = ''
    password = request.form['password']
    password_error = ''

    # if username.count('') > 0                                          
    # username_error = 'No spaces are allowed in the username.'
    #username = ''
    if len(username) > 20:
        username_error = 'Maximum number of characters allowed is 20.'
    if len(username) < 3:
        username_error = "A minimum of 3 characters is required."
    #if  username = ''                                                         
    #    username_error = "Username is required."

    #if password(' ') > 0:                                         
    #   password_error = 'No spaces are allowed in the username.'
    if len(password) > 20:
        password_error = 'Passwords cannot exceed 20 characters.'
    #if len(password) < 1:                                                    #or could I use username = '' ? didn't work
    #   password_error = "Password Required."
    if len(password) < 3:
        password_error = "Password must have a minimum of 3 characters."


    if not username_error and not password_error:
        return render_template('Welcome.html', username = username,password=password)
    else:
        return render_template('form.html', username=username, username_error=username_error, password=password, password_error=password_error)

app.run()
    

