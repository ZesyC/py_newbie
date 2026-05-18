from __future__ import annotations
from collections import deque
import sys
import time
import random

class MissionariesCannibals:

    OPERATORS = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    def __init__(self):
        self.start = (3, 3, 1)
        self.goal = (0, 0 , 0)

    def is_vali(self, state):
        m, c, _ = state
        if not(0 <= m <= 3 and 0<= c <= 3): return False
        if m > 0 and m < c: return False
        m_r, c_r = 3 - m, 3 - c
        if m_r > 0 and m_r < c_r: return False
        return True
    
    def get_neighbors(self, state):
        m, c, b = state
        results = []

        for dm, dc in self.OPERATORS:
            if b == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)
            if self.is_vali(new_state):
                results.append(((dm, dc, b), new_state))

        return results
    
    def bfs(self):
        op = deque([self.start])
        parent: dict[tuple[int, int, int], tuple[tuple[int, int, int] | None, tuple[int, int, int] | None]] = {
            self.start: (None, None)
        }
        visited = {self.start}
        while op:
            state = op.popleft()
            if state == self.goal:
                return self.reconstruct(parent, state)
            for action, neighbor in self.get_neighbors(state):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = (state, action)
                    op.append(neighbor)

        return None
    
    def reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append((cur, parent[cur][1]))
            cur = parent[cur][0]
        return list(reversed(path))

def bai3():
    mc = MissionariesCannibals()
    sol = mc.bfs()
    if sol is None:
        print("Không tìm thấy nghiệm")
        return

    print("Đường đi tìm được:")
    for state, action in sol:
        print(state, action)
    print(f"Tìm được nghiệm với {len(sol) - 1} chuyến thuyền")


bai3()
