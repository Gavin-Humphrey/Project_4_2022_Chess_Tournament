
class Player:
    def __init__(self,  last_name_, first_name_, dob_, gender_, rank_, score_):
        self.last_name = last_name_
        self.first_name = first_name_
        self.dob = dob_
        self.gender = gender_
        self.rank = rank_
        self.score = score_
        
        
    
    def update_score(self, new_score):
        self.score = new_score
    

    def __str__(self) -> str:
        return "Player's Name: {} {}".format(self.last_name, self.first_name)
        #return "Player's Name: {} {}; Date of birth: {}; Gender: {}; Rank: {}; Score: {}".format(self.last_name, self.first_name, self.dob, self.sex, self.rank, self.score)

    