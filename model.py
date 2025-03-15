import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained K-means model and the dataset
kmeans = joblib.load('./model/ruindiv.pkl')
data = pd.read_csv('./data/shipwreck.csv')

# Standardize the depth feature
scaler = StandardScaler()
data['Depth (m)'] = scaler.fit_transform(data[['Depth (m)']])

# Predict the clusters
data['Cluster'] = kmeans.predict(data[['Depth (m)']])

def suggest_diving_areas(experience_level):
    if experience_level.lower() == 'beginner':
        cluster = 0
    elif experience_level.lower() == 'intermediate':
        cluster = 1
    elif experience_level.lower() == 'pro':
        cluster = 2
    else:
        return 'Error: Invalid experience level'
    
    suggested_areas = data[data['Cluster'] == cluster][['Site', 'Original Name', 'Depth (m)', 'Administrative District']]
    return suggested_areas.to_dict(orient='records')