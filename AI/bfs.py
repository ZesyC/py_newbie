from __future__ import annotations
from collections import deque
import sys
import time
import random

class Breadth_first_search:
    def __init__(self, graph: dict, start, goals):
        self.graph = graph
        self.start = start
        self.goals = set(goals) if not isinstance(goals, set) else goals

    def bfs(self):
        op = deque([self.start])
        close = []
        parent = {self.start: None}
        
        while op:
            x = op.popleft()

            if x in self.goals:
                close.append(x)
                return self.reconstruct(parent, x), close
            
            close.append(x)
            for child in self.graph.get(x, []):
                if child not in close and child not in op:
                    op.append(child)
                    parent[child] = x

        return None, close
    
    def reconstruct(self, parent, goals):
        path, cur = [], goals
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))
    
def bai_1():
    graph = {
        'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'],
        'D': ['I', 'J'], 'E': ['K', 'L', 'M'], 'F': [],
        'G': ['N'], 'H': ['O', 'P'], 'I': ['P', 'Q'],
        'J': ['R'], 'K': ['S'], 'L': ['T'], 'M': [],
        'N': [], 'O': [], 'P': ['U'], 'Q': [], 'R': [],
        'S': [], 'T': [], 'U': []
        }
    
    find = Breadth_first_search(graph, start='A', goals='U')
    path, close = find.bfs()
    print(f"Đường đi tìm được: {'-'.join(path) if path else 'Không tìm thấy'}")
    print(f"Tổng số nút đã duyệt: {len(close)}")
    
bai_1()