class IDAStarSearch:
    def __init__(self, graph: dict, heuristic: dict, start, goals, alpha: float = 1.0):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)
        self.alpha = alpha

    def ida_star(self, verbose: bool = False):
        threshold = self.f_score(0, self.start)
        path = [self.start]
        close = []

        step = 0
        while True:
            visited = {self.start}
            step += 1

            if verbose:
                print(f"Lần lặp {step}:")
                print(f"  Ngưỡng hiện tại: {threshold}")

            new_threshold, result_path, total_cost = self.search(
                self.start,
                cost_from_start=0,
                threshold=threshold,
                path=path,
                visited=visited,
                close=close,
                verbose=verbose
            )

            if result_path is not None:
                return result_path, close, total_cost

            if new_threshold == float('inf'):
                return None, close, float('inf')

            threshold = new_threshold
            if verbose:
                print(f"  Tăng ngưỡng lên: {threshold}\n")

    def search(
        self,
        x,
        cost_from_start,
        threshold,
        path,
        visited,
        close,
        verbose: bool = False
    ):
        current_f_score = self.f_score(cost_from_start, x)
        close.append(x)

        if verbose:
            print(
                f"  X = {x}, "
                f"g={cost_from_start}, h={self.heuristic[x]}, f={current_f_score}"
            )
            print(f"  path hiện tại: {' -> '.join(path)}")

        if current_f_score > threshold:
            if verbose:
                print(f"  f({x}) vượt ngưỡng {threshold}, quay lui")
            return current_f_score, None, float('inf')

        if x in self.goals:
            if verbose:
                print(f"  Gặp đích: {x}\n")
            return current_f_score, path.copy(), cost_from_start

        min_next_threshold = float('inf')

        for child, cost in self.graph.get(x, []):
            if child in visited:
                continue

            visited.add(child)
            path.append(child)

            result_threshold, result_path, total_cost = self.search(
                child,
                cost_from_start + cost,
                threshold,
                path,
                visited,
                close,
                verbose
            )

            if result_path is not None:
                return result_threshold, result_path, total_cost

            min_next_threshold = min(min_next_threshold, result_threshold)

            path.pop()
            visited.remove(child)

        return min_next_threshold, None, float('inf')

    def f_score(self, cost_from_start, node):
        return cost_from_start + self.alpha * self.heuristic[node]


def bai2():
    graph = {
        'S': [('B', 1), ('A', 1)],
        'A': [('S', 1), ('B', 9)],
        'B': [('C', 6), ('G', 12), ('S', 1), ('A', 9)],
        'C': [('G', 5), ('B', 6)],
        'G': [('C', 5), ('B', 12)]
    }
    heuristic = {
        'S': 7,
        'A': 10,
        'B': 9,
        'C': 5,
        'G': 0
    }

    alpha = 2
    print(f"Từ S đến G bằng IDA* với alpha = {alpha}:")
    find = IDAStarSearch(graph, heuristic, start='S', goals='G', alpha=alpha)
    path, close, total_cost = find.ida_star(verbose=True)
    print(f"Thứ tự các nút được xét: {' -> '.join(close)}")
    if path is None:
        print("Không tìm thấy đường đi từ S đến G.")
        return

    print(f"Đường đi tìm được: {' -> '.join(path)}")
    print(f"Tổng chi phí đường đi: {total_cost}")


if __name__ == "__main__":
    bai2()
