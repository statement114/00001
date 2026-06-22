import pygame
import sys
from maze import generate_maze, is_valid_position,MAZE_HEIGHT,MAZE_WIDTH
from pathfinder import a_star

# 初始化 PyGame
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Pathfinder - A* Algorithm")

clock = pygame.time.Clock()

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 定义矩形区域（用于设置起点和终点）
START_RECT = pygame.Rect(0, 0, 10 * CELL_SIZE, 10 * CELL_SIZE)  # 左上角 10x10 块
END_RECT = pygame.Rect((MAZE_WIDTH - 10) * CELL_SIZE, (MAZE_HEIGHT - 10) * CELL_SIZE, 10 * CELL_SIZE, 10 * CELL_SIZE)

def draw_maze(maze, start, end, path):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            color = WHITE if maze[x][y] == 0 else BLACK
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

            # 判断是否在起点或终点区域
            if START_RECT.contains(rect):
                pygame.draw.rect(screen, BLUE, rect)  # 起点区域
            elif END_RECT.contains(rect):
                pygame.draw.rect(screen, RED, rect)  # 终点区域

            # 如果在路径中，就高亮显示
            if path is not None and (y, x) in path:
                pygame.draw.rect(screen, GREEN, rect)
                pygame.draw.rect(screen, YELLOW, rect, 2)

def show_instructions():
    font = pygame.font.SysFont("Arial", 20)
    text = font.render("Click on Start (Top-left block) and End (Bottom-right block) to set", True, BLACK)
    screen.blit(text, (20, 20))

def show_path_info(path):
    if path:
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"Path length: {len(path)}", True, BLACK)
        screen.blit(text, (20, 40))
    else:
        font = pygame.font.SysFont("Arial", 20)
        text = font.render("No path found.", True, RED)
        screen.blit(text, (20, 40))

def main():
    maze = generate_maze()  # 生成迷宫
    start = None
    end = None
    path = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # 起点设置逻辑
                if START_RECT.collidepoint(mouse_x, mouse_y):
                    maze_x = mouse_y // CELL_SIZE
                    maze_y = mouse_x // CELL_SIZE
                    if start is None:
                        start = (maze_x, maze_y)
                        print(f"Start set at: ({maze_x}, {maze_y})")
                    else:
                        print("Start set again.")

                # 终点设置逻辑
                elif END_RECT.collidepoint(mouse_x, mouse_y):
                    maze_x = mouse_y // CELL_SIZE
                    maze_y = mouse_x // CELL_SIZE
                    if end is None:
                        end = (maze_x, maze_y)
                        print(f"End set at: ({maze_x}, {maze_y})")
                    else:
                        print("End set again.")

                # 如果起点和终点都已设置，执行路径查找
                if start is not None and end is not None:
                    if is_valid_position(maze, start[0], start[1]) and is_valid_position(maze, end[0], end[1]):
                        path = a_star(maze, start, end)
                        if path is None:
                            print("No path found.")
                        else:
                            print("Found path:", path)

        # 清屏
        screen.fill(WHITE)

        # 绘制迷宫
        draw_maze(maze, start, end, path)

        # 显示提示信息
        show_instructions()

        # 显示路径信息
        show_path_info(path)

        # 更新屏幕
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
