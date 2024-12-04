from typing import Set, Tuple, Deque, List
from helper import read_file
from collections import deque


def is_valid_pos(pos: Tuple[int, int], max_rows: int, max_cols: int) -> bool:
    row, col = pos
    return 0 <= row < max_rows and 0 <= col < max_cols


def solve_p1():
    x = read_file(__file__).split('\n')

    TO_FIND = "XMAS"
    MAX_ROWS = len(x) if x else -1
    MAX_COLS = len(x[0]) if x else -1

    LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)
    D1, D2, D3, D4 = (1, 1), (1, -1), (-1, 1), (-1, -1)
    valid_moves = [LEFT, RIGHT, UP, DOWN, D1, D2, D3, D4]

    found_count = 0
    q: Deque[Tuple[int, Tuple[int, int], Tuple[int, int]]] = deque()

    for row, line in enumerate(x):
        for col, char in enumerate(line):
            if char == TO_FIND[0]:
                for move in valid_moves:
                    q.append((1, (row, col), move))  # Start with index 1 (second char)

    while q:
        looking_idx, pos, change = q.popleft()
        if looking_idx == len(TO_FIND):
            found_count += 1
            continue

        current_row, current_col = pos
        new_pos = (current_row + change[0], current_col + change[1])

        if (
            is_valid_pos(new_pos, MAX_ROWS, MAX_COLS) and
            TO_FIND[looking_idx] == x[new_pos[0]][new_pos[1]]
        ):
            q.append((looking_idx + 1, new_pos, change))

    return found_count



def solve_p2():
    x = read_file(__file__).split('\n')
    ans = 0
    return ans


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
