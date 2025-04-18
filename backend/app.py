from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os
import json
from team import Team
from user import User
from league import League
from routes.team_routes import team_bp
app.register_blueprint(team_bp)

# Load env vars
load_dotenv()

'''
app = Flask(__name__)
CORS(app)

# Register Blueprints
from routes.highlightly import highlightly_bp
app.register_blueprint(highlightly_bp)

@app.route("/")
def home():
    return "Starter Fantasy Backend is running!"
'''

app = Flask(__name__)

# Load environment variables (ensure you've set SPORTRADAR_API_KEY)
SPORTRADAR_API_KEY = os.getenv('SPORTRADAR_API_KEY', 'M31MHThjj9azPcbv3OTqSs3mSTWTKSz8VMthJGrZ')

@app.route('/')
def index():
    return "Starter Fantasy API is running!"

if __name__ == '__main__':
    # It's good practice to not run in debug mode in production
    app.run(debug=True)
