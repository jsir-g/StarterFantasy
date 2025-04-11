import os
import requests
from flask import Blueprint, jsonify

highlightly_bp = Blueprint("highlightly", __name__)

API_KEY = os.getenv("HIGHLIGHTLY_API_KEY")
BASE_URL = "https://api.highlightly.net/american-football/nfl"

@highlightly_bp.route("/api/teams", methods=["GET"])
def get_teams():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"{BASE_URL}/teams", headers=headers)
    return jsonify(response.json())
