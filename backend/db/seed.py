import os
import requests
import psycopg
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()
SPORTRADAR_API_KEY = os.getenv("SPORTRADAR_API_KEY")
DB_URL = os.getenv("NEON_DB_URL")

# API endpoints
TEAMS_API_URL = "https://api.sportradar.com/nfl/official/trial/v7/en/league/teams.json"
GAMES_API_URL_TEMPLATE = "https://api.sportradar.com/nfl/official/trial/v7/en/games/2024/REG/{week}/schedule.json"
STANDINGS_API_URL = "https://api.sportradar.com/nfl/official/trial/v7/en/seasons/2024/REG/standings/season.json"

def get_api_data(url):
    params = {'api_key': SPORTRADAR_API_KEY}
    headers = {'Accept': 'application/json'}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"[ERROR] API request failed: {err}")
        return {}

# 🚀 Seed all NFL teams into the database
def seed_teams():
    data = get_api_data(TEAMS_API_URL)
    teams = data.get("teams", [])
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            for team in teams:
                name = team.get("name")
                market = team.get("market")
                full_name = f"{market} {name}"
                alias = team.get("alias")
                abbreviation = team.get("abbreviation")
                conference = team.get("conference", {}).get("name")
                division = team.get("division", {}).get("name")
                cur.execute("""
                    INSERT INTO teams (name, market, full_name, alias, abbreviation, conference, division)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (full_name) DO NOTHING;
                """, (name, market, full_name, alias, abbreviation, conference, division))
        conn.commit()
    print(f"[✅] Seeded {len(teams)} teams.")

# 🏈 Seed games for a given week (week = "01", "08", etc.)
def seed_games(week):
    url = GAMES_API_URL_TEMPLATE.format(week=week)
    data = get_api_data(url)
    games = data.get("week", {}).get("games", [])
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            for game in games:
                game_id = game.get("id")
                home = game.get("home", {}).get("name")
                away = game.get("away", {}).get("name")
                home_score = game.get("scoring", {}).get("home_points")
                away_score = game.get("scoring", {}).get("away_points")
                status = game.get("status", "scheduled")
                cur.execute("""
                    INSERT INTO games (id, week, home_team, away_team, home_score, away_score, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING;
                """, (game_id, week, home, away, home_score, away_score, status))
        conn.commit()
    print(f"[✅] Seeded {len(games)} games for week {week}.")

# 🏆 Update team win/loss records
def seed_standings():
    data = get_api_data(STANDINGS_API_URL)
    conferences = data.get("conferences", [])
    updated = 0
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            for conf in conferences:
                for div in conf.get("divisions", []):
                    for team in div.get("teams", []):
                        full_name = team.get("name")
                        wins = team.get("wins")
                        losses = team.get("losses")
                        cur.execute("""
                            UPDATE teams SET wins = %s, losses = %s WHERE full_name = %s;
                        """, (wins, losses, full_name))
                        updated += 1
        conn.commit()
    print(f"[✅] Updated standings for {updated} teams.")

# 📦 Seed everything together
def seed_all(week):
    seed_teams()
    seed_games(week)
    seed_standings()

# 🧪 CLI entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed NFL data into Neon DB")
    parser.add_argument("--teams", action="store_true", help="Seed team data")
    parser.add_argument("--games", action="store_true", help="Seed games for given week")
    parser.add_argument("--standings", action="store_true", help="Seed win/loss standings")
    parser.add_argument("--all", action="store_true", help="Seed everything")
    parser.add_argument("--week", type=str, default="08", help="Specify NFL week (e.g. 01, 08, 17)")

    args = parser.parse_args()

    if args.all:
        seed_all(args.week)
    else:
        if args.teams:
            seed_teams()
        if args.games:
            seed_games(args.week)
        if args.standings:
            seed_standings()
