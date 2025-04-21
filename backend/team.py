import os
from team_controller import get_current_week, get_season_data

class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0

    def __repr__(self):
        return f"Team(name={self.name})"

    # Returns the teams playing for a certain week
    @staticmethod
    def teams_playing(week, team_names=None):
        data = get_current_week(week)

        if team_names is None:
            team_names = []

        games = data.get('week', {}).get('games', [])

        for game in games:
            home_team = game.get('home', {}).get('name')
            away_team = game.get('away', {}).get('name')

            if home_team and home_team not in team_names:
                team_names.append(home_team)
            if away_team and away_team not in team_names:
                team_names.append(away_team)

        return team_names

    # Returns whether this team won or lost in a certain week
    def win_or_loss(self, week):
        data = get_current_week(week)
        games = data.get('week', {}).get('games', [])

        for game in games:
            home_team = game.get('home', {}).get('name')
            away_team = game.get('away', {}).get('name')
            home_points = game.get('scoring', {}).get('home_points')
            away_points = game.get('scoring', {}).get('away_points')

            if self.name == home_team and home_points is not None and away_points is not None:
                return home_points > away_points
            elif self.name == away_team and home_points is not None and away_points is not None:
                return away_points > home_points

        return 'no game found'

    # Returns the team's record from season data
    def team_record(self, week=None):
        data = get_season_data()
        conferences = data.get('conferences', [])

        for conference in conferences:
            divisions = conference.get('divisions', [])
            for division in divisions:
                teams = division.get('teams', [])
                for team in teams:
                    if team.get('name') == self.name:
                        return team.get('wins'), team.get('losses')

        return 'record not found'
