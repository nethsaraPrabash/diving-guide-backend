from flask import Flask
from routes import suggest_diving_areas_endpoint, cdiving, classify_image

app = Flask(__name__)


app.add_url_rule('/suggest_diving_areas', 'suggest_diving_areas', suggest_diving_areas_endpoint, methods=['GET'])

app.add_url_rule('/cdiving', 'cdiving', cdiving, methods=['POST'])

app.add_url_rule('/classify_image', 'classify_image', classify_image, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)