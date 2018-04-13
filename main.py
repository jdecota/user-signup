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
    return render_template('Welcome.html', username = username)

app.run()
    

