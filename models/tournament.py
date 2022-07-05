
class Tournament:

    def __init__(self, name_, place_, date_, time_, players_,  nb_rounds_=0):
        self.name = name_
        self.place = place_
        self.date = date_
        self.time = time_
        self.players = players_
        self.nb_rounds = nb_rounds_
        self.rounds = []

    def __str__(self) -> str:
        return "Tournament: {}; Venue: {}; Date: {}; Time: {}" .format(self.name, self.place, self.date, self.time)

    






