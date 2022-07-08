

class Round:
    
    def __init__(self,Round_name_, date_begin_, date_end_, tournament_, list_match_):
        self.Round_name = Round_name_
        self.date_begin = date_begin_
        self.date_end = date_end_
        self.tournament = tournament_
        self.list_match = list_match_

        # ajouté
        if list_match_:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

        self.start_date = ""
        self.end_date = ""



    def __str__(self):
        return self.Round_name


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


