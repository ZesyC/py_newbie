class AStarSearch:
    def __init__(self, graph: dict, heuristic: dict, start, goals, alpha: float = 1.0):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)
        self.alpha = alpha

    def a_star(self, verbose: bool = False):
        op = [self.start]
        close = []
        parent = {self.start: None}
        g_score = {self.start: 0}
        best_goal = None
        best_goal_cost = float('inf')

        step = 0
        while op:
            op.sort(key=lambda node: self.f_score(g_score[node], node))
            x = op.pop(0)
            step += 1

            if verbose:
                print(f"Bước {step}:")
                print(
                    f"  Chọn X: {x}"
                    f"(g={g_score[x]}, h={self.heuristic[x]}, "
                    f"f={self.f_score(g_score[x], x)})"
                )
                print(f"  open sau khi lấy X: {self.format_nodes(op, g_score)}")
                print(f"  close hiện tại: {close}")

            if x in self.goals:
                close.append(x)
                if g_score[x] < best_goal_cost:
                    best_goal = x
                    best_goal_cost = g_score[x]
                if verbose:
                    print(f"  Gặp đích tạm thời: {x}, chi phí = {g_score[x]}")

                if not op or min(g_score[node] for node in op) >= best_goal_cost:
                    if verbose:
                        print("  Không còn nhánh nào có g nhỏ hơn đích tốt nhất.\n")
                    return self.reconstruct(parent, best_goal), close, best_goal_cost
                continue

            close.append(x)
            children = []
            for child, cost in self.graph.get(x, []):
                new_cost = g_score[x] + cost

                if child in close and new_cost >= g_score.get(child, float('inf')):
                    continue

                if child not in op or new_cost < g_score.get(child, float('inf')):
                    parent[child] = x
                    g_score[child] = new_cost
                    children.append(child)

                    if child not in op:
                        op.append(child)

            op.sort(key=lambda node: self.f_score(g_score[node], node))
            if verbose:
                print(f"  Node con mới thêm/cập nhật: {self.format_nodes(children, g_score)}")
                print(f"  open sau khi sắp xếp: {self.format_nodes(op, g_score)}\n")

        if best_goal is not None:
            return self.reconstruct(parent, best_goal), close, best_goal_cost

        return None, close, float('inf')

    def reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))

    def format_nodes(self, nodes, g_score):
        return '[' + ', '.join(
            f"{node}(g={g_score[node]}, h={self.heuristic[node]}, "
            f"f={self.f_score(g_score[node], node)})"
            for node in nodes
        ) + ']'

    def f_score(self, cost_from_start, node):
        return cost_from_start + self.alpha * self.heuristic[node]


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
    print(f"Từ S đến G bằng A* với alpha = {alpha}:")
    find = AStarSearch(graph, heuristic, start='S', goals='G', alpha=alpha)
    path, close, total_cost = find.a_star(verbose=True)
    print(f"Thứ tự các nút được xét: {' -> '.join(close)}")
    if path is None:
        print("Không tìm thấy đường đi từ S đến G.")
        return

    print(f"Đường đi tìm được: {' -> '.join(path)}")
    print(f"Tổng chi phí đường đi: {total_cost}")


if __name__ == "__main__":
    bai2()
