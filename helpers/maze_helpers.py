"""
A set of maze functions used throughout all other algorithms and data structures.
"""


def load_maze(filename):
    """
    This function is used to generate a 2d list based on a maze stored in a text file.
    """
    with open(filename, newline=None) as file:
        maze = [[c for c in line.rstrip("\n\r")] for line in file]

        return maze


def print_maze(maze):
    """
    This function prints maze
    """
    [print(row) for row in maze]


def is_maze_rectangular(maze):
    """
    This function checks whether the rows of a maze are all the same length
    """
    if len(maze) == 0:
        return True

    base_len = len(maze[0])

    for i in range(1, len(maze)):
        if len(maze[i]) != base_len:
            return False


def can_move(maze, pos):
    """
    This function checks whether a move to the give position can be made.
    """
    i, j = pos
    row_count = len(maze)
    col_count = len(maze[0])

    return 0 <= i < row_count and 0 <= j < col_count and maze[i][j] != "*"
