import sys

#import controllers.players_controller as pc
#import controllers.tournament_controller as tc
from controllers import players_controller
from controllers import tournament_controller

import models.players as  mp
from controllers.create_menu import CreateMenu
from views.display_menu import *
from tinydb import TinyDB, Query, where 
from controllers.database_controller import *




class MainMenuController:
    def __init__(self):
        self.view = ShowMain()
        self.menu_create = CreateMenu()
        self.controller_choice = None
        self.selected_players = ShowPlayers()# To do
       
    def __call__(self):
    
        self.view.show_menu_detail()
        entry = self.menu_create(self.menu_create.main_menu)
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
        self.create_player = players_controller.PlayerController()
        self.players_report = players_controller.PlayerReport()
        self.main_menu_controller = MainMenuController()
        ##self.menu_load_player_controller = pc.LoadPlayer.show_in_menu() # To do

        
    def __call__(self): 
        entry = self.menu_create(self.menu_create.player_menu)
        while True:
            if entry == "1": 
                self.controller_choice = database_controller.DatabaseWorker.save_player_in_db(self.create_player.create_player(), self.db)
                self.controller_choice = self.main_menu_controller()
            elif entry == "2":
                self.controller_choice = self.players_report(self.db)
            elif entry == "3":
                self.controller_choice = self.main_menu_controller()
            else:
                break

class TournamentMenuController(MainMenuController):

    def __init__(self):
        super().__init__()
        self.db = TinyDB('data_base.json')
        self.tdb = TinyDB('tournament_db.json')
        self.serialized_tournament_table = self.tdb.table('Tournament')
        self.serialized_player_table = self.db.table('Player')
        self.dict_tournament = self.serialized_tournament_table.all()
        self.all_player = self.serialized_player_table.all()
        self.tournament_report_controller =  tournament_controller.TournamentReport()
        self.create_tournament = tournament_controller.TournamentController()
        self.run_tournament = tournament_controller.TournamentController()
        self.main_menu_controller = MainMenuController()
               
    def __call__(self):
        entry = self.menu_create(self.menu_create.tournament_menu)
        
        if entry == "1":
            self.controller_choice = self.create_tournament.create_tournament(self.db, self.tdb)
            self.controller_choice = self.main_menu_controller()
        if entry == "2":
            self.name__ = input('Enter the name of tournament you want to search: ')
            self.controller_choice = self.run_tournament.run_tournament(self.name__, self.tdb)  
            self.controller_choice = self.main_menu_controller()
        if  entry == "3":
            self.controller_choice =  self.tournament_report_controller()
        if entry == "4":
            self.controller_choice = self.main_menu_controller()
            
          

class AppControllerExit:

    def __call__(self):
        sys.exit()
    




