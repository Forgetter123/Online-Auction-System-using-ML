from flask import Blueprint, render_template, request, redirect, url_for, session
import csv
import os
import time

auction_bp = Blueprint('auction', __name__)
AUCTION_CSV = 'datasets/auction_data.csv'
BIDS_CSV = 'datasets/bids.csv'
UPLOAD_FOLDER = 'static/uploads/'
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
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        for row in reader:
            if row:
                auctions.append({
                    'item_id': row[0],
                    'item_name': row[1],
                    'category': row[2],
                    'item_condition': row[3],
                    'starting_price': row[4],
                    'final_price': row[5],
                    'bids_count': row[6]
                })
    return render_template('auction_list.html', auctions=auctions)