import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0  # 实际代价
        self.h = 0  # 启发函数
        self.f = 0  # 总代价
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def a_star(maze, start, end):
    """实现 A* 算法"""
    open_list = []
    closed_list = set()
    start_node = Node(start[0], start[1])
    end_node = Node(end[0], end[1])

    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)
        if current == end_node:
            return reconstruct_path(current)

        closed_list.add((current.x, current.y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x = current.x + dx
            next_y = current.y + dy

            if is_valid_position(maze, next_x, next_y) and (next_x, next_y) not in closed_list:
                next_node = Node(next_x, next_y)
                next_node.g = current.g + 1
                next_node.h = abs(next_x - end_node.x) + abs(next_y - end_node.y)  # 曼哈顿距离
                next_node.f = next_node.g + next_node.h
                next_node.parent = current
                heapq.heappush(open_list, next_node)

    return None  # 没有找到路径

def reconstruct_path(node):
    """回溯路径"""
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    return path[::-1]
