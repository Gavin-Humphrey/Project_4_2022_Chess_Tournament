class CreatePlayer():

    def display_input(self):

        lastname = input("Player's last name:\n> ")
        firstname = input("Player's first name:\n> ")
        dob = input("Date of birth (DD/MM/YYYY):\n> ")
        sex = input("Player's sex:\n> ")
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

    
