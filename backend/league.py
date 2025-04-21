from user import User
from team import Team
# from cpu import CPU

class League:
    def __init__(self, name, user_name, user_password, cpus=[], teams=[]):
        self.name = name
        self.user = User(user_name, user_password)
        self.cpus = cpus
        self.teams = teams

    def __repr__(self):
        return f"<League {self.name}>"