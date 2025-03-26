from flask import Blueprint, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from flask import jsonify, request, session
from flask import current_app
from flask_wtf.csrf import generate_csrf
from math import ceil
import random
import csv
import os
import time

auction_bp = Blueprint('auction', __name__)
AUCTION_CSV = 'datasets/auction_data.csv'
BIDS_CSV = 'datasets/bids.csv'
UPLOAD_FOLDER = 'static/uploads/'
WATCHLIST_CSV = "datasets/watchlist.csv"  # New file to store watched items
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@auction_bp.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        item_name = request.form['item_name']
        category = request.form['category']
        item_condition = request.form['item_condition']
        starting_price = request.form['starting_price']
        image = request.files['image']
        auction_duration = request.form['auction_duration']
        
        filename = secure_filename(image.filename)
        image.save(os.path.join(UPLOAD_FOLDER, filename))
        
        item_id = str(int(time.time()))
        
        with open(AUCTION_CSV, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([item_id, item_name, category, item_condition, starting_price, 0, 0, auction_duration, 0, ""])
        
        return redirect(url_for('auction.view_auctions'))
    
    return render_template('add_item.html')

@auction_bp.route('/auctions')
def view_auctions():
    auctions = []
    with open(AUCTION_CSV, 'r') as file:
        reader = csv.DictReader(file)
        next(reader, None)  # Skip header
        for row in reader:
            try:
                duration_days = int(row['auction_duration'].split()[0])  # Extract the number from '3 Days'
            except ValueError:
                duration_days = 3  # Default value if parsing fails

            # Assume the auction started randomly in the past 30 days
            start_time = datetime.now() - timedelta(days=random.randint(1, 30))
            end_time = start_time + timedelta(days=duration_days)

            auctions.append({
                'item_id': row['item_id'],
                'item_name': row['item_name'],
                'category': row['category'],
                'item_condition': row['item_condition'],
                'starting_price': row['starting_price'],
                'final_price': row['final_price'],
                'bids_count': row['bids_count'],
                'auction_duration': row['auction_duration'],
                'status': row['status'],
                'end_time': end_time.isoformat()  # Convert to ISO format for HTML
            })

    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of auctions per page
    total_pages = ceil(len(auctions) / per_page)

    start = (page - 1) * per_page
    end = start + per_page
    paginated_auctions = auctions[start:end]

    pagination = {
        'current_page': page,
        'pages': total_pages,
        'has_next': page < total_pages,
        'has_prev': page > 1,
        'next_page': page + 1 if page < total_pages else None,
        'prev_page': page - 1 if page > 1 else None
    }
    return render_template('auction_list.html', auctions=paginated_auctions, pagination=pagination, csrf_token=generate_csrf)

@auction_bp.route('/my-bids')
def my_bids():
    return render_template('my_bids.html')  # Replace with actual logic

@auction_bp.route('/my_auctions')
def my_auctions():
    if 'username' not in session:
        return redirect(url_for('auth.login'))  # Redirect to login if not logged in

    username = session['username']
    user_auctions = []

    with open(AUCTION_CSV, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['seller'] == username:  # Assuming 'seller' column exists
                user_auctions.append(row)

    return render_template('my_auctions.html', auctions=user_auctions)

@auction_bp.route('/toggle_watch', methods=['POST'])
def toggle_watch():
    if 'username' not in session:
        return jsonify({"error": "User not logged in"}), 401

    item_id = request.json.get("item_id")
    username = session['username']
    watchlist = []

    # Load existing watchlist
    try:
        with open(WATCHLIST_CSV, 'r') as file:
            reader = csv.reader(file)
            watchlist = list(reader)
    except FileNotFoundError:
        pass

    # Check if the user has already watched this item
    entry = [username, str(item_id)]
    if entry in watchlist:
        watchlist.remove(entry)
        action = "removed"
    else:
        watchlist.append(entry)
        action = "added"

    # Save updated watchlist
    with open(WATCHLIST_CSV, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(watchlist)

    return jsonify({"success": True, "action": action})

@auction_bp.route('/auction/<int:auction_id>')
def view_auction(auction_id):
    auctions = pd.read_csv('data/auction_data.csv')
    auction = auctions[auctions['item_id'] == auction_id].to_dict(orient='records')
    
    if auction:
        return render_template('auction_detail.html', auction=auction[0])
    else:
        return "Auction Not Found", 404

@auction_bp.route('/browse')
def browse():
    return render_template('auction_list.html')