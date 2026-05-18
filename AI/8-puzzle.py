from collections import deque
import sys


class EightPuzzle:
    """8-Puzzle, trạng thái là tuple gồm 9 phần tử, 0 là ô trống."""

    GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def __init__(self, start_state):
        self.start = tuple(start_state)

    def get_neighbors(self, state):
        neighbors = []
        idx = state.index(0)
        row, col = idx // 3, idx % 3
        candidates = [
            ("Up", -1, 0),
            ("Down", 1, 0),
            ("Left", 0, -1),
            ("Right", 0, 1),
        ]

        for action, dr, dc in candidates:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_idx = nr * 3 + nc
                new_state = list(state)
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                neighbors.append((action, tuple(new_state)))

        return neighbors

    def bfs(self):
        if self.start == self.GOAL:
            return [], 0

        open_list = deque([self.start])
        parent = {self.start: (None, None)}
        visited = {self.start}
        nodes_expanded = 0

        while open_list:
            state = open_list.popleft()
            nodes_expanded += 1

            for action, neighbor in self.get_neighbors(state):
                if neighbor in visited:
                    continue

                parent[neighbor] = (state, action)
                if neighbor == self.GOAL:
                    return self._reconstruct(parent, neighbor), nodes_expanded

                visited.add(neighbor)
                open_list.append(neighbor)

        return None, nodes_expanded

    def _reconstruct(self, parent, goal):
        actions, cur = [], goal
        while parent[cur][0] is not None:
            prev, act = parent[cur]
            actions.append(act)
            cur = prev
        return list(reversed(actions))

    @staticmethod
    def pretty(state):
        rows = []
        for i in range(3):
            row = state[i * 3:(i + 1) * 3]
            rows.append(" ".join(str(x) if x else "_" for x in row))
        return "\n".join(rows)


def bai2():
    print("\n" + "=" * 60)
    print("BÀI 2: BFS giải 8-Puzzle")
    print("=" * 60)

    start_easy = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    print("\nTest đơn giản")
    print("Trạng thái ban đầu:")
    print(EightPuzzle.pretty(start_easy))
    actions, expanded = EightPuzzle(start_easy).bfs()
    print(f"\nNghiệm: {actions}")
    print(f"Số nút mở rộng: {expanded}")

    start_hard = (1, 4, 3, 7, 0, 6, 5, 8, 2)
    print("\nTest slide bài giảng")
    print("Trạng thái ban đầu:")
    print(EightPuzzle.pretty(start_hard))
    actions2, expanded2 = EightPuzzle(start_hard).bfs()

    if actions2 is None:
        print("\nKhông tìm thấy nghiệm")
    else:
        print(f"\nNghiệm dài: {len(actions2)} bước")
        print(f"Các hành động: {actions2}")
    print(f"Số nút mở rộng: {expanded2}")

bai2()
