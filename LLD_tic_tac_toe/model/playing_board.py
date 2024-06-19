class PlayingBoard():
    size = None
    playing_board = None

    def __init__(self, size) -> None:
        self.size = size
        self.playing_board = [[None]*self.size for _ in range(self.size)]
    
    def add_player_symbol(self, row, col, playing_symbol_instance):

        if row < 0 or col < 0 or row >= self.size or col >= self.size:
            return False

        if self.playing_board[row][col] != None:
            return False
        
        self.playing_board[row][col] = playing_symbol_instance

        return True
    
    def can_player_make_move(self):
        for row in self.playing_board:
            if None in row:
                return True
        
        return False
    
    def print_board_state(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.playing_board[row][col]:
                    print(f"{self.playing_board[row][col].symbol}    | ",  end =" ")
                else:
                    print(f"{self.playing_board[row][col]} | ",  end =" ")
            print("\n-----------------------")
