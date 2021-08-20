"""
This is an example implementation of DFS algorithm (iterative).
"""

from stack import Stack
from helpers.graph_heplers import get_path, offsets
from helpers.maze_helpers import load_maze, can_move, print_maze


def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current = stack.pop()
        if current == goal:
            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left"]:
            next_row, next_col = offsets[direction]
            neighbout = (current[0] + next_row, current[1] + next_col)
            if can_move(maze, neighbout) and neighbout not in predecessors:
                stack.push(neighbout)
                predecessors[neighbout] = current

    return None


def main():
    maze = load_maze("data/mazes/maze1")
    print_maze(maze)

    start = (0, 0)
    goal = (2, 2)

    result = dfs(maze, start, goal)
    assert result == [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2)]
    print(result)


if __name__ == "__main__":
    main()
