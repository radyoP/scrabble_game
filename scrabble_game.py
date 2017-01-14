import collections
import random
import time
import trie
import scrabble_tools


class Game:
    def __init__(self, player0, player1, ignore_time = False):
        self.board = [
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]
        self.letters_bag = collections.Counter({"A": 9,
                                                "B": 2,
                                                "C": 2,
                                                "D": 4,
                                                "E": 10,
                                                "F": 2,
                                                "G": 3,
                                                "H": 2,
                                                "I": 9,
                                                "J": 1,
                                                "K": 1,
                                                "L": 4,
                                                "M": 2,
                                                "N": 6,
                                                "O": 8,
                                                "P": 2,
                                                "Q": 1,
                                                "R": 6,
                                                "S": 4,
                                                "T": 6,
                                                "U": 4,
                                                "V": 2,
                                                "W": 2,
                                                "X": 1,
                                                "Y": 2,
                                                "Z": 1})
        self.letters_values = {"A": 1,
                               "B": 3,
                               "C": 3,
                               "D": 2,
                               "E": 1,
                               "F": 4,
                               "G": 2,
                               "H": 4,
                               "I": 1,
                               "J": 8,
                               "K": 5,
                               "L": 1,
                               "M": 3,
                               "N": 1,
                               "O": 1,
                               "P": 3,
                               "Q": 10,
                               "R": 1,
                               "S": 1,
                               "T": 1,
                               "U": 1,
                               "V": 4,
                               "W": 4,
                               "X": 8,
                               "Y": 4,
                               "Z": 10}
        self.pos_values = [
    [-3, +1, +1, +2, +1, +1, +1, -3, +1, +1, +1, +2, +1, +1, -3],
    [+1, -2, +1, +1, +1, +3, +1, +1, +1, +3, +1, +1, +1, -2, +1],
    [+1, +1, -2, +1, +1, +1, +2, +1, +2, +1, +1, +1, -2, +1, +1],
    [+2, +1, +1, -2, +1, +1, +1, +2, +1, +1, +1, -2, +1, +1, +2],
    [+1, +1, +1, +1, -2, +1, +1, +1, +1, +1, -2, +1, +1, +1, +1],
    [+1, +3, +1, +1, +1, +3, +1, +1, +1, +3, +1, +1, +1, +3, +1],
    [+1, +1, +2, +1, +1, +1, +2, +1, +2, +1, +1, +1, +2, +1, +1],
    [-3, +1, +1, +2, +1, +1, +1, -2, +1, +1, +1, +2, +1, +1, -3],
    [+1, +1, +2, +1, +1, +1, +2, +1, +2, +1, +1, +1, +2, +1, +1],
    [+1, +3, +1, +1, +1, +3, +1, +1, +1, +3, +1, +1, +1, +3, +1],
    [+1, +1, +1, +1, -2, +1, +1, +1, +1, +1, -2, +1, +1, +1, +1],
    [+2, +1, +1, -2, +1, +1, +1, +2, +1, +1, +1, -2, +1, +1, +2],
    [+1, +1, -2, +1, +1, +1, +2, +1, +2, +1, +1, +1, -2, +1, +1],
    [+1, -2, +1, +1, +1, +3, +1, +1, +1, +3, +1, +1, +1, -2, +1],
    [-3, +1, +1, +2, +1, +1, +1, -3, +1, +1, +1, +2, +1, +1, -3]]
        self.player0 = Player(player0)
        self.player1 = Player(player1)
        self.player0.hand = self.give_letters(self.player0.hand)
        self.player1.hand = self.give_letters(self.player1.hand)
        self.move_num = 0
        self.last_moves_strings = 4*[False]
        self.ignore_time = ignore_time

        with open("dictionary.txt", "r") as file:
            words = [line[:-1] for line in file]
        self.valid_words = trie.Trie(words)

    def play(self):
        player = self.player0
        while not self.end_of_game():
            try:
                self.move(player)
            except (ValueError, TimeoutError):
                if player == self.player0:
                    print("Player0 loses. Game terminated")
                    return "p1"
                else:
                    print("Player1 loses. Game terminated")
                    return "p0"
            except IndexError:
                self.move_num += 1
                player = self.other_player(player)
                continue
            self.move_num += 1
            player = self.other_player(player)
        print("End of the game")
        if self.player0.score > self.player1.score:
            return "p0"
        elif self.player0.score < self.player1.score:
            return "p1"
        else:
            return "draw"

    def end_of_game(self):
        return set(self.letters_bag) == {} or (False not in self.last_moves_strings)

    def other_player(self, player):
        return self.player1 if player == self.player0 else self.player0

    def move(self, player):
        t1 = time.time()
        move = player.player.play(self.board, player.hand)
        t2 = time.time()
        if not self.ignore_time and t2 - t1 > 10:
            print("I'm not gonna wait that long!")
            raise TimeoutError
        if isinstance(move[0], str):
            print("\n\n    Player wants to change letters: "+move+"   Time:", round(t2 - t1, 3), "s")
            for ch in move:
                self.letters_bag[ch] += 1
                player.hand.remove(ch)
                self.last_moves_strings[self.move_num % 4] = True
        else:
            if self.board_is_valid(move):
                print("\n\n    Move is correct. Time:", round(t2-t1, 3), "s")
            else:
                print("    Move is incorrect")
                raise ValueError
            player.score += self.compare(self.board, move, player)
            self.board = move
            self.last_moves_strings[self.move_num % 4] = False
        player.hand = self.give_letters(player.hand)
        scrabble_tools.print_board(self.board)
        print("-------------Player 0:", self.player0.score, "---Player 1:", self.player1.score, "-------------")

    def compare(self, board, p_board, player):
        """Compares board from player with board, that was originally given to him and returns score"""
        mult = 1
        score = 0
        for x in range(15):
            for y in range(15):
                if board[x][y] != p_board[x][y]:
                    player.hand.remove(p_board[x][y])
                    if self.pos_values[x][y] < 0:
                        mult *= -1*(self.pos_values[x][y])
                        score += self.letters_values[p_board[x][y]]
                    else:
                        score += self.pos_values[x][y] * self.letters_values[p_board[x][y]]
        score *= mult
        return score

    def board_is_valid(self, board):
        """Checks whether every word on board is valid."""
        for word in self.find_words_on_board(board):
            if word not in self.valid_words:
                return False
        return True

    def find_words_on_board(self, board, rotated=False):
        """Finds all words on board"""
        for line in board:
            word = ""
            for ch in line:
                is_letter = False if ch == "*" else True
                if is_letter:
                    word += ch
                elif (not is_letter) and len(word) > 1:
                    yield word
                    word = ""
                elif (not is_letter) and len(word) == 1:
                    word = ""
        rotated_board = list(zip(*board[::-1]))
        rotated_board = [x[::-1] for x in rotated_board]
        if not rotated:
            return self.find_words_on_board(rotated_board, True)

    def give_letters(self, hand):
        """Accepts players hand as argument and randomly gives him l"""
        while len(hand) != 7:
            bag = list()
            for i in self.letters_bag.keys():
                bag += [i]*self.letters_bag[i]
            ran_ch = random.choice(bag)
            self.letters_bag[ran_ch] -= 1
            hand.append(ran_ch)
        return hand


class Player:
    """
    Class to wrap Player class. There sure is better way, but I was to lazy too do something better
    It remembers player's hand and score
    """
    def __init__(self, player):
        self.player = player
        self.hand = list()
        self.score = 0
