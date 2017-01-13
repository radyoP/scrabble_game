# not proud author: Pavel Janata
# Module of various functions, which should be
# useful in making scrabble bot
#


def space_in_direction(board, x, y):
    """
    returns list of how much space is in all direction in this order: up, down, left, right
    expected inputs are, game board, and x and y coordinates

    """
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    space_in_dir = []
    for dir in directions:
        word_len = 1
        next_x_y = [x+(dir[0]*word_len),y+(dir[1]*word_len)]
        while not next_to(board, dir, next_x_y[0], next_x_y[1]) and is_on_board(next_x_y[0], next_x_y[1]):
            word_len += 1
            next_x_y = [x+(dir[0]*word_len),y+(dir[1]*word_len)]
        space_in_dir.append(word_len-1)
    return space_in_dir


def next_to(board, orig_dir, x, y):
    """
    Checks in four directions, whether, there is letter. If it's, returns True
    """
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1), (0,0))
    orig_dir = tuple([-x for x in orig_dir])
    for dir in directions:
        if dir != orig_dir and is_on_board(x+dir[0], y+dir[1]) and board[x+dir[0]][y+dir[1]] != "*":
            return True
    return False

def print_board(board):
    first_line = "  "*2
    for i in range(15):
        first_line += str(i) + "  " if i < 10 else str(i) + " "
    print(first_line)
    for row_num, row in enumerate(board):
        line = ""
        for c in row:
            if c == "*":
                c = "·"
            line += c + "  "
        if row_num < 10:
            print("", row_num, "│", line[:-2])
        else:
            print(row_num, "│", line[:-2])



def is_on_board(x, y):
    return (0 <= x < 15) and (0 <= y < 15)

if __name__ == "__main__":
    """
    Examples of functions uses
    """

    board = [["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "R", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "O", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "O", "*", "L", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "F", "L", "A", "M", "E", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "K", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "E", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]
    print(board[9][6])
    in_dire = space_in_direction(board, 9, 6)
    print(in_dire)
    print("up:", in_dire[0], "down:", in_dire[1], "left:", in_dire[2], "right:", in_dire[3],)
