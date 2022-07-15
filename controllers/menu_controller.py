import sys
from controllers.players_controller import *
from controllers.tournament_controller import TournamentController
import models.players as  mp
from controllers import create_menu
from views.display_menu import *
from tinydb import TinyDB, Query, where # just added
from controllers.database_controller import *
import controllers.players_controller as pc


class MainMenuController:
    def __init__(self):
        self.view = ShowMain()
        self.menu_to_create = create_menu.CreateMenu()
        self.controller_choice = None

    def __call__(self):
    
        self.view.show_menu_detail()
        entry = self.menu_to_create(self.menu_to_create.main_menu)

        if entry == "1":
            self.controller_choice = PlayerMenuController()
            self.player_menu_controller_choice()
        if entry == "2":
            self.controller_choice = TournamentMenuController()
            self.tournament_menu_controller_choice()
        if entry == "3":
            self.controller_choice = AppControllerExit()
            self.exit_app_controller_choice()

    def player_menu_controller_choice(self):
        return self.controller_choice()

    def tournament_menu_controller_choice(self):
        return self.controller_choice()

    def exit_app_controller_choice(self):
        return self.controller_choice()

class PlayerMenuController(MainMenuController):

    def __init__(self):
        super().__init__()
        self.db = TinyDB('data_base.json') 
        self.serialized_player_table = self.db.table('Player')
        self.create_player = pc.PlayerController()
        self.main_menu_controller = MainMenuController()
        
    def __call__(self):
        entry = self.menu_to_create(self.menu_to_create.player_menu)
        if entry == "1":
            self.players_controller = database_controller.DatabaseWorker.save_player_in_db(self.create_player.create_player(), self.db)
            self.controller_choice = self.main_menu_controller()
        if entry == "2":
            self.controller_choice = self.main_menu_controller()


class TournamentMenuController(MainMenuController):
     
    def __init__(self):
        super().__init__()
        self.db = TinyDB('data_base.json')
        self.tdb = TinyDB('tournament_db.json')
        self.serialized_tournament_table = self.db.table('Tournament')
        self.create_tournament = TournamentController()  
        self.main_menu_controller = MainMenuController()
         

    def __call__(self):
        entry = self.menu_to_create(self.menu_to_create.tournament_menu)
        if entry == "1":
            self.tournament_control = database_controller.DatabaseWorker.save_tournament_in_db(self.create_tournament.create_tournament(self.db), self.tdb)
            self.controller_choice = self.main_menu_controller()
        if entry == "2":
            self.controller_choice = self.main_menu_controller()


class AppControllerExit:

    def __call__(self):
        sys.exit()
    


