import random

# 存储迷宫尺寸和障碍密度的常量
MAZE_WIDTH = 30
MAZE_HEIGHT = 30
OBSTACLE_DENSITY = 0.3

def generate_maze(width=MAZE_WIDTH, height=MAZE_HEIGHT, obstacle_density=OBSTACLE_DENSITY):
    """生成一个随机的迷宫（0为通路，1为障碍）"""
    maze = [
        [random.choice([0, 1]) if random.random() < obstacle_density else 0 for _ in range(width)]
        for _ in range(height)
    ]
    return maze

def is_valid_position(maze, x, y):
    """检查坐标是否在迷宫内且不是障碍"""
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

# 手动设置起点和终点的边界框
START_RECT = (0, 0, 10, 10)  # 左上角
END_RECT = (MAZE_WIDTH - 10, MAZE_HEIGHT - 10, 10, 10)  # 右下角
