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
                print(f"Bước {step}:\nX = {current},\nopen = {children},\nclose = {visited[:-1]}\n")

            if not children:
                return None, visited

            best_child = min(children, key=lambda node: self.heuristic[node])

            # Với heuristic khoảng cách đến đích, giá trị nhỏ hơn là tốt hơn.
            if self.heuristic[best_child] >= self.heuristic[current]:
                return None, visited

            current = best_child
            path.append(current)
            visited.append(current)

        return path, visited


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
