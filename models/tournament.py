from models.players import *
from .round import*

class Tournament:

    
    def __init__(self, name_, place_, date_, time_control_, nb_player_, players_,  nb_rounds_, round_, desc_=''):
        self.name = name_
        self.place = place_
        self.date = date_
        self.time_control = time_control_ # changed from time
        self.nb_player = nb_player_
        self.players = players_
        self.nb_rounds = nb_rounds_
        self.rounds = round_
        self.desc = desc_ # changed from state


    def __str__(self) -> str:
        return "Tournament: {}; Venue: {}; Date: {}; " .format(self.name, self.place, self.date,)

   








    """ def create_round(self, round_number):
        pair_players = self.create_players_pairs(current_round=round_number)
        round = Round("Round " + str(round_number + 1), pair_players)
        self.rounds.append(round)


    def create_players_pairs(self, current_round):
        first_rank = Player()
        # first round the players are sorted by their ranks
        if current_round == 0:
            sorted_players = sorted(self.players, key = first_rank.rank, reverse=True)

        # Next round, by their score
        else:
            sorted_players = []
            score_sorted_players = sorted(self.players, key= first_rank.total_score, reverse=True)"""

   


