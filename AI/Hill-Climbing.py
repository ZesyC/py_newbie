class Steepest_ascent_hill_climbing:
    def __init__(self, graph: dict, heuristic: dict, start, goals):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def hill_climbing(self, verbose: bool = False):
        current = self.start
        path = [current]
        visited = [current]

        step = 0
        while current not in self.goals:
            children = [
                child for child in self.graph.get(current, [])
                if child not in visited
            ]
            step += 1
            if verbose:
                print(f"Bước {step}:")
                print(f"  Node hiện tại: {current}(h={self.heuristic[current]})")
                print(f"  Ứng viên: {self.format_nodes(children)}")
                print(f"  Đã đi qua: {visited[:-1]}")

            if not children:
                if verbose:
                    print("  Không còn node con để đi tiếp.\n")
                return None, visited

            best_child = min(children, key=lambda node: self.heuristic[node])
            if verbose:
                print(f"  Chọn tốt nhất: {best_child}(h={self.heuristic[best_child]})")

            # Với heuristic khoảng cách đến đích, giá trị nhỏ hơn là tốt hơn.
            if self.heuristic[best_child] >= self.heuristic[current]:
                if verbose:
                    print("  Dừng: node tốt nhất không tốt hơn node hiện tại.\n")
                return None, visited

            current = best_child
            path.append(current)
            visited.append(current)
            if verbose:
                print(f"  Đường đi hiện tại: {' -> '.join(path)}\n")

        return path, visited

    def format_nodes(self, nodes):
        return '[' + ', '.join(
            f"{node}(h={self.heuristic[node]})" for node in nodes
        ) + ']'


def bai1():
    graph = {
        'S': ['A', 'D'],
        'A': ['B', 'C'],
        'D': ['E', 'F'],
        'B': [],
        'C': [],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }
    heuristic = {
        'S': 12, 'A': 10, 'D': 9, 'B': 7,
        'C': 8, 'E': 6, 'F': 4, 'G': 0
    }
    edge_cost = {
        ('S', 'A'): 4, ('S', 'D'): 3,
        ('A', 'B'): 5, ('A', 'C'): 2,
        ('D', 'E'): 6, ('D', 'F'): 3,
        ('F', 'G'): 5, ('E', 'G'): 2
    }

    find = Steepest_ascent_hill_climbing(
        graph, heuristic, start='S', goals='G'
    )
    path, visited = find.hill_climbing(verbose=True)

    print(f"Thứ tự các nút được chọn: {' -> '.join(visited)}")
    if path is None:
        print("Không tìm thấy đường đi từ S đến G.")
        return

    total_cost = sum(edge_cost[(a, b)] for a, b in zip(path, path[1:]))
    print(f"Đường đi tìm được: {' -> '.join(path)}")
    print(f"Tổng chi phí đường đi: {total_cost}")


if __name__ == "__main__":
    bai1()
