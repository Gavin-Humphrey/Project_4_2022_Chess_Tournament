from models.players import *
from .round import*

class Tournament:

    
    def __init__(self, name_, place_, date_, time_control_, nb_rounds_, round_, nb_player_, players_, desc_=''):  
        self.name = name_
        self.place = place_
        self.date = date_
        self.time_control = time_control_ # changed from time
        self.nb_rounds = nb_rounds_
        self.rounds = round_
        self.nb_player = nb_player_
        self.players = players_
        self.desc = desc_ # changed from state


    def __str__(self) -> str:
        return "Tournament: {}; Venue: {}; Date: {}; " .format(self.name, self.place, self.date,)

   








    