class AStarSearch:
    def __init__(self, graph: dict, heuristic: dict, start, goals, alpha=1):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)
        self.alpha = alpha

    def a_star(self, verbose: bool = False):
        op = [self.start]
        closed = []
        parent = {self.start: None}
        g_score = {self.start: 0}
        best_goal = None
        best_cost = float('inf')

        step = 0
        while op:
            op.sort(key=lambda node: self._f_score(g_score[node], node))
            x = op.pop(0)
            step += 1
            closed.append(x)

            if x in self.goals:
                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, g(X) = {g_score[x]}, "
                        f"h(X) = {self.heuristic[x]}, "
                        f"f(X) = {self._f_score(g_score[x], x)},\n"
                        f"open = {op},\n"
                        f"close = {closed}\n"
                    )

                if g_score[x] < best_cost:
                    best_goal = x
                    best_cost = g_score[x]

                if not op or min(
                    self._f_score(g_score.get(node, float('inf')), node)
                    for node in op
                ) >= best_cost:
                    return self._reconstruct(parent, best_goal), closed, best_cost
                continue

            for child, cost in self.graph.get(x, []):
                new_cost = g_score[x] + cost
                old_cost = g_score.get(child, float('inf'))

                if child in closed and new_cost >= old_cost:
                    continue

                if child not in op or new_cost < old_cost:
                    parent[child] = x
                    g_score[child] = new_cost

                    if child not in op:
                        op.append(child)

            if verbose:
                print(
                    f"Buoc {step}:\n"
                    f"X = {x}, g(X) = {g_score[x]}, "
                    f"h(X) = {self.heuristic[x]}, "
                    f"f(X) = {self._f_score(g_score[x], x)},\n"
                    f"open = {op},\n"
                    f"close = {closed}\n"
                )

        if best_goal is not None:
            return self._reconstruct(parent, best_goal), closed, best_cost

        return None, closed, float('inf')

    def _f_score(self, cost_from_start, node):
        return cost_from_start + self.alpha * self.heuristic[node]

    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def bai2():
    graph = {
        'S': [('A', 1), ('B', 1)],
        'A': [('S', 1), ('B', 9)],
        'B': [('S', 1), ('A', 9), ('C', 6), ('G', 12)],
        'C': [('B', 6), ('G', 5)],
        'G': [('B', 12), ('C', 5)]
    }
    heuristic = {
        'S': 7,
        'A': 10,
        'B': 9,
        'C': 5,
        'G': 0
    }

    alpha = 2
    print(f"Bai 2: A* tu S den G voi alpha = {alpha}:")
    search = AStarSearch(
        graph, heuristic, start='S', goals={'G'}, alpha=alpha
    )
    path, closed, total_cost = search.a_star(verbose=True)

    if path is not None:
        print(f"Duong di tim duoc: {' - '.join(path)}")
        print(f"Tong chi phi duong di: {total_cost}")
    else:
        print("Khong tim thay duong di.")

    print(f"Thu tu duyet: {closed}")
    print(f"Tong so nut duyet: {len(closed)}")


if __name__ == "__main__":
    bai2()
