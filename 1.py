from helper import read_file


def solve_p1():
    x = read_file(__file__).split('\n')
    l1, l2 = [], []
    for l in x:
        n1, n2 = map(int, l.split())
        l1.append(n1)
        l2.append(n2)

    l1.sort()
    l2.sort()

    ans = 0
    for n1, n2 in zip(l1, l2):
        ans += abs(n1 - n2)
    return ans


def solve_p2():
    x = read_file(__file__).split('\n')
    l1, l2 = {}, {}
    for l in x:
        n1, n2 = map(int, l.split())
        if n1 not in l1:
            l1[n1] = 0
        l1[n1] += 1
        if n2 not in l2:
            l2[n2] = 0
        l2[n2] += 1

    ans = 0
    for k, v in l1.items():
        if k not in l2:
            continue
        ans += l2[k] * v * k

    return ans


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
