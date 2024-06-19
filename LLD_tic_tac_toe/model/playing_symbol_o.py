from LLD_tic_tac_toe.model.playing_symbol import PlayingSymbol
from LLD_tic_tac_toe.model.symbol_types import SymbolTypes

class PlayingSymbolO(PlayingSymbol):

    def __init__(self) -> None:
        o_symbol = SymbolTypes.O.name
        super().__init__(o_symbol)
