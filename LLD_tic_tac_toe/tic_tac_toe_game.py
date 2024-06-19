from collections import deque

from LLD_tic_tac_toe.model.playing_board import PlayingBoard
from LLD_tic_tac_toe.model.playing_player import PlayingPlayer
from LLD_tic_tac_toe.model.playing_symbol_o import PlayingSymbolO
from LLD_tic_tac_toe.model.playing_symbol_x import PlayingSymbolX

class TictacToeGame():

    player_turn_deque = None
    game_board_instance = None

    def __init__(self, board_size) -> None:
        self.board_size = board_size
        self.initialise_game_session()

    def initialise_game_session(self):
        self.player_turn_deque = deque()
        self.game_board_instance = PlayingBoard(size=self.board_size)

        cross_symbol_instance = PlayingSymbolX()
        circle_symbol_instance = PlayingSymbolO()

        player_1_instance = PlayingPlayer(name="Naruto", symbol_instance=cross_symbol_instance)
        player_2_instance = PlayingPlayer(name="Sasuke", symbol_instance=circle_symbol_instance)

        self.player_turn_deque.append(player_1_instance)
        self.player_turn_deque.append(player_2_instance)

    def start_game_session(self):
        is_game_completed = False

        while(not is_game_completed):
            
            player = self.player_turn_deque.popleft()

            self.game_board_instance.print_board_state()

            if not self.game_board_instance.can_player_make_move():
                print("No more Moves can be made !!")
                is_game_completed = True
                continue

            print(f"Player: {player.player_name} enter row, column ...")
            input_row, input_col = map(int, input().split(','))

            is_move_completed = self.game_board_instance.\
                add_player_symbol(
                    row=input_row, col=input_col,
                    playing_symbol_instance=player.player_symbol_instance
                )
            
            if not is_move_completed:
                print("Incorrect position selected, try again ...")
                self.player_turn_deque.appendleft(player)
                continue

            self.player_turn_deque.append(player)

            current_player_won = self.check_player_win(
                row=input_row, col=input_col,
                playing_symbol=player.player_symbol_instance.symbol)

            if current_player_won:
                self.game_board_instance.print_board_state()
                return player.player_name
            
        return "Tie !!"
    
    def check_player_win(self, row, col, playing_symbol):
        is_verticle_strike = is_horizontal_strike = is_left_diagonal_strike = is_right_diagonal_Strike = True
       # import pdb;pdb.set_trace()

        # check horizonal strike
        for current_col in range(self.board_size):
            if not self.game_board_instance.playing_board[row][current_col]:
                is_horizontal_strike = False
                break

            if self.game_board_instance.playing_board[row][current_col].symbol  != playing_symbol:
                is_horizontal_strike = False
                break
        
        # check vertical strike
        for current_row in range(self.board_size):
            if not self.game_board_instance.playing_board[current_row][col]:
                is_verticle_strike = False
                break

            if self.game_board_instance.playing_board[current_row][col].symbol != playing_symbol:
                is_verticle_strike = False
                break
        
        if row == col:
            for diagonal_index in range(self.board_size):
                if not self.game_board_instance.playing_board[diagonal_index][diagonal_index]:
                    is_left_diagonal_strike = False
                    break

                if self.game_board_instance.playing_board[diagonal_index][diagonal_index].symbol  != playing_symbol:
                    is_left_diagonal_strike = False
                    break
        else:
            is_left_diagonal_strike =  False

        for index in range(self.board_size):
            diagonal_row = self.board_size - index -1
            diagonal_col = index

            if not self.game_board_instance.playing_board[diagonal_row][diagonal_col]:
                is_right_diagonal_Strike = False
                break

            if self.game_board_instance.playing_board[diagonal_row][diagonal_col].symbol != playing_symbol:
                is_right_diagonal_Strike = False
                break

        if is_left_diagonal_strike or is_right_diagonal_Strike or is_horizontal_strike or is_verticle_strike:
            return True
        
        return False

            