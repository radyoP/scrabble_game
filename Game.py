import scrabble_game
import argparse


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


def one_game(args):
    p0 = load_players(args.player0)
    p1 = load_players(args.player1)
    game = scrabble_game.Game(p0, p1, args.ignore_time)
    game_res = game.play()
    if game_res == "p0":
        print("Player0 wins!")
    elif game_res == "p1":
        print("Player1 wins!")
    return game_res


def tournament(args):
    res = {"p0": 0,"p1": 0, "draw": 0}
    for i in range(args.tournament):
        res[one_game(args)] += 1
        print("\n\n--------------------------Player0:", res["p0"], "Player1:", res["p1"], "--------------------------\n\n")
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p0", "--player0", type=str, default="scrabble_player.py", help="Name of module with player one")
    parser.add_argument("-p1","--player1", type=str, default="scrabble_player.py", help="Name of module with player two")
    parser.add_argument('-it', '--ignore_time', action="store_true", default=False,
                        help="Doesn't interrupt game, if players, plays for too long")
    parser.add_argument("-to","--tournament", type=int, default=0,
                        help="Runs multiple games")
    args = parser.parse_args()

    if args.player0 == args.player1:
        print("Trying to import players from "+args.player0)
    else:
        print("Trying to import players from "+args.player0+"and "+args.player1)

    if args.ignore_time:
        print("Ignoring time")
    if args.tournament == 0:
        one_game(args)
    else:
        print("Number of iterations:",args.tournament)
        res = tournament(args)
        print("\n\nPlayer0:", res["p0"], "Player1:", res["p1"], "\n\n")
