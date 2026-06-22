import random

# 迷宫尺寸
MAZE_WIDTH = 30
MAZE_HEIGHT = 30
OBSTACLE_DENSITY = 0.3  # 障碍概率

def generate_maze(width=MAZE_WIDTH, height=MAZE_HEIGHT, obstacle_density=OBSTACLE_DENSITY):
    """生成一个 NxN 的随机迷宫，0 表示可以通行，1 表示障碍"""
    maze = [
        [random.choice([0, 1]) if random.random() < obstacle_density else 0 for _ in range(width)]
        for _ in range(height)
    ]
    return maze

def is_valid_position(maze, x, y):
    """检查给定位置是否有效（即在迷宫内且不是障碍）"""
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0
