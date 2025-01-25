
from sklearn.ensemble import IsolationForest

def detect_fraud(bidding_data):
    model = IsolationForest()
    model.fit(bidding_data)
    predictions = model.predict(bidding_data)
    return bidding_data[predictions == -1]
