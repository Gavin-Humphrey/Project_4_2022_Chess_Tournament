from controllers.menu_controller import MainMenuController


def main():
    menu_display = MainMenuController()
        
    menu_display.__call__()


if __name__ == "__main__":
    main()
