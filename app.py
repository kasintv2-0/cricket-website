# app.py
from flask import Flask, render_template, jsonify
import os
from datetime import datetime
import requests

app = Flask(__name__)

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

# Initialize the API with your key
cricket_api = CricketScoreAPI('763c4b17-bc64-4dfa-974d-627b4aa47c5f')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/live-scores')
def live_scores():
    matches = cricket_api.get_live_matches()
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)
