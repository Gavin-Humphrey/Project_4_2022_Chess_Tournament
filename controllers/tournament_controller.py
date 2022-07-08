from datetime import datetime, date
import database 
from models import tournament, match, round
from models.players import Player


class TournamentController:
    database = ""
    @classmethod
    def create_tournament(cls):
        input_name = input("Please enter name of the tournament")
        input_place = input("Please enter the venue")
        while not stop:
                    try:
                        start_date = datetime.strptime(input("Please enter tournament {} date of satrt in (DD/MM/YYYY): ".format(i+1)), "%d/%m/%Y").strftime("%d/%m/%Y")
                        stop = True
                    except:
                        print("Please enter tournament's start date in format (DD/MM/YYYY")

        input_time = input("Please enter time for the tournament")
        input_nb_player = input("Please enter the number of players in the tournament")
        list_players = cls.get_player_name(input_nb_player, database)
        nb_rounds = input("Please enter the number of rounds for this tournament")
        if list_players != []:
            
            tournament = tournament.Tournament(input_name, input_place, start_date, input_time,
                    input_nb_player, list_players, nb_rounds, )

    @classmethod
    def create_matchs(list_pair):
        list_match = []

    @classmethod
    def get_player_name(cls, nb_player, db):
        list_player = []
        for i in range(nb_player):
            print(f"Player {i+1} ")
            first_name = input("Please enter player's first name")
            last_name = input("Please enter players last name")
            p = database.DatabaseWorker.get_player_by_name(first_name, last_name, db)
            if not p:
                print(f"Player {first_name} {last_name} does not exist in the database. Please register this player and try again")
                # To do: add menu choice. 1st choice: reenter new player name; 2nd choice: go to the main menu to create a new player
                return []
            else:
                
                list_player.append(p)

