from flask import Flask, render_template, session, redirect, url_for
from routes.auth import auth_bp
from routes.auction import auction_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(auction_bp, url_prefix='/auction')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html', username=session['username'])

if __name__ == '__main__':
    app.run(debug=True)