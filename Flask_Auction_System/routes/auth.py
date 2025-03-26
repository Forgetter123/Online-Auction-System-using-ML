from flask import Blueprint, render_template, request, redirect, url_for, session
import csv
import os
from werkzeug.utils import secure_filename

auth_bp = Blueprint('auth', __name__)
USERS_CSV = 'datasets/Users.csv'
UPLOAD_FOLDER = 'static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        document = request.files['document']
        filename = secure_filename(document.filename)
        document.save(os.path.join(UPLOAD_FOLDER, filename))

        with open(USERS_CSV, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, filename])
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open(USERS_CSV, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username and row[1] == password:
                    session['username'] = username
                    return redirect(url_for('dashboard'))
        return "Invalid credentials", 401
    return render_template('login.html')

@auth_bp.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))