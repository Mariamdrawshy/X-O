from constants import GameConstants

class GameLogic:
    def __init__(self):
        self.board = [GameConstants.EMPTY] * (GameConstants.BOARD_SIZE ** 2)
        self.current_player = GameConstants.PLAYER_X

    def start_game(self, ui):
        game_over = False
        while not game_over:
            ui.display_board(self.board)
            move = ui.get_player_move(self.current_player)
            if move == "RESTART":
                self.__init__()
                ui.reset_game()
                continue
            elif move is None:
                break
            if self.is_valid_move(move):
                self.board[move] = self.current_player
                if self.check_winner():
                    ui.display_board(self.board)
                    ui.show_winner(self.current_player)
                    game_over = True
                elif self.is_draw():
                    ui.display_board(self.board)
                    ui.show_draw()
                    game_over = True
                self.switch_player()
            else:
                ui.invalid_move_message()

    def is_valid_move(self, move):
        if move is None or move == "RESTART":
            return False
        return self.board[move] == GameConstants.EMPTY

    def switch_player(self):
        self.current_player = GameConstants.PLAYER_O if self.current_player == GameConstants.PLAYER_X else GameConstants.PLAYER_X

    def check_winner(self):
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != GameConstants.EMPTY:
                return True
        return False

    def is_draw(self):
        return GameConstants.EMPTY not in self.board
