from datetime import datetime, date
#from controllers.database_controller import save_player_in_db
from models.players import Player
from views.players import *
from controllers import menu_controller
from .database_controller import DatabaseWorker#
from .create_menu import CreateMenu   #To do


class PlayerController:

    @classmethod
    def create_player(cls):
        list_player = []
        stop = False
        while not stop :
            try:

                nb_player = int(input("Please enter the number of players you want to create: "))
                stop = True
            except:
                print("Please enter a number ")
            else:
                for i in range(nb_player):
                    stop_rank = False
                    stop_score = False
                    stop_dob = False
                    last_name = input("Please enter player {} last name: ".format(i+1))
                    first_name = input("Please enter player {} first name: ".format(i+1))
                    while not stop_dob:
                        try:
                            dob = datetime.strptime(input("Please enter player {} date of birth in (DD/MM/YYYY): ".format(i+1)), "%d/%m/%Y").strftime("%d/%m/%Y")
                            stop_dob = True
                        except:
                            print("Please enter player's date of birth in format (DD/MM/YYYY")
                    gender = input("Please enter player {} gender: ".format(i+1))
                    while not stop_rank:
                        try:
                            rank = int(input("Please enter player {} rank: ".format(i+1)))
                            stop_rank = True
                        except:
                            print("Attributed rank should be a number")
                    while not stop_score:
                        try:
                            score = int(input("Please enter player {} score: ".format(i+1)))
                            stop_score = True
                        except:
                            print("Attributed score should be a number")

                    p = Player(last_name, first_name, dob, gender, rank, score)
                    print(p)
                    list_player.append(p)
                return list_player


# To do
"""class LoadPlayer:
    def show_in_menu(self, nb_players_to_load, db):
        all_players = db.table('Player')
        loaded_player = []
        for i in nb_players_to_load:
            return f"You have {str(nb_players_to_load - i)} players to load."
        print("Chose a player: \n")

        
        player_menu_display = []
        for i, player in enumerate(all_players):
            return f"{str(i+1)} - {player['Last name']} {player['First name']}\n"
        player_menu_display.append(str(i+1))"""



"""def ordre(ditc_player):
    return ditc_player ['Rank']

    
def player_classment(list_player):
    if len(list_player) != 8:
        return "We are sorry we can't start a tournament, the number of players has to be 8 and not {}".format(len(list_player))
    else:
        return [ e ['Last name'] + ' '+ e ['First name'] for e in sorted(list_player,key = ordre, reverse=True)]
    

def player_pair(list_player_ranking):
    if isinstance(list_player_ranking, list):
        return list(zip(list_player_ranking[:4], list_player_ranking[4:]))"""
