class UniformCostSearch:
    def __init__(self, graph: dict, start, goals):
        self.graph = graph
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def ucs(self, verbose: bool = False):
        op = [(0, self.start)]
        closed = []
        parent = {self.start: None}
        cost_so_far = {self.start: 0}

        step = 0
        while op:
            op.sort(key=lambda item: item[0])
            current_cost, x = op.pop(0)

            if x in closed:
                continue

            step += 1
            closed.append(x)

            if x in self.goals:
                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, cost = {current_cost},\n"
                        f"open = {op},\n"
                        f"close = {closed}\n"
                    )
                return self._reconstruct(parent, x), closed, current_cost

            for child, cost in self.graph.get(x, []):
                new_cost = current_cost + cost

                if child in closed and new_cost >= cost_so_far.get(child, float('inf')):
                    continue

                if new_cost < cost_so_far.get(child, float('inf')):
                    cost_so_far[child] = new_cost
                    parent[child] = x
                    op.append((new_cost, child))

            if verbose:
                print(
                    f"Buoc {step}:\n"
                    f"X = {x}, cost = {current_cost},\n"
                    f"open = {op},\n"
                    f"close = {closed}\n"
                )

        return None, closed, float('inf')

    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def bai6():
    print("Bai 6: UCS tren do thi co trong so:")
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('C', 3), ('D', 2)],
        'B': [('D', 1), ('G', 5)],
        'C': [('G', 7)],
        'D': [('G', 2)],
        'G': []
    }

    search = UniformCostSearch(graph, start='S', goals='G')
    path, closed, total_cost = search.ucs(verbose=True)

    if path is not None:
        print(f"Duong di tim duoc: {' - '.join(path)}")
        print(f"Tong chi phi duong di: {total_cost}")
    else:
        print("Khong tim thay duong di.")

    print(f"Thu tu duyet: {closed}")
    print(f"Tong so nut duyet: {len(closed)}")


if __name__ == "__main__":
    bai6()
