from datetime import datetime, date
from models.round import Round


class RoundController:

    @classmethod
    def create_round(cls, list_match):
        
        input_round_name = input("Please enter round name: ")

        
                
        return Round(input_round_name, list_match)
    
