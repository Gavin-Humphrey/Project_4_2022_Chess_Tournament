
from controllers.tournament_controller import *
from models.match import Match


class Round:
    
    def __init__(self, round_name_, list_match_):
        self.round_name = round_name_
        self.date_begin = ''
        self.date_end = ''
        self.list_match = list_match_


    def __str__(self):
        return self.round_name


    def create_matchs(self):
        matchs = []
        for i, pair in enumerate(self.players_pairs):
            matchs.append(Match(name=f"Match {i+1}", players_pair=pair))

        return matchs
        



    


"""class Round:
    def __init__(self, name, players_pairs, load_match: bool = False):

        self.name = name
        self.players_pairs = players_pairs

        # If we load a game, we assign an empty list to the matches in order to load them.
        # Else, we can create it normally
        if load_match:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

    def __str__(self):
        return self.name

    def create_matchs(self):
        matchs = []
        for i, pair in enumerate(self.players_pairs):
            matchs.append(Match(name=f"Match {i}", players_pair=pair))
        return matchs"""


