"""
This is an example implementation of A* algorithm.
"""

from data_structures.priority_queue import PriorityQueue
from helpers.graph_heplers import get_path, offsets
from helpers.maze_helpers import load_maze, can_move, print_maze, calc_distance


def heuristic(goal, neighbour):
    """
    Use a simple heuristic taking into account the Manhattan distance between 'a' and 'b'
    """
    return calc_distance(goal, neighbour)


def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)

    predecessors = {start: None}
    g_values = {start: 0}

    while not pq.is_empty():
        current = pq.get()
        if current == goal:
            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left"]:
            next_row, next_col = offsets[direction]
            neighbour = (current[0] + next_row, current[1] + next_col)
            if can_move(maze, neighbour) and neighbour not in g_values:
                # +1 because we are using unweighted graphs and so the distance (edge between nodes) is always 1
                new_cost = g_values[current] + 1
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current

    return None


def main():
    maze = load_maze("data/mazes/maze1")
    print_maze(maze)

    start = (0, 0)
    goal = (3, 3)

    result = a_star(maze, start, goal)
    assert result == [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]
    print(result)


if __name__ == "__main__":
    main()
