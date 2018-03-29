# https://www.reddit.com/r/dailyprogrammer/comments/7t6fnc/20180126_challenge_348_hard_square_sum_chains/

def squarer(num):
    def candidates(num, maxima):
        return [i for i in range(1, maxima + 1) if i != num and not (((num + i) ** 0.5) % 1)]

    def get_neighbors(seq, num):
        idx = seq.index(num)
        return seq[(idx - 1) % len(seq)], seq[(idx + 1) % len(seq)]

    def is_solved(seq):
        num = len(seq)
        counter = [n for n in seq if get_neighbors(seq, n)[0] in candidates(n, num) and get_neighbors(seq, n)[1] in candidates(n, num)]
        return len(counter) == num - 2

    def brute_force(nodes):
        from itertools import permutations

        for perm in permutations(nodes):
            if is_solved(perm):
                return perm
        return None

    def breadth_first(graph, nodes):
        def _bfs(graph, start):
            openset = [[start]]
            closedset = []
            closedset.append(openset[-1])
            while openset:
                current = openset.pop()
                if is_solved(current) and len(current) == num:
                    return current
                for j in graph[current[-1]]:
                    if j not in current:
                        child = current + [j]
                        if child not in closedset:
                            openset.insert(0, child)
                            closedset.append(child)
            return None

        for node in nodes:
            sol =  _bfs(graph, node)
            if sol:
                return sol
        return None

    def depth_first(graph, nodes, visited=None):
        stack = [[[n], {n}] for n in nodes]
        while stack:
            path, visited = stack.pop()
            if len(path) == num:
                return list(reversed(path))
            for u in graph[path[-1]]:
                if u not in visited:
                    stack.append([path + [u], visited | {u}])
        return None

    graph = {n: set(candidates(n, num)) for n in range(1, num + 1)}

    nodes = sorted(graph, key=lambda x: len(graph[x]))
    for u in nodes:
        graph[u] = sorted(graph[u], key=lambda x: len(graph[x]), reverse=True)

    return depth_first(graph, nodes)


def main():
    cases = [15, 8, 23, 24, 25, 64]
    for case in cases:
        print(case, squarer(case))


if __name__ == '__main__':
    main()
