from models.players import *
from .round import*

class Tournament:

    
    def __init__(self, name_, place_, date_, time_, nb_player_, players_,  nb_rounds_, state_="Create"):
        self.name = name_
        self.place = place_
        self.date = date_
        self.time = time_
        self.nb_player = nb_player_
        self.players = players_
        self.nb_rounds = nb_rounds_
        self.rounds = []
        self.state = state_


    def __str__(self) -> str:
        return "Tournament: {}; Venue: {}; Date: {}; Time: {}" .format(self.name, self.place, self.date, self.time)


    def create_rounds(self, list_player, round_name="round 1"):
        pass

    def ordre(self, ditc_player):
        return ditc_player ['Rank']

    
    def player_classment(self):
        list_player = self.players.copy()
        if len(list_player) % 2 == 0:
            return "We are sorry we can't start a tournament, the number of players has to be pair"
        else:
            return [ e ['Last name'] +' '+ e ['First name'] for e in sorted(list_player,key = self.ordre, reverse=True)]
        

    def player_pair(self, list_player_ranking):
        if isinstance(list_player_ranking, list):
            return list(zip(list_player_ranking[:4], list_player_ranking[4:]))









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

   


