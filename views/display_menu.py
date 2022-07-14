import models.players as mp
import models.tournament as mt
from controllers import database_controller
from tinydb import TinyDB, Query, where
from views.display_board import *
from controllers.database_controller import *


class ShowMain:
    
    def show_menu_detail(self):
        
        print("|---------|-------------------------------|--------|\n"
            "|         |     Tournament Management     |        |\n"
            "|---------|-------------------------------|--------|\n"
            "|---------|-------------------------------|--------|\n"
            "|         |          Main Menu            |        |\n"
            "|---------|-------------------------------|--------|\n"
            "|---------|-------------------------------|--------|\n"
            "|         | Enter a number of your choice |        |\n"
            "|---------|-------------------------------|--------|\n"
            )


class ShowTournament:
         
    def __call__(self):
        tdb = TinyDB('tournament_db.json')
        tournament_not_yet_started = False
        tournaments_db = mt.tdb

        for t in tournaments_db:
            if t.rounds == []:
                print({'Name':t.name, 'Venue':t.place})
                tournament_not_yet_started = True

        return tournament_not_yet_started


class ShowPlayers:
     
    def __call__(self):
        db = TinyDB('data_base.json')
        players_database = mp.db   
        for p in players_database:
            print({'Last name':p.last_name, 'First name':p.first_name, 'Rank':p.rank})
