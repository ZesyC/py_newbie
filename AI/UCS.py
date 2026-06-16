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
            if verbose:
                print(f"Bước {step}:")
                print(f"X = {x}, chi phí = {current_cost}")
                print(f"open = {self._format_open(op)}")
                print(f"close = {closed}\n")

            if x in self.goals:
                closed.append(x)
                return self._reconstruct(parent, x), closed, current_cost

            closed.append(x)

            for child, cost in self.graph.get(x, []):
                new_cost = current_cost + cost

                if child in closed and new_cost >= cost_so_far.get(child, float('inf')):
                    continue

                if new_cost < cost_so_far.get(child, float('inf')):
                    cost_so_far[child] = new_cost
                    parent[child] = x
                    op.append((new_cost, child))

        return None, closed, float('inf')

    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))

    def _format_open(self, op):
        return '[' + ', '.join(f"{node}(cost={cost})" for cost, node in op) + ']'


def bai6():
    print('Bài 6: UCS trên đồ thị có trọng số:')
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('C', 3), ('D', 2)],
        'B': [('D', 1), ('G', 5)],
        'C': [('G', 7)],
        'D': [('G', 2)],
        'G': []
    }

    find = UniformCostSearch(graph, start='S', goals='G')
    path, closed, total_cost = find.ucs(verbose=True)

    if path is not None:
        print(f"Đường đi tìm được: {' - '.join(path)}")
        print(f"Tổng chi phí đường đi: {total_cost}")
    else:
        print('Không tìm thấy đường đi.')
    print(f'Thứ tự duyệt: {closed}')
    print(f'Tổng số nút duyệt: {len(closed)}')


bai6()
