from flask import Blueprint, render_template
import csv

admin_bp = Blueprint('admin', __name__)
USERS_CSV = 'datasets/Users.csv'
AUCTION_CSV = 'datasets/auction_data.csv'

@admin_bp.route('/admin')
def admin_panel():
    users = []
    auctions = []
    
    with open(USERS_CSV, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            users.append({'username': row[0]})
    
    with open(AUCTION_CSV, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            auctions.append({'item_name': row[1]})
    
    return render_template('admin.html', users=users, auctions=auctions, fraud_bidders=[])