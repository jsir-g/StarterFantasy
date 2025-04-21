import os
import requests
from team import Team
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SPORTRADAR_API_KEY = os.getenv('SPORTRADAR_API_KEY')

class User:
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        self.chosen = None
        self.teams = []

    # Fetch all NFL team names from Sportradar
    def get_team_names(self):
        url = f'https://api.sportradar.com/nfl/official/trial/v7/en/league/teams.json'
        params = {'api_key': SPORTRADAR_API_KEY}
        headers = {"Accept": "application/json"}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            team_list = []
            for team in data.get('teams', []):
                market = team.get('market')
                name = team.get('name')
                if name != 'TBD':
                    team_list.append(f"{market} {name}")

            return team_list

        except requests.exceptions.RequestException as err:
            print(f"Error fetching teams: {err}")
            return []

    # Initialize the user's available teams list
    def initialize_team_names(self):
        self.teams = self.get_team_names()

    # Remove team from list if win
    def check_win_loss(self, week):
        if not self.chosen:
            print("No team chosen yet.")
            return self.teams

        result = self.chosen.win_or_loss(week)
        if result is True and self.chosen.name in self.teams:
            self.teams.remove(self.chosen.name)
        
        return self.teams