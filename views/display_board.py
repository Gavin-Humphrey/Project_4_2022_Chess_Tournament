from tinydb import TinyDB, Query, where

import controllers.players_controller as pc
from views.players import *
import controllers.tournament_controller as tc
from views.tournament import *

def main():

    #print(create_player())
    db = TinyDB('data_base.json')
    Player = Query()
    Table_player = db.table('Player')
    #print('trouver', Table_player.all())

    serialized_player_table = db.table('Player')
    #save_player_in_db(create_player(), serialized_player_table)
    #get_all_players()
    get_all_players(serialized_player_table.all())
    list_player_order = pc.player_classment(serialized_player_table.all())
    print(list_player_order)
    print("")
    print('===================== Player By Pair =====================')
    print("")
    for p1, p2 in pc.player_pair(list_player_order):
        print(p1 , " vs " , p2)

    tdb = TinyDB('tournament_db.json')
    serialized_tournament_table = tdb.table('Tournament')
    #save_tournament(create_tournament(), serialized_tournament_table)
    get_all_tournament(serialized_tournament_table.all())
    t1 = tc.TournamentController.create_tournament(db)
    serialized_tournament_table = tdb.table('Tournament')

    print('avant', t1.__dict__)
    dict_tournament = t1.__dict__
    list_round = [e.__dict__ for e in dict_tournament['rounds']]
    list_match = [e.__dict__  for e in list_round[0]['list_match']]
    list_round[0]['list_match'] = list_match

    dict_tournament['rounds'] = list_round
    
    serialized_tournament_table.insert(dict_tournament)

    
    #print(create_tournament)

