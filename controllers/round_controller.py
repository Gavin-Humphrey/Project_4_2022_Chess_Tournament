from datetime import datetime, date
from models.round import Round


class RoundController:

    @classmethod
    def create_round(cls, list_match):
        
        input_Round_name = input("Please enter round name: ")

        stop_date_begin = False
        while not stop_date_begin:
            try:
                input_date_begin = datetime.strptime(input("Please enter round start date in (DD/MM/YYYY): "), "%d/%m/%Y").strftime("%d/%m/%Y")
                stop_date_begin = True
            except:
                print("Please enter round start date in format (DD/MM/YYYY")
        
        stop_end_date = False
        while not stop_end_date:
            try:
                input_end_date = datetime.strptime(input("Please enter round end date in (DD/MM/YYYY): "), "%d/%m/%Y").strftime("%d/%m/%Y")
                stop_end_date = True
            except:
                print("Please enter round end date in format (DD/MM/YYYY")
                
        return Round(input_Round_name, input_date_begin, input_end_date, list_match)
    
