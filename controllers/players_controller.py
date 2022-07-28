from datetime import datetime, date
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
    # Working on
    @classmethod
    def update_player_ranking(cls, player, list_player, rank, score=True):
        if score:
            player.score += player.match_score
        player.rank = rank
        p = player.list_player(save_match_score=True)
        print(p['Last name'])




# To do
class PlayerReport:
   
    def __call__(self, db):
        self.menu_create = CreateMenu()
        self.main_menu_controller = menu_controller.MainMenuController()
        self.display_player = display_menu.DisplayPlayersReport()
        serialized_player_table = db.table('Player')
        self.players_db = serialized_player_table.all()
       
        self.display_player()
        entry = self.menu_create(self.menu_create.players_report_menu)
        while True:
            if entry == "1":
                player_by_name = [(w["Last name"], w['First name'], w['Date of birth'], w['Gender'], w['Rank'])  for w in  self.players_db]
                player_by_name.sort(key=lambda x : x[0])
                self.display_player.display_alphabetical(player_by_name)
                PlayerReport.__call__(self, db)
            elif entry == "2":
                player_by_name = [(w['Rank'], w["Last name"], w['First name'], w['Date of birth'], w['Gender'])  for w in  self.players_db]
                player_by_name.sort(key=lambda x : x[0])
                self.display_player.display_ranking(player_by_name)
                PlayerReport.__call__(self, db)
            elif entry == "3":
                self.main_menu_controller()
            else:
                return self.main_menu_controller()
            