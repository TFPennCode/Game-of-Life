"""
This is an attempt at Conway's Game Of Life
By Toby Penner

If you don't know what the game is: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

I would like to learn to how to possibly optimize this to allow for faster execution time (more iterations per second) 
and also larger board sizes (optimizing memory usage). I think I might want to rewrite it in Go or C# for more speed on execution.

I will be taking an OOP approach to creating this game and there will be two main classes: Board and Cell
"""
from board import Board
import time

iterations_per_sec = 50  # in practice its actually slighly less because this is assuming instant execution of the rest of the code

# This is a famous pattern in the Life 1.06 format
GOSPER_GUN_LIFE = """
#Life 1.06
24 0
22 1
24 1
12 2
13 2
20 2
21 2
34 2
35 2
11 3
15 3
20 3
21 3
34 3
35 3
0 4
1 4
10 4
16 4
20 4
21 4
0 5
1 5
10 5
14 5
16 5
17 5
22 5
24 5
10 6
16 6
24 6
11 7
15 7
12 8
13 8
"""


def convert_life_to_list(life_str: str):
    # This function just converts patterns of cells in the Life 1.06 format into an array that the code can use
    lines = life_str.split("\n")  # Split the string into the individual coordinatess
    output = []
    for line in lines:  # iterate through each coordinates
        if line != "" and line[0] != "#":  # ignore blank lines and comments
            cords = line.split()  # get each of the coordinatess seperate
            output.append(
                (int(cords[1]), int(cords[0]))
            )  # form tuple of coordinatess and add it to the final output
    return output


board = Board(
    25, 50, convert_life_to_list(GOSPER_GUN_LIFE)
)  # initialize the board with the pattern defined above as the initial starting position
print(board)  # show board before any iterations have happened
while True:
    board.iterate_board()  # iterate the board once
    print(board)  # print the board after one iteration
    time.sleep(
        1 / iterations_per_sec
    )  # wait the required time for the correct amount of iterations per second to occur
