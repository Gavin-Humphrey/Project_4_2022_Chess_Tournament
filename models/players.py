
class Player:
    def __init__(self,  last_name_, first_name_, dob_, gender_, rank_, score_):
        self.last_name = last_name_
        self.first_name = first_name_
        self.dob = dob_
        self.gender = gender_
        self.rank = rank_
        self.score = score_
            
    
    def update_score(self, score_match):
        self.score += score_match
    
    def __str__(self) -> str:
        return "Player's Name: {} {}".format(self.last_name, self.first_name)
       

    