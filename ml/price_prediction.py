
import joblib
import numpy as np

model = joblib.load('price_prediction_model.pkl')

def predict_price(auction):
    input_data = np.array([
        [auction.item_condition, auction.starting_price, auction.bids_count, auction.seller_rating, auction.auction_duration]
    ])
    return model.predict(input_data)[0]
