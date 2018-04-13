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
    # if username.count('') > 0                                          
    # username_error = 'No spaces are allowed in the username.'
    #username = ''
    if len(username) > 20:
        username_error = 'Maximum number of characters allowed is 20.'
    if len(username) < 3:
        username_error = "A minimum of 3 characters is required."
    #if  username == ''                                                         
     #   username_error = "Username is required."

    if not username_error:
        return render_template('Welcome.html', username = username)
    else:
        return render_template('form.html', username=username, username_error=username_error) 
        
app.run()
    

