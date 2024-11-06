from flask import Flask, render_template, jsonify
import os
from datetime import datetime
import requests

app = Flask(__name__)

# Add configuration for production
app.config['SECRET_KEY'] = '763c4b17-bc64-4dfa-974d-627b4aa47c5f'
app.config['DEBUG'] = False

class CricketScoreAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.cricapi.com/v1"
        
    def get_live_matches(self):
        endpoint = f"{self.base_url}/matches"
        params = {
            "apikey": self.api_key,
            "offset": 0
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            live_matches = [
                match for match in data.get("data", [])
                if match.get("status") == "Live"
            ]
            return live_matches
        except requests.exceptions.RequestException as e:
            print(f"Error fetching live matches: {e}")
            return None

# Use environment variable for API key
API_KEY = os.getenv('763c4b17-bc64-4dfa-974d-627b4aa47c5f', '763c4b17-bc64-4dfa-974d-627b4aa47c5f')
cricket_api = CricketScoreAPI(API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/live-scores')
def live_scores():
    matches = cricket_api.get_live_matches()
    return jsonify(matches)

# Add error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Only use this for local development
    app.run(debug=False)
else:
    # This is used by the production WSGI server
    application = app
