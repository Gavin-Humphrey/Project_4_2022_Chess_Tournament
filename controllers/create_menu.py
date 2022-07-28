class CreateMenu:
   
    main_menu = [("1", "Players Menu"), ("2", "Tournament Menu"), ("3", "Exit")]

    player_menu = [("1", "Create Player"), ("2", "Load Players"), ("3", "Update Player's Ranking"), ("4", "Back To Control Menu <<--")]

    tournament_menu = [("1", "Create A New Tournament"), ("2", "Run A Tournament"), ("3", "Load A Tournament Report"), ("4", "Resume An Ongoing Tournament"), ("5", "Back To Control Menu <<--")]

    time_control_menu = [("1", "Bullet"), ("2", "Blitz"), ('3', "Rapid")]
    
    players_report_menu = [("1", "Alphabetical Order"), ("2", "Ranking"), ("3", "Back To Control Menu <<--")]

    tournaments_report_menu = [("1", "Display All Tournaments"), ("2", "Choose A Tournament To Display"),  ("3", "Back To Control Menu <<--")]
                               
    sub_tournaments_report_menu = [("1", "Display All Players In This Tournament"),  ("2", "Display All The Rounds In This Tournament"), 
        ("3", "Display All The Matches In This Tournament"), ("4", "Retourn To Control Menu")]
                                 
                                 
                                 
                                
                               
                           
                           
                          


    def __call__(self, menu_to_show):
        
        for line in menu_to_show:
            print(line[0] + " : " + line[1])
        while True:
            print("Enter Your Menu Choice Number")
            entry = input("-->> ")
            for line in menu_to_show:
                if entry == line[0]:
                 return str(line[0])


    
            