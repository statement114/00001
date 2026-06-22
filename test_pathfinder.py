from pathfinder import a_star
from maze import generate_maze
def test_maze():
    maze = generate_maze(30, 30)
    start = (0, 0)
    end = (29, 29)
    path = a_star(maze, start, end)
    print("Path found:", path)
test_maze()
