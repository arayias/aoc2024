from helper import read_file
import re


def solve_p1():
    x = read_file(__file__).split('\n')
    ans = 0
    for line in x:
        f = re.findall(r"mul\(\d+,\d+\)", line)
        for match in f:
            n1, n2 = map(int, match[4:-1].split(","))
            ans += n1 * n2
    return ans


def solve_p2():
    x = read_file(__file__).split('\n')
    ans = 0
    skip = False
    for line in x:
        f = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for match in f:
            if match == "don't()":
                skip = True
            elif match == "do()":
                skip = False
            elif not skip:
                n1, n2 = map(int, match[4:-1].split(","))
                ans += n1 * n2
    return ans


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
