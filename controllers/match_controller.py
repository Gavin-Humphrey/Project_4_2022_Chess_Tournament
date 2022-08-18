from models.match import Match


class MatchController:
    @classmethod
    def create_match(cls, player1_name, player2_name):

        return Match(player1_name, player2_name)
