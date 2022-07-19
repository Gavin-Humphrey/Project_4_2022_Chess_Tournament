class CreateMenu:
   
    main_menu = [("1", "Players Menu"), ("2", "Tournament Menu"), ("3", "Exit")]

    player_menu = [("1", "Create Player"), ("2", "Load Players"), ("3", "Update Player's Ranking"), ("4", "Back to Control Menu <<--")]

    tournament_menu = [("1", "Create a New Tournament"), ("2", "Run a Tournament#"), ("3", "Back to Tournament Menu <<--")]

    time_control_menu = [("1", "Bullet"), ("2", "Blitz"), ('3', "Rapid")]


    def __call__(self, menu_to_show):
        
        for line in menu_to_show:
            print(line[0] + " : " + line[1])
        while True:
            print("Enter Your Menu Choice Number")
            entry = input("-->> ")
            for line in menu_to_show:
                if entry == line[0]:
                 return str(line[0])


    
            