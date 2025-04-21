from flask import Blueprint, jsonify
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("NEON_DB_URL")

team_bp = Blueprint("teams", __name__)

@team_bp.route("/api/teams", methods=["GET"])
def get_teams():
    try:
        with psycopg.connect(DB_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, full_name, abbreviation, conference, division, wins, losses
                    FROM teams
                    WHERE full_name NOT ILIKE '%TBD%'
                    ORDER BY full_name;
                """)
                rows = cur.fetchall()

                teams = [
                    {
                        "id": row[0],
                        "name": row[1],
                        "abbreviation": row[2],
                        "conference": row[3],
                        "division": row[4],
                        "wins": row[5],
                        "losses": row[6],
                    }
                    for row in rows
                ]

        return jsonify(teams)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
