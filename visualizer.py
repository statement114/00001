import pygame
import sys
from maze import generate_maze, is_valid_position
from pathfinder import a_star

# 初始化 Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Pathfinder - A* Algorithm")

clock = pygame.time.Clock()

# 颜色设定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 显示迷宫
def draw_maze(maze, start, end, path):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            color = WHITE if maze[x][y] == 0 else BLACK
            pygame.draw.rect(screen, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if (x, y) == start:
                pygame.draw.circle(screen, BLUE, (y * CELL_SIZE + 10, x * CELL_SIZE + 10), 5)
            elif (x, y) == end:
                pygame.draw.circle(screen, RED, (y * CELL_SIZE + 10, x * CELL_SIZE + 10), 5)
            if (x, y) in path:
                pygame.draw.rect(screen, GREEN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# 主循环函数
def main():
    width, height = 30, 30
    maze = generate_maze(width, height)
    start = (0, 0)
    end = (height - 1, width - 1)

    # 设置起点和终点
    start_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
    end_rect = pygame.Rect((width-1)*CELL_SIZE, (height-1)*CELL_SIZE, CELL_SIZE, CELL_SIZE)

    running = True
    while running:
        screen.fill(WHITE)

        # 绘制迷宫
        draw_maze(maze, start, end, [])

        # 显示提示信息
        font = pygame.font.SysFont("Arial", 20)
        text = font.render("Click on start and end to set", True, BLACK)
        screen.blit(text, (20, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 设置起点和终点
                if start_rect.collidepoint(event.pos):
                    start = (event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE)
                elif end_rect.collidepoint(event.pos):
                    end = (event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE)

                # 执行 A* 算法
                path = a_star(maze, start, end)
                if path:
                    print("Found path:", path)
                else:
                    print("No path found.")

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
