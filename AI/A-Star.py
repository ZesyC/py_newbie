import time
import tracemalloc
from queue import PriorityQueue


def a_star_search(graph, heuristic, start, goal):
    """
    Tìm đường đi ngắn nhất từ start đến goal bằng thuật toán A*.

    graph: lưu các cạnh và chi phí giữa các đỉnh
    heuristic: lưu h(n), tức chi phí ước lượng từ mỗi đỉnh đến đích
    start: đỉnh bắt đầu
    goal: đỉnh kết thúc
    """

    # open_set lưu các đỉnh sẽ xét.
    # Mỗi phần tử có dạng: (f_score, node)
    open_set = PriorityQueue()
    open_set.put((heuristic[start], start))

    # came_from dùng để lưu đường đi.
    # Ví dụ: came_from['D'] = 'A' nghĩa là trước D là A.
    came_from = {}

    # g_score lưu chi phí thật từ start đến từng đỉnh.
    # Ban đầu chưa biết đường đi nên gán là vô cực.
    g_score = {}
    for node in heuristic:
        g_score[node] = float('inf')

    # Đi từ start đến chính nó thì chi phí bằng 0.
    g_score[start] = 0

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = [goal]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph[current]:
            new_cost = g_score[current] + cost

            if new_cost < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = new_cost

                f_score = new_cost + heuristic[neighbor]
                open_set.put((f_score, neighbor))

    return None, float('inf')


# Đồ thị của bài 2.
# Mỗi đỉnh trỏ đến danh sách các đỉnh kề và chi phí đi đến đỉnh đó.
graph = {
    'A': [('C', 9), ('D', 7), ('E', 13), ('F', 20)],
    'C': [('H', 6)],
    'D': [('H', 8), ('E', 4)],
    'E': [('K', 4), ('I', 3)],
    'F': [('I', 6)],
    'H': [('K', 5)],
    'K': [('B', 6)],
    'I': [('K', 9), ('B', 5)],
    'B': [],
}

# Giá trị heuristic h(n) của từng đỉnh.
heuristic = {
    'A': 14,
    'C': 15,
    'D': 9,
    'E': 8,
    'F': 7,
    'H': 10,
    'K': 2,
    'I': 4,
    'B': 0,
}


if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'B'

    tracemalloc.start()
    start_time = time.perf_counter()

    path, cost = a_star_search(graph, heuristic, start_node, goal_node)

    end_time = time.perf_counter()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    if path is None:
        print(f"Không tìm thấy đường đi từ {start_node} đến {goal_node}")
    else:
        print("Đường đi ngắn nhất:", " -> ".join(path))
        print("Chi phí:", cost)

    print(f"Thời gian chạy: {end_time - start_time:.6f} giây")
    print(f"Bộ nhớ hiện tại: {current_memory / 1024:.2f} KB")
    print(f"Bộ nhớ đỉnh: {peak_memory / 1024:.2f} KB")
