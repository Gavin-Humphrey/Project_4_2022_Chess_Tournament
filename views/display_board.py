from tinydb import TinyDB, Query, where
from controllers.players import *
from views.players import *


#print(create_player())
db = TinyDB('data_base.json')
player_table = db.table('Player')
#save_player_in_db(create_player(), player_table)
#get_all_players()
get_all_players(player_table.all())
list_player_order = player_classment(player_table.all())
print(list_player_order)

print('--------------------------------------------------------------')
for p1, p2 in make_match(list_player_order):
    print(p1 , " vs " , p2)