from flask import Flask
from routes import suggest_diving_areas_endpoint

app = Flask(__name__)

# Register the routes
app.add_url_rule('/suggest_diving_areas', 'suggest_diving_areas', suggest_diving_areas_endpoint, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)