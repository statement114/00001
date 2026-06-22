import heapq
from maze import is_valid_position
class Node:
    def __init__(self, x, y, g=0, h=0, parent=None):
        self.x = x
        self.y = y
        self.g = g  # 实际代价
        self.h = h  # 启发式估计值（曼哈顿距离）
        self.f = g + h  # f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def a_star(maze, start, end):
    """使用 A* 算法找出从 start 到 end 的最短路径"""
    if not is_valid_position(maze, start[0], start[1]):
        print("Start position is invalid.")
        return None
    if not is_valid_position(maze, end[0], end[1]):
        print("End position is invalid.")
        return None

    if start == end:
        return [start]

    open_list = []
    closed_list = set()

    # 起点加入打开列表
    start_node = Node(start[0], start[1])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add((current_node.x, current_node.y))

        if (current_node.x, current_node.y) == (end[0], end[1]):
            path = []
            while current_node:
                path.append((current_node.y, current_node.x))  # (y, x) 是 path 的坐标格式
                current_node = current_node.parent
            return path[::-1]  # 反转路径，从起点到终点

        # 遍历四个相邻格子（上下左右）
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in neighbors:
            x, y = current_node.x + dx, current_node.y + dy

            if not is_valid_position(maze, x, y) or (x, y) in closed_list:
                continue

            neighbor_node = Node(x, y)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = abs(x - end[0]) + abs(y - end[1])  # 曼哈顿距离
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            neighbor_node.parent = current_node

            if (x, y) not in closed_list:
                heapq.heappush(open_list, neighbor_node)

    return None
