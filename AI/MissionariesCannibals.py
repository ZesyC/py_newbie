from collections import deque


class MissionariesCannibals:
    OPERATORS = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    def __init__(self):
        self.start = (3, 3, 1)
        self.goal = (0, 0, 0)

    def bfs(self, verbose: bool = False):
        op = deque([self.start])
        closed = []
        parent = {self.start: (None, None)}

        step = 0
        while op:
            x = op.popleft()
            step += 1
            closed.append(x)

            if x == self.goal:
                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x},\n"
                        f"open = {list(op)},\n"
                        f"close = {closed}\n"
                    )
                return self._reconstruct(parent, x), closed

            for action, child in self._get_children(x):
                if child not in parent:
                    op.append(child)
                    parent[child] = (x, action)

            if verbose:
                print(
                    f"Buoc {step}:\n"
                    f"X = {x},\n"
                    f"open = {list(op)},\n"
                    f"close = {closed}\n"
                )

        return None, closed

    def _get_children(self, state):
        missionaries, cannibals, boat = state
        children = []

        for move_m, move_c in self.OPERATORS:
            if boat == 1:
                child = (
                    missionaries - move_m,
                    cannibals - move_c,
                    0
                )
            else:
                child = (
                    missionaries + move_m,
                    cannibals + move_c,
                    1
                )

            if self._is_valid(child):
                action = (move_m, move_c)
                children.append((action, child))

        return children

    def _is_valid(self, state):
        missionaries, cannibals, _ = state

        if not 0 <= missionaries <= 3 or not 0 <= cannibals <= 3:
            return False

        if missionaries > 0 and missionaries < cannibals:
            return False

        missionaries_right = 3 - missionaries
        cannibals_right = 3 - cannibals

        if (
            missionaries_right > 0
            and missionaries_right < cannibals_right
        ):
            return False

        return True

    def _reconstruct(self, parent, goal):
        path = []
        cur = goal

        while cur is not None:
            previous, action = parent[cur]
            path.append((cur, action))
            cur = previous

        return list(reversed(path))


def bai3():
    print("Bai 3: Bai toan nguoi truyen giao va ke an thit:")
    search = MissionariesCannibals()
    path, closed = search.bfs(verbose=True)

    if path is None:
        print("Khong tim thay loi giai.")
        return

    print("Duong di tim duoc:")
    for state, action in path:
        print(f"Trang thai: {state}, hanh dong: {action}")

    print(f"Tong so chuyen thuyen: {len(path) - 1}")
    print(f"Tong so trang thai duyet: {len(closed)}")


if __name__ == "__main__":
    bai3()
