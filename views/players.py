import json
from datetime import datetime
from certifi import where

def get_all_players(list_player):
    print(" ")
    print('=================== PLAYERS TABLE ========================')
    for i, player in enumerate( list_player):
        print(f"\n ------------------- Player no {i+1} -------------------------\n ")
        for k, v in player.items():
            print(k+ " : "+ str(v))
        print(f"\n --------------------------------------------------------- ")
    print('==========================================================')
    



