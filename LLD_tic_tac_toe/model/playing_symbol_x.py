from LLD_tic_tac_toe.model.playing_symbol import PlayingSymbol
from LLD_tic_tac_toe.model.symbol_types import SymbolTypes

class PlayingSymbolX(PlayingSymbol):

    def __init__(self) -> None:
        x_symbol = SymbolTypes.X.name
        super().__init__(x_symbol)
