from collections import deque


class IterativeDeepeningSearch:
    def __init__(self, graph: dict, start, goals):
        self.graph = graph
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def ids(self, max_depth: int = 50, verbose: bool = False):
        all_closed = []

        for limit in range(max_depth + 1):
            op = [(self.start, [self.start])]
            closed = []
            parent = {self.start: None}
            step = 0

            if verbose:
                print(f"Gioi han do sau = {limit}:")

            while op:
                x, path = op.pop()
                step += 1
                depth = len(path) - 1

                closed.append(x)

                if x in self.goals:
                    all_closed.extend(closed)
                    if verbose:
                        print(
                            f"Buoc {step}:\n"
                            f"X = {x}, depth = {depth},\n"
                            f"open = {[node for node, _ in op]},\n"
                            f"close = {closed}\n"
                        )
                    return self._reconstruct(parent, x), all_closed

                if depth < limit:
                    for child in reversed(self.graph.get(x, [])):
                        open_nodes = [node for node, _ in op]
                        if child not in path and child not in closed and child not in open_nodes:
                            op.append((child, path + [child]))
                            parent[child] = x

                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, depth = {depth},\n"
                        f"open = {[node for node, _ in op]},\n"
                        f"close = {closed}\n"
                    )

            all_closed.extend(closed)

            if verbose:
                print(f"Khong tim thay o do sau {limit}\n")

        return None, all_closed

    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


class BreadthFirstSearch:
    def __init__(self, graph: dict, start, goals):
        self.graph = graph
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def bfs(self, verbose: bool = False):
        op = deque([self.start])
        closed = []
        parent = {self.start: None}

        step = 0
        while op:
            x = op.popleft()
            step += 1

            closed.append(x)

            if x in self.goals:
                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x},\n"
                        f"open = {list(op)},\n"
                        f"close = {closed}\n"
                    )
                return self._reconstruct(parent, x), closed

            for child in self.graph.get(x, []):
                if child not in closed and child not in op:
                    op.append(child)
                    parent[child] = x

            if verbose:
                print(
                    f"Buoc {step}:\n"
                    f"X = {x},\n"
                    f"open = {list(op)},\n"
                    f"close = {closed}\n"
                )

        return None, closed

    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def tinh_chi_phi_duong_di(path, weights):
    if path is None:
        return None

    cost = 0
    for current_node, next_node in zip(path, path[1:]):
        edge = (current_node, next_node)
        if edge not in weights:
            edge = (next_node, current_node)
        cost += weights[edge]
    return cost


def dinh_dang_duong_di(path):
    if path is None:
        return "Khong tim thay"
    return " - ".join(path)


def in_bang_so_sanh(ids_path, ids_closed, bfs_path, bfs_closed, weights):
    ids_cost = tinh_chi_phi_duong_di(ids_path, weights)
    bfs_cost = tinh_chi_phi_duong_di(bfs_path, weights)

    print("\nBANG SO SANH")
    print("IDS:")
    print(f"- Duong di: {dinh_dang_duong_di(ids_path)}")
    print(f"- Chi phi: {ids_cost}")
    print(f"- So trang thai mo rong: {len(ids_closed)}")
    print(f"- Thu tu duyet: {ids_closed}")

    print("\nBFS:")
    print(f"- Duong di: {dinh_dang_duong_di(bfs_path)}")
    print(f"- Chi phi: {bfs_cost}")
    print(f"- So trang thai mo rong: {len(bfs_closed)}")
    print(f"- Thu tu duyet: {bfs_closed}")


def in_nhan_xet():
    print("\nNHAN XET")
    print(
        "- Ca IDS va BFS deu tim duoc duong di ngan nhat theo so canh la "
        "A - C - G - I, voi chi phi bang 3."
    )
    print(
        "- BFS mo rong it trang thai hon trong bai nay vi no duyet theo tung "
        "muc va khong lap lai cac dinh da dua vao hang doi."
    )
    print(
        "- IDS ton nhieu lan mo rong hon vi phai chay lai tu dinh A voi cac "
        "gioi han do sau tang dan, nen mot so dinh bi duyet lai nhieu lan."
    )


def bai_phan_2():
    print("PHAN 2: CODING VA DOI SANH IDS - BFS")

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F", "G"],
        "D": ["B"],
        "E": ["B", "H"],
        "F": ["C", "H"],
        "G": ["C", "I"],
        "H": ["E", "F", "I"],
        "I": ["G", "H"],
    }

    weights = {
        ("A", "B"): 1,
        ("A", "C"): 1,
        ("B", "D"): 1,
        ("B", "E"): 1,
        ("C", "F"): 1,
        ("C", "G"): 1,
        ("E", "H"): 1,
        ("F", "H"): 1,
        ("G", "I"): 1,
        ("H", "I"): 1,
    }

    start = "A"
    goal = "I"

    print(f"Dinh xuat phat: {start}")
    print(f"Dinh dich: {goal}")

    ids_search = IterativeDeepeningSearch(graph, start=start, goals=goal)
    ids_path, ids_closed = ids_search.ids(max_depth=10, verbose=False)

    bfs_search = BreadthFirstSearch(graph, start=start, goals=goal)
    bfs_path, bfs_closed = bfs_search.bfs(verbose=False)

    in_bang_so_sanh(ids_path, ids_closed, bfs_path, bfs_closed, weights)
    in_nhan_xet()


if __name__ == "__main__":
    bai_phan_2()
