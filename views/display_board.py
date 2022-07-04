from tinydb import TinyDB, Query, where
from controllers.database import load_tournament
from controllers.players import *
from views.players import *
from controllers.tournament import *


#print(create_player())
db = TinyDB('data_base.json')
serialized_player_table = db.table('Player')
#save_player_in_db(create_player(), serialized_player_table)
#get_all_players()
get_all_players(serialized_player_table.all())
list_player_order = player_classment(serialized_player_table.all())
print(list_player_order)
print("")
print('===========================================================')
print("")
for p1, p2 in make_match(list_player_order):
    print(p1 , " vs " , p2)

serialized_tournament_table = db.table('Tournament')
load_tournament(create_tournament(), serialized_tournament_table)
create_tournament()
print(create_tournament())