from collections import deque


class EightPuzzle:
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def __init__(self, start_state):
        self.start = tuple(start_state)

    def get_neighbors(self, state):
        neighbors = []

        i = state.index(0)
        r, c = i // 3, i % 3

        candidates = [("up", -1, 0), ("down", 1, 0), ("right", 0, 1), ("left", 0, -1)]

        for act, dr, dc in candidates:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_i = nr * 3 + nc

                new_state = list(state)
                new_state[i], new_state[new_i] = (new_state[new_i], new_state[i])

                neighbors.append((act, tuple(new_state)))

        return neighbors

    def bfs(self):
        if self.start == self.goal:
            return [], 0

        op = deque([self.start])
        parent: dict = {self.start: (None, None)}
        visited = {self.start}
        nodes_exp = 0

        while op:
            state = op.popleft()
            nodes_exp += 1

            for act, neigh in self.get_neighbors(state):
                if neigh in visited:
                    continue

                parent[neigh] = (state, act)

                if neigh == self.goal:
                    return self.__reconstruct(parent, neigh), nodes_exp

                visited.add(neigh)
                op.append(neigh)

        return None, nodes_exp

    def __reconstruct(self, parent, goal):
        acts, cur = [], goal

        while parent[cur][0] is not None:
            prev, act = parent[cur]
            acts.append(act)
            cur = prev

        return list(reversed(acts))

    @staticmethod
    def pretty(state):
        rows = []
        for i in range(3):
            row = state[i * 3 : (i + 1) * 3]
            rows.append(" ".join(str(x) if x else "_" for x in row))
        return "\n".join(rows)


def bai2():
    print("\n" + "=" * 60)
    print("BÀI 2: BFS giải 8-Puzzle")
    print("=" * 60)
    
    # Test 1: trạng thái đơn giản
    start_easy = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    print("\n--- Test đơn giản ---")
    print("Trạng thái ban đầu:")
    print(EightPuzzle.pretty(start_easy))
    actions, expanded = EightPuzzle(start_easy).bfs()
    print(f"\nCác hàng động: {actions}")
    print(f"Số nút mở rộng: {expanded}")
    
    # Test 2: trạng thái slide bài giảng
    start_hard = (1, 4, 3, 7, 0, 6, 5, 8, 2)
    print("\n--- Test slide bài giảng ---")
    print("Trạng thái ban đầu:")
    print(EightPuzzle.pretty(start_hard))
    actions2, expanded2 = EightPuzzle(start_hard).bfs()
    if actions2 is not None:
        print(f"\nMở rộng: {len(actions2)} bước")
        print(f"Các hành động: {actions2}")
    else:
        print("\nKhông tìm thấy nghiệm")
    print(f"Số nút mở rộng: {expanded2}")

bai2()