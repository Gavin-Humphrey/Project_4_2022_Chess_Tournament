
from datetime import datetime, date
from models.players import Player
from models.tournament import Tournament
#from controllers.database_controller import save_tournament
from controllers.players_controller import * #create_player

def create_tournament():
    tournament_list = []
    stop_create_tournament = False
    while not stop_create_tournament:
        try:
          create_tournament_choice = input("Do you want to create a tournament? Enter Y for yes: ")
          stop_create_tournament = True
        except: 
            print("Please enter Y for yes and any other letter for no")
        else:     
            if create_tournament_choice == "Y":
                stop_date = False
                stop_time = False
                name = input("Please enter tournament name: ")
                place = input("please enter tournament venue: ")
                
                while not stop_date:
                    try:
                        date = datetime.strptime(input("Please enter tournament date in (DD/MM/YYYY): "), "%d/%m/%Y").strftime("%d/%m/%Y")
                        stop_date = True
                    except:
                        print("Please enter date of tournament in format (DD/MM/YYYY")

                while not stop_time:
                    try:
                        time = input("please enter tournament time in (HH:MM): ")
                        stop_time = True
                    except:
                        print("Please enter tournament time in (HH:MM) format")

                players = input("Please enter the number of players for this tournament: ")
                     
            t = Tournament(name, place, date, time, players)
            print(t)
            tournament_list.append(t)
              
            return tournament_list

    

               

   















