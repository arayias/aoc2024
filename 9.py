from helper import read_file



def parse_input(inp):
    file = True
    free = []
    used = []
    idx = 0
    used_n = 0
    for i,c in enumerate([_ for _ in inp]):
        c = int(c)
        if file:
            used.append((used_n,idx,idx+c))
            used_n += 1
        else:
            free.append((0,idx,idx+c))
        idx += c
        file = not(file)
    return used,free[::-1]

def solve_p1():
    x = read_file(__file__).split('\n')[0]
    used, free = parse_input(x)
    current_free = free.pop()
    current_used = used.pop()
    moved = []
    while used and current_free:
        if not current_free or not current_used:
            break
        _,free_start,free_end = current_free
        id,used_start,used_end = current_used
        used_size = used_end - used_start
        free_size = free_end - free_start

        if used_start > free_end:
            if used_size == free_size:
                current_free = free.pop()
                current_used = used.pop()
                moved.append((id,free_start,free_end))
            elif used_size < free_size:
                current_free = (_,free_start+used_size,free_end)
                moved.append((id,free_start,free_start+used_size))
                current_used = used.pop() if used else None
            else:
                current_used = (id,used_start+free_size,used_end)
                moved.append((id,free_start,free_end))
                current_free = free.pop() if free else None
        else:
            used.append(current_used)
            break

    check_sum = 0
    for idx,l,r in moved:
        for i in range(l,r):
            check_sum += i * idx

    for idx,l,r in used:
        for i in range(l,r):
            check_sum += i * idx

    return check_sum

def solve_p2():
    x = read_file(__file__).split('\n')[0]
    used, free = parse_input(x)
    moved = []

    while used:
        id, used_start, used_end = used.pop()
        used_size = used_end - used_start
        best_fit_index = None
        best_fit_start = float("inf")

        for idx, avail  in enumerate(free):
            if avail is None:
                continue
            avail_id, avail_start, avail_end = avail
            avail_size = avail_end - avail_start
            # must be to the left
            if avail_end > used_start:
                continue

            if avail_size >= used_size and avail_start < best_fit_start:
                best_fit_index = idx
                best_fit_start = avail_start

        if best_fit_index is not None:
            # print(f"moving {id} to {free[best_fit_index]}")
            avail_id, avail_start, avail_end = free[best_fit_index]
            if avail_end - avail_start == used_size:
                free[best_fit_index] = None
            else:
                free[best_fit_index] = (avail_id, avail_start + used_size, avail_end)
            moved.append((id, avail_start, avail_start + used_size))
        else:
            moved.append((id, used_start, used_end))

    check_sum = 0
    for idx, l, r in moved:
        for i in range(l, r):
            check_sum += i * idx

    return check_sum


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
