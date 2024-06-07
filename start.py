import pygame
import sys
from game_logic import GameLogic
from user_interface import UserInterface

custom_event = pygame.USEREVENT + 1

def start():
    ui = UserInterface()
    ui.show_menu()
    game = None
    in_menu = True

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and in_menu:
                        ui.start_game_screen()
                        game = GameLogic()
                        game.start_game(ui)
                        in_menu = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r and not in_menu:
                        if game:
                            pygame.event.post(pygame.event.Event(custom_event))
                    elif event.key == pygame.K_m:
                        ui.show_menu()
                        game = None
                        in_menu = True
                elif event.type == custom_event:
                    if game:
                        game.__init__()
                        ui.reset_game()
                        game.start_game(ui)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    start()
