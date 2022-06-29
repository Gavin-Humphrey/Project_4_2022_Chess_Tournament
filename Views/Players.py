
class ViewPlayer:

    def create_player(self):

        lastname = input("Player's last name:\n> ")
        firstname = input("Player's first name:\n> ")
    
        dob = input("Date of birth:\n> ") 
        if dob.isdigit() and len(dob) == 10:
            print("Age entered")   
        else:
            print("Vous devez entrer un nombre à 10 chiffres") 
                  
        sex = input("'H' pour un homme \n'F' pour une femme: ")
        rank = input("Player's rank:\n> ")
     
        print(f"player {lastname} {firstname} created.")

        return {
            "last name": lastname,
            "first name": firstname,
            "dob": dob,
            "sex": sex,
            "rank": rank,
            "total score": 0,
        }

    def upload_players():
        
        def interface_menu(self, players_to_load):

            list_of_all_players = []

            for i in range(players_to_load):
                print(f"You have {str(players_to_load - i)} players to chose from.")
                    

    def update_player():
       pass
       
    
