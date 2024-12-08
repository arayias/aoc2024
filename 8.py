from typing import Dict, List, Set, Tuple
from helper import read_file
from collections import defaultdict

def get_antenna_positions(grid : List[str]) -> Dict[str, List[Tuple[int,int]]]:
    positions = defaultdict(list)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                positions[char].append((x, y))
    return positions

def visualize(grid : List[str], positions : Set[tuple]) -> None:
    height = len(grid)
    width = len(grid[0])

    for y in range(height):
        for x in range(width):
            if (x, y) in positions:
                print('X', end='')
            else:
                print(grid[y][x], end='')
        print()

def get_antinodes(p1 : Tuple[int,int], p2 : Tuple[int,int], width : int, height : int) -> Set[Tuple[int,int]]:
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    antinodes = set()

    antinodes.add((x1-dx, y1-dy))
    antinodes.add((x1+dx, y1+dy))
    antinodes.add((x2-dx, y2-dy))
    antinodes.add((x2+dx, y2+dy))

    antinodes.remove(p1)
    antinodes.remove(p2)

    return antinodes

def get_antinodes_two(p1 : Tuple[int,int], p2 : Tuple[int,int], width : int, height : int) -> Set[Tuple[int,int]]:
    def generate_antinodes(x : int, y : int, dx : int, dy : int, width : int, height : int) -> None:
        for direction in (1, -1):
            multiplier = direction
            while True:
                new_x = x + dx * multiplier
                new_y = y + dy * multiplier
                if 0 <= new_x < width and 0 <= new_y < height:
                    antinodes.add((new_x, new_y))
                    multiplier += direction
                else:
                    break

    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    antinodes = set()

    for x, y in (p1, p2):
        generate_antinodes(x, y, dx, dy, width, height)

    return antinodes

def solve_p1():
    grid = read_file(__file__).split('\n')
    height = len(grid)
    width = len(grid[0])

    positions = get_antenna_positions(grid)
    antinodes = set()

    for freq, antennas in positions.items():
        for i, p1 in enumerate(antennas):
            for j in range(i + 1, len(antennas)):
                p2 = antennas[j]

                new_nodes = get_antinodes(p1, p2, width, height)

                for node in new_nodes:
                    x, y = node
                    if 0 <= x < width and 0 <= y < height:
                        antinodes.add(node)

    for pos_list in positions.values():
        for pos in pos_list:
            if pos in antinodes:
                antinodes.add(pos)

    # visualize(grid, antinodes)
    return len(antinodes)

def solve_p2():
    grid = read_file(__file__).split('\n')
    height = len(grid)
    width = len(grid[0])

    positions = get_antenna_positions(grid)
    antinodes = set()

    for freq, antennas in positions.items():
        for i, p1 in enumerate(antennas):
            for j in range(i + 1, len(antennas)):
                p2 = antennas[j]

                new_nodes = get_antinodes_two(p1, p2, width, height)

                for node in new_nodes:
                    x, y = node
                    if 0 <= x < width and 0 <= y < height:
                        antinodes.add(node)

    for pos_list in positions.values():
        for pos in pos_list:
            if pos in antinodes:
                antinodes.add(pos)

    # visualize(grid, antinodes)
    return len(antinodes)

print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
