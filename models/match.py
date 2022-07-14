

class Match:
    def __init__(self, name_player1_, name_player2_, match_date_, score_=0):

        self.player1 = name_player1_
        self.player2 = name_player2_
        self.match_date = match_date_
        self.score = score_
        
    def __str__(self):
        return f"match  {self.player1.last_name} {self.player1.first_name} vs  {self.player2.last_name} {self.player2.first_name}  round:{self.round_name} score : {self.score}"
    
    def update_score(self, new_score):
        self.score = new_score
    