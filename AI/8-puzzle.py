from collections import deque


class EightPuzzle:
    GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    MOVES = [
        ('up', -1, 0),
        ('down', 1, 0),
        ('left', 0, -1),
        ('right', 0, 1)
    ]

    def __init__(self, start):
        self.start = tuple(start)

    def bfs(self, verbose: bool = False):
        op = deque([self.start])
        closed = []
        parent = {self.start: (None, None)}

        step = 0
        while op:
            x = op.popleft()
            step += 1
            closed.append(x)

            if x == self.GOAL:
                if verbose:
                    print(f"Buoc {step}:")
                    print("X =")
                    print(self._format_state(x))
                    print(f"open = {len(op)} trang thai")
                    print(f"close = {len(closed)} trang thai\n")
                return self._reconstruct(parent, x), closed

            for action, child in self._get_children(x):
                if child not in parent:
                    op.append(child)
                    parent[child] = (x, action)

            if verbose:
                print(f"Buoc {step}:")
                print("X =")
                print(self._format_state(x))
                print(f"open = {len(op)} trang thai")
                print(f"close = {len(closed)} trang thai\n")

        return None, closed

    def _get_children(self, state):
        children = []
        empty_index = state.index(0)
        row, col = divmod(empty_index, 3)

        for action, row_change, col_change in self.MOVES:
            new_row = row + row_change
            new_col = col + col_change

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(state)
                new_state[empty_index], new_state[new_index] = (
                    new_state[new_index],
                    new_state[empty_index]
                )
                children.append((action, tuple(new_state)))

        return children

    def _reconstruct(self, parent, goal):
        actions = []
        cur = goal

        while parent[cur][0] is not None:
            previous, action = parent[cur]
            actions.append(action)
            cur = previous

        return list(reversed(actions))

    def _format_state(self, state):
        rows = []
        for i in range(0, 9, 3):
            row = state[i:i + 3]
            rows.append(' '.join(str(value) if value else '_' for value in row))
        return '\n'.join(rows)


def bai2():
    start = (1, 2, 3, 4, 5, 0, 6, 7, 8)

    print("Bai 2: BFS giai bai toan 8-Puzzle:")
    print("Trang thai ban dau:")
    print(EightPuzzle(start)._format_state(start))

    search = EightPuzzle(start)
    actions, closed = search.bfs(verbose=True)

    if actions is not None:
        print(f"Cac hanh dong: {actions}")
        print(f"Tong so buoc: {len(actions)}")
    else:
        print("Khong tim thay loi giai.")

    print(f"Tong so trang thai duyet: {len(closed)}")


if __name__ == "__main__":
    bai2()
