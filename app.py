from flask import Flask, Blueprint, render_template, session, redirect, url_for
from routes.auth import auth_bp
from routes.auction import auction_bp
from routes.admin import admin_bp
from routes.main import main_bp
from routes.filters import timeuntil
from routes.ml_routes import ml_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(auction_bp, url_prefix='/auction')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(main_bp)
app.register_blueprint(ml_routes)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))  # Ensure the user is logged in

    user = {'username': session['username']}  # Example user data
    stats = {'active_bids': 10, 'completed_auctions': 5}  # Example statistics data

    return render_template('dashboard.html', user=user, stats=stats)

@app.template_filter('format_price')
def format_price(price):
    """Format price with two decimal places."""
    try:
        return f"${float(price):,.2f}"
    except (ValueError, TypeError):
        return "$0.00"
    
main_bp = Blueprint('main', __name__)  

app.jinja_env.filters['format_price'] = format_price
app.jinja_env.filters['timeuntil'] = timeuntil


if __name__ == '__main__':
    app.run(debug=True)