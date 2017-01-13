import scrabble_game
import sys


def load_players(module):
    module = module[:-3] if module[-3:] == ".py" else module
    try:
        imported_player = __import__(module)
        player = imported_player.ScrabblePlayer("dictionary.txt")
    except ImportError:
        print("No module '" + module + "' found.")
        exit()
    except NameError:
        print("Module '" + module + "' doesn't contain ScrabblePlayer class")
        exit()
    return player


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No arguments given, trying to import players from module scrabble_player")
        try:
            p0 = load_players("scrabble_player")
            p1 = load_players("scrabble_player")
        except NameError:
            print("No module scrabble_player found. Terminating")
            exit()

    elif len(sys.argv) == 2:
        print("One argument given, trying to import player form module " + sys.argv[1])
        p0 = load_players(sys.argv[1])
        print("Attempting to import second player form 'scrabble_player'")
        p1 = load_players("scrabble_player")

    else:
        player1_module = sys.argv[1]
        player2_module = sys.argv[2]
        print("Two arguments given, trying to import players form modules " + player1_module+" and "+player2_module)
        p0 = load_players(player1_module)
        p1 = load_players(player2_module)

    game = scrabble_game.Game(p0, p1)
    game.play()