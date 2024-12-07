from typing import Dict, Set, List, Tuple
from collections import defaultdict, deque
from helper import read_file


directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
turns = {"^": ">", ">": "v", "v": "<", "<": "^"}

def solve_p1():
    grid = read_file(__file__).split("\n")
    grid = [list(row) for row in grid]

    guard_pos: Tuple[int, int] = (-1, -1)
    guard_dir = "^"

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                guard_pos = (i, j)
                guard_dir = cell
                grid[i][j] = "."
                break
        if guard_pos != (-1, -1):
            break

    states = set()
    states.add((guard_pos,guard_dir))
    visited = set()
    visited.add(guard_pos)

    while True:
        di, dj = directions[guard_dir]
        ni, nj = guard_pos[0] + di, guard_pos[1] + dj

        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
            break

        if grid[ni][nj] != "#":
            guard_pos = (ni, nj)
            if (guard_pos,guard_dir) in states:
                assert False
            states.add((guard_pos,guard_dir))
            visited.add(guard_pos)
        else:
            guard_dir = turns[guard_dir]

    return len(visited)

def find_loop_with_obstacle(grid : List[List[str]], obstacle_pos : Tuple[int,int],start_pos : Tuple[int,int], guard_dir : str) -> int:
    grid = [row[::] for row in grid]
    if grid[start_pos[0]][start_pos[1]] == "#":
        return 0

    grid[obstacle_pos[0]][obstacle_pos[1]] = "#"

    guard_pos = start_pos

    states = set()
    states.add((guard_pos,guard_dir))

    while True:
        di, dj = directions[guard_dir]
        ni, nj = guard_pos[0] + di, guard_pos[1] + dj

        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
            break

        if grid[ni][nj] != "#":
            guard_pos = (ni, nj)
        else:
            guard_dir = turns[guard_dir]

        if (guard_pos,guard_dir) in states:
            return 1

        states.add((guard_pos,guard_dir))
    return 0

def solve_p2():
    grid = read_file(__file__).split("\n")
    grid = [list(row) for row in grid]

    guard_pos: Tuple[int, int] = (-1, -1)
    guard_dir = "^"

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                guard_pos = (i, j)
                guard_dir = cell
                grid[i][j] = "."
                break
        if guard_pos != (-1, -1):
            break

    start_pos = guard_pos

    curr_pos = guard_pos
    curr_dir = guard_dir
    orig_path = set()
    while True:
        orig_path.add(curr_pos)
        di, dj = directions[curr_dir]
        ni, nj = curr_pos[0] + di, curr_pos[1] + dj

        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
            break

        if grid[ni][nj] != '#':
            curr_pos = (ni, nj)
        else:
            curr_dir = turns[curr_dir]

    ans : int = 0
    for possible_location in orig_path-{start_pos}:
        ans += find_loop_with_obstacle(grid,possible_location,start_pos,guard_dir)

    return ans

print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
