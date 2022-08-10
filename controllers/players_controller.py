from audioop import reverse
from datetime import datetime, date
from tinydb import TinyDB, Query
#from controllers.database_controller import save_player_in_db
from models.players import Player
from views.players import *
from controllers import menu_controller
from .database_controller import DatabaseWorker#
from .create_menu import CreateMenu   #To do
from views import display_menu 



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
    @classmethod
    def display_player_scores(cls, player_table):
        print(" ")
        print("   Players Ranking By Score")
        for i, player in enumerate( player_table, 1):
            print(f"\n-- Player no {i} --\n ")
            for k, v in player.items():
                if k in ["Last name", "First name", "Rank", "Score"]:
                    print(k+ " : "+ str(v))
    @classmethod
    def update_player_score_rank(cls, all_players, player_table):
        cls.display_player_scores(all_players)
        player = Query()
       
        valid = False
        while not valid:
            choice = input(f"please enter player identifiant between  1 and {len(all_players)} that you want to update Score | Rank: ")
            try:
                if int(choice) <= len(all_players) or int(choice) >= 1:
                    last_name = all_players[int(choice) - 1]['Last name']
                    valid = True
            except:
                pass
        print("1: update score \n2: update Rank\n3: update Rank\n")
        choice = input ("please enter your choice: ")

        #choice = input ("please enter 1 if you want to update score, 2 for Rank 3 for twice : ")
        if choice == "1":
            new_score = int(input('please enter the new Score : '))
            player_table.update({'Score': new_score}, player["Last name"] == last_name)
        elif choice == "2":
            new_rank = int(input('please enter the new Rank : '))
            player_table.update({'Rank': new_rank}, player["Last name"] == last_name)
        elif choice == "3":
            new_score = int(input('please enter the new Score : '))
            new_rank = int(input('please enter the new Rank : '))
            player_table.update({'Score': new_score}, player["Last name"] == last_name)
            player_table.update({'Rank': new_rank}, player["Last name"] == last_name)
            


        
        
        
        


        
    @classmethod
    def display_all_players(cls, db):
        
        #list_player_ = db.all()
        #list_player = sorted(list_player_, key= lambda x : x['Score'],reverse=True)
        #print(list_player)

        """player_table = db.table('Player')
        player = Query()
        cls.display_all_players(player_table, db)"""

        

            
    # Working on
    """@classmethod
    def update_player_ranking(cls, player, list_player, rank, score=True):
        if score:
            player.score += player.match_score
        player.rank = rank
        p = player.list_player(save_match_score=True)
        print(p['Last name'])"""

class PlayerReport:
   
    def __call__(self, db):
        self.menu_create = CreateMenu()
        self.main_menu_controller = menu_controller.MainMenuController()
        self.display_player = display_menu.DisplayPlayersReport()
        serialized_player_table = db.table('Player')
        self.players_db = serialized_player_table.all()
        self.players_score_classment = PlayerController()
        self.player = Query()
        self.display_player()
        entry = self.menu_create(self.menu_create.players_report_menu)
        while True:
            if entry == "1":
                self.player_score = self.players_score_classment.display_all_players(serialized_player_table)
                list_player_score = sorted(serialized_player_table, key= lambda x : x['Score'],reverse=True)
                self.display_player.display_player_scores(list_player_score)
                PlayerReport.__call__(self, db)
            elif entry == "2":
                print('eoooooo')
                player_by_name = [{"Last name":w["Last name"],'First name': w['First name'], 'Date of birth':w['Date of birth'], 'Gender': w['Gender'], 'Rank':w['Rank']}  for w in  self.players_db]
                player_by_name.sort(key=lambda x : x["Last name"])
                self.display_player.display_alphabetical(player_by_name)
                PlayerReport.__call__(self, db)
            elif entry == "3":
                player_by_rank = [{"Rank":w['Rank'], "Last name":w["Last name"],'First name': w['First name'], 'Date of birth':w['Date of birth'], 'Gender': w['Gender']}  for w in  self.players_db]
                player_by_rank.sort(key=lambda x : x["Rank"], reverse=True)
                self.display_player.display_ranking(player_by_rank)
                PlayerReport.__call__(self, db)
            elif entry == "4":
                self.main_menu_controller()
            else:
                return self.main_menu_controller()
            