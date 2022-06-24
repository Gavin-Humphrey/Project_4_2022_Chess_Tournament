class Player:

    def __init__(self, lastname, firstname, dob, sex, total_score, rank=0):

        self.lastname = lastname
        self.firstname = firstname
        self.dob = dob
        self.sex = sex
        self.match_score = 0
        self.total_score = total_score
        self.rank = rank



    def __str__(self):
            
        return f"{self.firstname} {self.lastname} [{self.match_score} pts]"

