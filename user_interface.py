import pygame
import sys
from abc import ABC, abstractmethod
from constants import GameConstants

class IUserInterface(ABC):
    @abstractmethod
    def start_game_screen(self):
        pass

    @abstractmethod
    def display_board(self, board):
        pass

    @abstractmethod
    def get_player_move(self, player):
        pass

    @abstractmethod
    def show_winner(self, player):
        pass

    @abstractmethod
    def show_draw(self):
        pass

    @abstractmethod
    def invalid_move_message(self):
        pass

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def show_game_end(self):
        pass

    @abstractmethod
    def reset_game(self):
        pass

class UserInterface(IUserInterface):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT + 100))
        pygame.display.set_caption("Tic Tac Toe")
        self.font = pygame.font.Font(None, GameConstants.FONT_SIZE)
        self.title_font = pygame.font.Font(None, GameConstants.TITLE_FONT_SIZE)
        self.menu_options_font = pygame.font.Font(None, GameConstants.MENU_OPTIONS_FONT_SIZE)
        self.in_game = False

    def start_game_screen(self):
        self.screen.fill(GameConstants.BG_COLOR)
        pygame.display.update()
        self.in_game = True

    def display_board(self, board):
        self.screen.fill(GameConstants.BG_COLOR)
        cell_width = GameConstants.SCREEN_WIDTH // 3
        cell_height = (GameConstants.SCREEN_HEIGHT - 100) // 3

        for row in range(3):
            for col in range(3):
                pygame.draw.rect(self.screen, GameConstants.LINE_COLOR, (col * cell_width, row * cell_height, cell_width, cell_height), 3)
                if board[row * 3 + col] == GameConstants.PLAYER_X:
                    pygame.draw.line(self.screen, GameConstants.LINE_COLOR, (col * cell_width + 10, row * cell_height + 10),
                                     ((col + 1) * cell_width - 10, (row + 1) * cell_height - 10), 3)
                    pygame.draw.line(self.screen, GameConstants.LINE_COLOR, ((col + 1) * cell_width - 10, row * cell_height + 10),
                                     (col * cell_width + 10, (row + 1) * cell_height - 10), 3)
                elif board[row * 3 + col] == GameConstants.PLAYER_O:
                    pygame.draw.circle(self.screen, GameConstants.LINE_COLOR, (col * cell_width + cell_width // 2, row * cell_height + cell_height // 2), cell_width // 2 - 10, 3)

        self.display_footer()
        pygame.display.update()

    def display_footer(self):
        footer_y = GameConstants.SCREEN_HEIGHT - 80
        text_spacing = 50

        player1_text = self.menu_options_font.render("Player 1 - X", True, GameConstants.TEXT_COLOR)
        player2_text = self.menu_options_font.render("Player 2 - O", True, GameConstants.TEXT_COLOR)
        restart_text = self.menu_options_font.render("Restart (R)", True, GameConstants.TEXT_COLOR)
        menu_text = self.menu_options_font.render("Menu (M)", True, GameConstants.TEXT_COLOR)

        player1_rect = player1_text.get_rect(center=(GameConstants.SCREEN_WIDTH // 2, footer_y))
        player2_rect = player2_text.get_rect(center=(GameConstants.SCREEN_WIDTH // 2, footer_y + text_spacing))
        restart_rect = restart_text.get_rect(center=(GameConstants.SCREEN_WIDTH // 2, footer_y + text_spacing * 2))
        menu_rect = menu_text.get_rect(center=(GameConstants.SCREEN_WIDTH // 2, footer_y + text_spacing * 3))

        self.screen.blit(player1_text, player1_rect)
        self.screen.blit(player2_text, player2_rect)
        self.screen.blit(restart_text, restart_rect)
        self.screen.blit(menu_text, menu_rect)

    def get_player_move(self, player):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if y < GameConstants.SCREEN_HEIGHT - 100:
                        col = x // (GameConstants.SCREEN_WIDTH // 3)
                        row = y // ((GameConstants.SCREEN_HEIGHT - 100) // 3)
                        return row * 3 + col
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.show_menu()
                        return None
                    elif event.key == pygame.K_r:
                        return "RESTART"

    def show_winner(self, player):
        text = self.font.render(f"Winner: Player {player}", True, GameConstants.TEXT_COLOR)
        self.screen.blit(text, (50, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        self.show_game_end()

    def show_draw(self):
        text = self.font.render("Draw!", True, GameConstants.TEXT_COLOR)
        self.screen.blit(text, (250, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        self.show_game_end()

    def invalid_move_message(self):
        text = self.font.render("Invalid move!", True, GameConstants.TEXT_COLOR)
        self.screen.blit(text, (150, 250))
        pygame.display.update()
        pygame.time.wait(1000)

    def show_menu(self):
        self.screen.fill(GameConstants.BG_COLOR)
        title_text = self.title_font.render("Tic Tac Toe", True, GameConstants.LINE_COLOR)
        self.screen.blit(title_text, (GameConstants.SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

        start_text = self.menu_options_font.render("Press ENTER to Start", True, GameConstants.LINE_COLOR)
        self.screen.blit(start_text, (GameConstants.SCREEN_WIDTH // 2 - start_text.get_width() // 2, 300))

        quit_text = self.menu_options_font.render("Press ESC to Quit", True, GameConstants.LINE_COLOR)
        self.screen.blit(quit_text, (GameConstants.SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 400))

        pygame.display.update()
        self.in_game = False

    def show_game_end(self):
        self.screen.fill(GameConstants.BG_COLOR)
        end_text = self.title_font.render("Game Over", True, GameConstants.LINE_COLOR)
        self.screen.blit(end_text, (GameConstants.SCREEN_WIDTH // 2 - end_text.get_width() // 2, 100))

        restart_text = self.menu_options_font.render("Press R to Restart", True, GameConstants.LINE_COLOR)
        self.screen.blit(restart_text, (GameConstants.SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 300))

        menu_text = self.menu_options_font.render("Press M for Menu", True, GameConstants.LINE_COLOR)
        self.screen.blit(menu_text, (GameConstants.SCREEN_WIDTH // 2 - menu_text.get_width() // 2, 400))

        quit_text = self.menu_options_font.render("Press ESC to Quit", True, GameConstants.LINE_COLOR)
        self.screen.blit(quit_text, (GameConstants.SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 500))

        pygame.display.update()

    def reset_game(self):
        self.start_game_screen()
