
from datetime import datetime, date
from models.tournament import Tournament
from controllers.database import load_tournament

def create_tournament():

    tournament_list = []
    
    stop_create_tournament = False
    while not stop_create_tournament:
        try:
          create_tournament_choice = input("Do you want to create a tournament? Enter Y for Yes: ")
        except: 
            print("Please enter Y for yes and any other letter for no")
        else:     
            if create_tournament_choice == "Y":
                stop_date = False
                stop_time_control = False
                name = input("Please enter tournament name: ")
                place = input("please enter tournament venue: ")
                
                while not stop_date:
                    try:
                        date = datetime.strptime(input("Please enter tournament date in (DD/MM/YYYY): ".format()), "%d/%m/%Y").strftime("%d/%m/%Y")
                        stop_date = True
                    except:
                        print("Please enter date of tournament in format (DD/MM/YYYY")

                while not stop_time_control:
                    try:
                        time_control = datetime.strptime(input("please enter tournament time in (HH:MM): "), "%H:%M")
                        stop_time_control = True
                    except:
                        print("Please enter tournament time in (HH:MM) format")

                players = input("Please enter the number of players: ")

                t = Tournament(name, place, date, time_control, players)
                print(t)
                tournament_list.append(t)

            return tournament_list















