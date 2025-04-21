from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Import and register routes AFTER app is created
from routes.team_routes import team_bp
app.register_blueprint(team_bp)

@app.route("/")
def home():
    return "Starter Fantasy API is running!"

if __name__ == "__main__":
    app.run(debug=True)
