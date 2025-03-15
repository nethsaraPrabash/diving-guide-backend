import joblib
import numpy as np
import pandas as pd


best_rf = joblib.load("model/random_forest_model.pkl")
encoder = joblib.load("model/encoder.pkl")
scaler = joblib.load("model/scaler.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

def preprocess_input(data):
    new_data_df = pd.DataFrame([[data["discipline"], data["country"], data["event"], data["sex"], data["year"]]],
                               columns=["discipline", "country", "event", "sex", "year"])
    
    # Encode categorical variables
    new_data_encoded = encoder.transform(new_data_df[["discipline", "country", "event", "sex"]])
    
    # Scale numerical features
    new_data_scaled = scaler.transform(new_data_df[["year"]])
    
    # Combine encoded categorical and scaled numerical features
    new_data_final = np.hstack((new_data_encoded, new_data_scaled))
    
    return new_data_final

def make_prediction(processed_data):
    # Make a prediction
    new_prediction = best_rf.predict(processed_data)
    predicted_label = label_encoder.inverse_transform(new_prediction)[0]
    
    return predicted_label