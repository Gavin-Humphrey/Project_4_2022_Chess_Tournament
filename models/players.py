
class Player:
    def __init__(self, id_player_, last_name_, first_name_, sex_, rank_, score_):
        self.id_player = id_player_
        self.last_name = last_name_
        self.first_name = first_name_
        #self.dob = dob_
        self.sex = sex_
        self.rank = rank_
        self.score = score_
    
    def update_score(self, new_score):
        self.score = new_score
    

    def __str__(self) -> str:
        return " je suis le joueur {} {} qui le score {} mon rank est {}".format(self.last_name, self.first_name, self.score, self.rank)
    