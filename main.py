from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config ['DEBUG']  

@app.route('/')
def index():
    return render_template("signup.html")

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    username_error = ''
    password = request.form['password']
    password_error = ''
    verify_password = request.form['verify_password']
    verify_pass_error = ''
    email = request.form['email']
    email_error = ''

    if  ' ' in username:                                      
            username_error = 'No spaces are allowed.'
    if len(username) > 20:
            username_error = 'Maximum number of characters allowed is 20.'
    if len(username) > 0 and len(username) < 3:
            username_error = "A minimum of 3 characters is required."
    if (username.strip() == ''):                                                        
            username_error = "Username is required."

    if ' ' in password:                                         
       password_error = 'No spaces are allowed.'
    if len(password) > 20:
        password_error = 'Passwords cannot exceed 20 characters.'
    if len(password) < 1:                                                   
       password_error = "Password Required."
    if len(password) < 3 and len(password) > 0 :
        password_error = "Password must have a minimum of 3 characters."

    if verify_password != password:                                         
        verify_pass_error = "Passwords do not match."                      

    if ' ' in email:
        email_error = 'No spaces allowed'
    if email.count('@') > 1:
        email_error = 'Invalid Email'
    if email.count('.') > 1:                                        
        email_error = 'Invalid Email'
    if len(email) > 20:                                                          
        email_error = 'Maximum number of characters is 20'
    if len(email) == 1 or len(email) == 2:
        email_error = "A minimum of 3 characters is required"    

    if not username_error and not password_error and not verify_pass_error and not email_error:
        return render_template('welcome.html', username=username)

    else:
        return render_template('signup.html', username=username, username_error=username_error, 
        password=password, password_error=password_error, verify_password=verify_password, 
        verify_pass_error=verify_pass_error, email=email, email_error=email_error)

app.run()
    

