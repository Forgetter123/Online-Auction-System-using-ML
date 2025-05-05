import pickle
import numpy as np

def load_model():
    with open('models/final_price_model.pkl', 'rb') as f:
        return pickle.load(f)

def predict_final_price(features):
    model = load_model()
    return model.predict(np.array([features]))[0]