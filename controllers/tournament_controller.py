from datetime import datetime, date

from tinydb import TinyDB
from models import tournament
from models.players import Player
from controllers.database_controller import DatabaseWorker
import controllers.round_controller as RC
import controllers.match_controller as MC



class TournamentController:
    @classmethod
    def create_tournament(cls, db):
        input_name = input("Please enter name of the tournament: ")
        input_place = input("Please enter the venue: ")
        stop = False
        while not stop:
                    try:
                        start_date = datetime.strptime(input("Please enter tournament  date of satrt in (DD/MM/YYYY): "), "%d/%m/%Y").strftime("%d/%m/%Y")
                        stop = True
                    except:
                        print("Please enter tournament's start date in format (DD/MM/YYYY")

        #input_time = input("Please enter time for the tournament") # time_control au lieu
        input_nb_player = input("Please enter the number of players in the tournament: ") 
        list_players = cls.get_player_name(int(input_nb_player), db)
        #nb_rounds = input("Please enter the number of rounds for this tournament")

        def nb_rounds(cls):   
            nb_rounds = 4
            print("the number of rounds is 4 by default\n"
                    "Do you want to change this number ?")
            valid_number = False
            while not valid_number:
                print("Enter 'Y' to change, and 'N' to continuer")
                choice = input(": ")
                if choice == "Y":
                    nb_rounds = input("Enter number of rounds :")
                    if nb_rounds.isdigit():
                        valid_number = True
                    else:
                        print("Enter digits")
                if choice == "N":
                    valid_number = True
            return nb_rounds

        def add_time_control(cls):
            print("Please chose time-control: ")
            time_control = None
            entry = input("Enter 1 for Bullet; 2 for Blitz; or 3 for Rapid: ")
            if entry == "1":
                time_control = "Bullet"
            if entry == "2":
                time_control = "Blitz"
            if entry == "3":
                time_control = "Rapid"
            return time_control

        if list_players != []:
           
            list_players_ranking = cls.player_classment(list_players) 
            list_pair = cls.player_pair(list_players_ranking) 
            list_match = cls.create_matchs(list_pair)
            round1 = RC.RoundController.create_round(list_match)
            tournament_ = tournament.Tournament(input_name, input_place, start_date, add_time_control(cls),
                    input_nb_player, list_players, nb_rounds(cls), [round1])
            return tournament_
       
    @classmethod
    def create_matchs(cls, list_pair):
        list_match = []
        for name_p1, name_p2 in list_pair:
            list_match.append(MC.MatchController.create_match(name_p1, name_p2))
        return list_match
     
    @classmethod
    def get_player_name(cls, nb_player, db):
        list_player = []
        for i in range(nb_player):
            print(f"Player {i+1} ")
            first_name = input("Please enter player's first name: ")
            last_name = input("Please enter players last name: ")
            p, pfound = DatabaseWorker.get_player_by_name(last_name, first_name, db)
            if not pfound:
                print(f"Player {last_name} {first_name} does not exist in the database. Please register this player and try again")
                # To do: add menu choice. 1st choice: reenter new player name; 2nd choice: go to the main menu to create a new player
                return []
            else:
                
                list_player.append(p)
        return list_player

    @classmethod   
    def order(cls, ditc_player):
        return ditc_player ['Rank']

    @classmethod
    def player_classment(cls, list_player):
        if len(list_player) % 2 != 0:
            return "We are sorry we can't start a tournament, the number of players has to be pair"
        else:
            return [ e ['Last name'] +' '+ e ['First name'] for e in sorted(list_player, key = cls.order, reverse=True)]
        
    @classmethod
    def player_pair(cls, list_player_ranking):
        if isinstance(list_player_ranking, list):
            return list(zip(list_player_ranking[:int(len(list_player_ranking)/2)], list_player_ranking[int(len(list_player_ranking)/2):]))


        

