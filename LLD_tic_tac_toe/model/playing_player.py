class PlayingPlayer():
    player_name = None
    player_symbol = None

    def __init__(self, name, symbol_instance) -> None:
        self.player_name = name
        self.player_symbol_instance = symbol_instance
    
    def get_player_name(self):
        return self.player_name
    
    def set_player_name(self, name):
        self.player_name = name
    
    def get_player_symbol(self):
        return self.player_symbol
    
    def set_player_symbol(self, symbol_instance):
        self.player_symbol = symbol_instance
    