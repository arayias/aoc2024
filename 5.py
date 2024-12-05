from collections import defaultdict, deque
from typing import Dict, Set, List, Tuple
from helper import read_file

def generate_dependency_graph(rules: List[str]) -> Tuple[Dict[int, Set[int]],Dict[int, Set[int]]]:
    dep : Dict[int,Set[int]] = defaultdict(set)
    graph :  Dict[int,Set[int]] = defaultdict(set)
    for rule in rules:
        before, after = map(int,rule.split("|"))
        dep[after].add(before)
        graph[before].add(after)
    return dep,graph


def solve_p1():
    rules, updates = map(lambda x: x.split("\n"),read_file(__file__).split("\n\n"))
    dep_dict,_ = generate_dependency_graph(rules)
    ans = 0
    for update in updates:
        seen : Set[int] = set()
        current_pages = list(map(int,update.split(",")))
        in_pages = set(current_pages)
        valid = True
        for page in current_pages:
            requirements = (dep_dict[page].intersection(in_pages)).issubset(seen)
            if not requirements:
                valid = False
                break
            seen.add(page)
        if not valid:
            # reorder
            continue
        ans += current_pages[len(current_pages)//2]

    return ans

def solve_p2():
    rules, updates = map(lambda x: x.split("\n"),read_file(__file__).split("\n\n"))
    dep_dict,graph = generate_dependency_graph(rules)
    ans = 0
    for update in updates:
        seen : Set[int] = set()
        current_pages = list(map(int,update.split(",")))
        in_pages = set(current_pages)
        valid = True
        for page in current_pages:
            requirements = (dep_dict[page].intersection(in_pages)).issubset(seen)
            if not requirements:
                valid = False
                break
            seen.add(page)
        if not valid:
            # current_pages.sort(key= lambda x : len(dep_dict[x].intersection(in_pages))) hacky but works doing it the right way
            in_deg = {page : 0 for page in current_pages}
            for page in current_pages:
                for req in dep_dict[page]:
                    if req in in_deg:
                        in_deg[page] += 1
            queue = deque([page for page in current_pages if in_deg[page] == 0])
            correct_order : List[int]  = []
            while queue:
                curr = queue.popleft()
                correct_order.append(curr)

                for n in graph[curr].intersection(in_pages):
                    in_deg[n] -= 1
                    if in_deg[n] == 0:
                        queue.append(n)


            ans += correct_order[len(correct_order) // 2]

    return ans


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
