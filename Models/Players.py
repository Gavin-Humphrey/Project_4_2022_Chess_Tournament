

class Player:

    def __init__(self, lastname, firstname, dob, sex, total_score, rank=0):

        self.lastname = lastname
        self.firstname = firstname
        self.dob = dob
        self.sex = sex
        self.match_score = 0
        self.total_score = 0
        self.rank = rank


    def __str__(self):
            
        return f"{self.firstname} {self.lastname}"

    def get_player(self):
        player= {
            'lastname': self.lastname,
            'firstname':self.firstname,
            'dob': self.dob,
            'sex': self.sex,
            'total_score': self.total_score,
            'rank': self.rank
    }
        return player

     