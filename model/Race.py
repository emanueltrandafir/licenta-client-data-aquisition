

class Race:
    def __init__(self, race_name, username, distance):
        self.name = race_name
        self.createdBy = username
        self.players = [username]
        self.distance = distance