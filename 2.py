from helper import read_file


def is_safe_sequence(seq):
    increasing = seq[0] < seq[1]
    is_safe = True
    issue_idx = -1

    for i in range(1, len(seq)):
        diff = abs(seq[i] - seq[i-1])

        if increasing:
            if seq[i-1] >= seq[i] or diff < 1 or diff > 3:
                is_safe = False
                issue_idx = i
                break
        else:
            if seq[i-1] <= seq[i] or diff < 1 or diff > 3:
                is_safe = False
                issue_idx = i
                break

    return [is_safe, issue_idx]


def solve_p1():
    x = read_file(__file__).split('\n')
    safe_count = 0

    for level in x:
        level = list(map(int, level.split()))
        is_safe, issue_idx = is_safe_sequence(level)
        if is_safe:
            safe_count += 1

    return safe_count


def solve_p2():
    x = read_file(__file__).split('\n')
    safe_count = 0

    for level in x:
        level = list(map(int, level.split()))
        is_safe, issue_idx = is_safe_sequence(level)

        if issue_idx != -1:
            for i in range(len(level)):
                if is_safe_sequence(level[:i] + level[i+1:])[0]:
                    is_safe = True
                    break

        if is_safe:
            safe_count += 1

    return safe_count


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
