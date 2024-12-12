from helper import read_file
from typing import Dict, Tuple

memo : Dict[Tuple[int,int],int] = {}
def transform_stone(stone: int, remaining_blinks: int = 75) -> int:
    if (stone, remaining_blinks) in memo:
        return memo[(stone, remaining_blinks)]

    if remaining_blinks == 0:
        return 1

    if stone == 0:
        memo[(stone, remaining_blinks)] = transform_stone(1, remaining_blinks - 1)
        return memo[(stone, remaining_blinks)]

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid]) if stone_str[:mid] else 0
        right = int(stone_str[mid:]) if stone_str[mid:] else 0
        memo[(stone, remaining_blinks)] = transform_stone(left, remaining_blinks - 1) + transform_stone(right, remaining_blinks - 1)
        return memo[(stone, remaining_blinks)]

    memo[(stone, remaining_blinks)] = transform_stone(stone * 2024, remaining_blinks - 1)
    return memo[(stone, remaining_blinks)]

def solve_p1():
    stones = list(map(int, read_file(__file__).split('\n')[0].split()))
    return sum(transform_stone(stone,25) for stone in stones)

def solve_p2():
    stones = list(map(int, read_file(__file__).split('\n')[0].split()))
    return sum(transform_stone(stone,75) for stone in stones)


print(f"p1: {solve_p1()}")
print(f"p2: {solve_p2()}")
