from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock database
users = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users:
            flash('Email already registered!')
        else:
            users[email] = {'password': password, 'verified': False}
            flash('Sign up successful! Please log in.')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/confirm_token', methods=['GET', 'POST'])
def confirmToken():
    return render_template('confirm_token.html')

@app.route('/home', methods=['GET', 'POST'])
def success():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
