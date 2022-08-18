class CreateMenu:
    """Creates the main menu, and sub-menus
    according to the number chosen"""

    main_menu = [("1", "Players Menu"), ("2", "Tournament Menu"), ("3", "Exit")]
    player_menu = [
        ("1", "Create Player"),
        ("2", "Update Player's Ranking"),
        ("3", "Load All Players Report"),
        ("4", "Back To Control Menu <<--"),
    ]
    tournament_menu = [
        ("1", "Create A New Tournament"),
        ("2", "Run A Tournament"),
        ("3", "Resume Tournament"),
        ("4", "Display Tournament"),
        ("5", "Load A Tournament Report"),
        ("6", "Delete A Tournament"),
        ("7", "Back To Control Menu <<--"),
    ]
    sub_tournaments_menu = [
        ("1", "Display Finished Matches"),
        ("2", "Display Matches In Progress"),
        ("3", "Display All Matches"),
    ]
    time_control_menu = [("1", "Bullet"), ("2", "Blitz"), ("3", "Rapid")]
    players_report_menu = [
        ("1", "Display Players Ranking By Score"),
        ("2", "Alphabetical Order"),
        ("3", "Ranking"),
        ("4", "Back To Control Menu <<--"),
    ]
    tournaments_report_menu = [
        ("1", "Display All Tournaments"),
        ("2", "Choose A Tournament To Display"),
        ("3", "Back To Control Menu <<--"),
    ]
    sub_tournaments_report_menu = [
        ("1", "Display All Players In This Tournament"),
        ("2", "Display All The Rounds In This Tournament"),
        ("3", "Display All The Matches In This Tournament"),
        ("4", "Return To Control Menu"),
    ]

    def __call__(self, menu_to_show):
        for line in menu_to_show:
            print(line[0] + " : " + line[1])
        while True:
            print("Enter Your Menu Choice Number")
            entry = input("-->> ")
            for line in menu_to_show:
                if entry == line[0]:
                    return str(line[0])
