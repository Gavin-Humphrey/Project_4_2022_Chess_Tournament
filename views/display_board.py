from tinydb import TinyDB, Query, where

from controllers.players_controller import *
from views.players import *
from controllers.tournament_controller import *
from views.tournament import *

def main():

    #print(create_player())
    db = TinyDB('data_base.json')
    serialized_player_table = db.table('Player')
    #save_player_in_db(create_player(), serialized_player_table)
    #get_all_players()
    get_all_players(serialized_player_table.all())
    list_player_order = player_classment(serialized_player_table.all())
    print(list_player_order)
    print("")
    print('===================== Player By Pair =====================')
    print("")
    for p1, p2 in player_pair(list_player_order):
        print(p1 , " vs " , p2)

    tdb = TinyDB('tournament_db.json')
    serialized_tournament_table = tdb.table('Tournament')
    #save_tournament(create_tournament(), serialized_tournament_table)
    get_all_tournament(serialized_tournament_table.all())
    t1 = TournamentController.create_tournament(db)
    print(t1)
    #print(create_tournament)

