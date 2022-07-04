
class Tournament:

    def __init__(self, name_, place_, date_, time_control_, players_):
        self.name = name_
        self.place = place_
        self.date = date_
        self.time_control = time_control_
        self.players = players_

    def __str__(self):
        return "Tournament: {}\nVenue: {}\nDate: {}\nTime: {}" .format(self.name, self.place, self.date, self.time_control)





