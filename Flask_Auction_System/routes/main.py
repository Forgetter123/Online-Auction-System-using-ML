from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/terms')
def terms():
    return render_template('terms.html')

@main_bp.route('/privacy')
def privacy():
    return render_template('privacy.html')  

@main_bp.route('/payments')
def payments():
    return render_template('payment.html')

@main_bp.route('/notifications')
def notifications():
    return render_template('notifications.html')