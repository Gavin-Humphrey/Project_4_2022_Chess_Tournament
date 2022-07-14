import sys
from controllers.players_controller import PlayerController
from controllers.tournament_controller import TournamentController
import models.players as  mp
from .create_menu import CreateMenu
import views.display_menu as vdm
from tinydb import TinyDB, Query, where # just added


class MainMenuController:
    
    def __init__(self):
        self.view = vdm.ShowMain()
        self.create_menu = CreateMenu()
        self.controller_choice = None

    def __call__(self):
    
        self.view.show_menu_detail()
        entry = self.create_menu(self.create_menu.main_menu)

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
        self.create_player = PlayerController()
        self.main_menu_controller = MainMenuController()
        #self.player_model = mp.Player()
        self.player_model = PlayerController.create_player()

    def __call__(self):
        entry = self.create_menu(self.create_menu.player_menu)
        if entry == "1":
            self.controller_choice = self.create_player()
        if entry == "2":
            self.controller_choice = self.main_menu_controller()


class TournamentMenuController(MainMenuController):
     
    def __init__(self):
        super().__init__()
        tdb = TinyDB('data_base.json') 
        self.create_tournament = TournamentController()
        self.main_menu_controller = MainMenuController()
        self.tournament_control = TournamentController.create_tournament(tdb)


    def __call__(self):
        entry = self.create_menu(self.create_menu.tournament_menu)
        if entry == "1":
            self.controller_choice = self.create_tournament()
        if entry == "2":
            self.controller_choice = self.main_menu_controller()


class AppControllerExit:

    def __call__(self):
        sys.exit()