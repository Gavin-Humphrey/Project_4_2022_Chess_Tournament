import json
from datetime import datetime
from models.tournament import *


def get_all_tournament(tournament_list):
    print(" ")
    print("==================== TOURNAMENT =======================")   
    for i, tournament in enumerate(tournament_list,1):
        print(f"\n ------------------- Tournament -----------------------\n")
        print('Tournament ID: ', i)
       
        for k, v in tournament.items():
            print(k+ " : "+ str(v))
        print(f"\n ------------------------------------------------------ ")
    print('==========================================================')
