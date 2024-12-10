from collections import deque
from helper import read_file
from typing import List, Set, Tuple

def get_neighbors(grid : List[List[int]], r : int , c : int) -> List[Tuple[int,int]] :
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])
    neighbors = []

    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < rows and 0 <= new_c < cols:
            neighbors.append((new_r, new_c))
    return neighbors

def get_trail_score(grid : List[List[int]], start_r : int, start_c : int) -> int:
    rows, cols = len(grid), len(grid[0])
    visited : Set[Tuple[int, int]] = set()
    reachable_nines : int = 0
    queue = deque([(start_r, start_c)])

    while queue:
        r, c = queue.popleft()
        current_height = grid[r][c]

        if current_height == 9:
            reachable_nines += 1
            continue

        for next_r, next_c in get_neighbors(grid, r, c):
            next_height = grid[next_r][next_c]
            if (next_r, next_c) not in visited and next_height == current_height + 1:
                visited.add((next_r, next_c))
                queue.append((next_r, next_c))

    return reachable_nines

def get_alt_trail_score(grid : List[List[int]], start_r : int, start_c : int) -> int:
    rows, cols = len(grid), len(grid[0])
    unique_paths : int = 0
    queue = deque([(start_r, start_c, tuple([(start_r, start_c)]))])

    while queue:
        r, c, path = queue.popleft()
        current_height = grid[r][c]

        if current_height == 9:
            unique_paths += 1
            continue

        for next_r, next_c in get_neighbors(grid, r, c):
            next_height = grid[next_r][next_c]
            if next_height == current_height + 1:
                new_path = path + ((next_r, next_c),)
                queue.append((next_r, next_c, new_path))

    return unique_paths

def solve_p1():
    x = read_file(__file__).split('\n')
    grid = [[int(_) for _ in i] for i in x]

    total_score = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                score = get_trail_score(grid, r, c)
                total_score += score

    return total_score


def solve_p2():
    x = read_file(__file__).split('\n')
    grid = [[int(_) for _ in i] for i in x]

    total_score = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                score = get_alt_trail_score(grid, r, c)
                total_score += score

    return total_score

print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
