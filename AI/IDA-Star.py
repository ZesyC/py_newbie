class IDAStarSearch:
    def __init__(self, graph: dict, heuristic: dict, start, goals, alpha=1):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)
        self.alpha = alpha

    def ida_star(self, verbose: bool = False):
        threshold = self._f_score(0, self.start)
        closed = []
        iteration = 0

        while True:
            path = [self.start]
            visited = {self.start}
            iteration += 1

            if verbose:
                print(
                    f"Lần lặp {iteration}:\n"
                    f"threshold = {threshold}\n"
                )

            next_threshold, result, total_cost = self._search(
                x=self.start,
                cost_from_start=0,
                threshold=threshold,
                path=path,
                visited=visited,
                closed=closed,
                verbose=verbose
            )

            if result is not None:
                return result, closed, total_cost

            if next_threshold == float('inf'):
                return None, closed, float('inf')

            threshold = next_threshold

    def _search(
        self,
        x,
        cost_from_start,
        threshold,
        path,
        visited,
        closed,
        verbose
    ):
        current_f = self._f_score(cost_from_start, x)
        closed.append(x)

        if verbose:
            print(
                f"X = {x}, g(X) = {cost_from_start}, "
                f"h(X) = {self.heuristic[x]}, f(X) = {current_f},\n"
                f"path = {path}\n"
            )

        if current_f > threshold:
            return current_f, None, float('inf')

        if x in self.goals:
            return current_f, path.copy(), cost_from_start

        next_threshold = float('inf')

        for child, cost in self.graph.get(x, []):
            if child in visited:
                continue

            path.append(child)
            visited.add(child)

            result_threshold, result, total_cost = self._search(
                x=child,
                cost_from_start=cost_from_start + cost,
                threshold=threshold,
                path=path,
                visited=visited,
                closed=closed,
                verbose=verbose
            )

            if result is not None:
                return result_threshold, result, total_cost

            next_threshold = min(next_threshold, result_threshold)
            path.pop()
            visited.remove(child)

        return next_threshold, None, float('inf')

    def _f_score(self, cost_from_start, node):
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
    print(f"Bài 2: IDA* từ S đến G với alpha = {alpha}:")
    search = IDAStarSearch(
        graph, heuristic, start='S', goals={'G'}, alpha=alpha
    )
    path, closed, total_cost = search.ida_star(verbose=True)

    if path is not None:
        print(f"Đường đi tìm được: {' - '.join(path)}")
        print(f"Tổng chi phí đường đi: {total_cost}")
    else:
        print("Không tìm thấy đường đi.")

    print(f"Thứ tự duyệt: {closed}")
    print(f"Tổng số nút duyệt: {len(closed)}")


if __name__ == "__main__":
    bai2()
