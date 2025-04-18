from flask import Blueprint, jsonify
from team import Team

team_bp = Blueprint("team", __name__)

@team_bp.route("/api/teams", methods=["GET"])
def get_teams():
    week = "08"
    team_names = Team.teams_playing(week)
    teams = [Team(name=team_name) for team_name in team_names]
    return jsonify([team.__repr__() for team in teams])
