from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Load env vars
load_dotenv()

app = Flask(__name__)
CORS(app)

# Register Blueprints
from routes.highlightly import highlightly_bp
app.register_blueprint(highlightly_bp)

@app.route("/")
def home():
    return "Starter Fantasy Backend is running!"
