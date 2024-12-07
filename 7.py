from helper import read_file

def can_produce_target(nums, target, idx=0, current=0):

    if current > target:
        return False

    if idx == len(nums):
        return current == target

    if can_produce_target(nums, target, idx + 1, current + nums[idx]):
        return True

    if can_produce_target(nums, target, idx + 1, (current if current > 0 else 1) * nums[idx]):
        return True

    return False


def can_produce_target_with_concat(nums, target, idx=0, current=0):

    if current > target:
        return False

    if idx == len(nums):
        return current == target


    if can_produce_target_with_concat(nums, target, idx + 1, current + nums[idx]):
        return True

    if can_produce_target_with_concat(nums, target, idx + 1, (current if current > 0 else 1) * nums[idx]):
        return True

    if current > 0:
        concat_result = int(str(current) + str(nums[idx]))
        if concat_result <= target:
            if can_produce_target_with_concat(nums, target, idx + 1, concat_result):
                return True

    return False



def solve_p1():
    x = read_file(__file__).split('\n')
    a = 0
    for eq in x:
        ans, values = eq.split(": ")
        ans = int(ans)
        values = list(map(int, values.split()))

        if can_produce_target(values, ans):
            a += ans

    return a


def solve_p2():
    x = read_file(__file__).split('\n')
    a = 0
    for eq in x:
        ans, values = eq.split(": ")
        ans = int(ans)
        values = list(map(int, values.split()))

        if can_produce_target_with_concat(values, ans):
            a += ans

    return a


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
