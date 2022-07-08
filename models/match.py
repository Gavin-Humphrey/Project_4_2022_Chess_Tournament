

class Match:
    def __init__(self, name_, name_player1_, name_player2_, round_name_="round 1", score_=0):

        self.name = name_
        self.player1 = name_player1_
        self.player2 = name_player2_
        self.round_name = round_name_
        self.score = score_
        

    def __str__(self):
        return f"match {self.name} : {self.player1.last_name} {self.player1.first_name} vs  {self.player2.last_name} {self.player2.first_name}  round:{self.round_name} score : {self.score}"
    
    def update_score(self, new_score):
        self.score = new_score
    