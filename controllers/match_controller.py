
from models.match import Match
from datetime import datetime, date

class MatchController:
    @classmethod
    def create_match(cls, player1_name, player2_name):

        stop_match_date = False
        while not stop_match_date:
            try:
                input_match_date = datetime.strptime(input("Please enter match date in (DD/MM/YYYY): "), "%d/%m/%Y").strftime("%d/%m/%Y")
                stop_match_date = True
            except:
                print("Please enter match date in format (DD/MM/YYYY")

        return Match(player1_name, player2_name, input_match_date)

        