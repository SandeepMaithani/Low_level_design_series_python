from LLD_tic_tac_toe.tic_tac_toe_game import TictacToeGame


if __name__ == "__main__":

    # start game
    game_session = TictacToeGame(board_size=3)
    game_result = game_session.start_game_session()

    if game_result == "Tie !!":
        print("No Winner for current game :(")

    print(f"Game winner is: {game_result}")
    