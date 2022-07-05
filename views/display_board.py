from tinydb import TinyDB, Query, where
from controllers.database import save_tournament
from controllers.players import *
from views.players import *
from controllers.tournament import *
from views.tournament import *


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
for p1, p2 in make_match(list_player_order):
    print(p1 , " vs " , p2)

tdb = TinyDB('tournament_db.json')
serialized_tournament_table = tdb.table('Tournament')
#save_tournament(create_tournament(), serialized_tournament_table)
get_all_tournament(serialized_tournament_table.all())
create_tournament()
print(create_tournament())