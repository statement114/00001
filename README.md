# Maze Pathfinder with A* Algorithm

A simple A* pathfinding visualization tool using **PyGame** that allows you to:

- **Set a start and end point by clicking on the maze**
- **Find the shortest path using A* algorithm**
- **Visualize the path in real-time in the PyGame window**



## 项目结构

```
MazePathfinder/
├── maze.py        # 迷宫生成与位置验证
├── pathfinder.py  # A* 路径查找算法
├── visualizer.py  # 完整图形界面展示与交互
├── main.py        # 主程序入口
├── README.md      # 项目说明文件
└── requirements.txt # 依赖文件（仅供安装使用）
```



## 安装依赖

确保你已经安装了 **PyGame**，使用以下命令安装（如果尚未安装）：

```bash
pip install pygame
```



## 如何运行

1. 启动终端并进入项目文件夹：
   ```
   cd MazePathfinder
   ```
2. 运行程序：
   ```
   python main.py
   ```



## 使用说明

1. **点击左上角的 10×10 区域**来设置**起点（Start）**。
2. **点击右下角的 10×10 区域**来设置**终点（End）**。
3. 一旦起点和终点都设置完毕，**A* 算法**将自动寻找最短路径。
4. 路径将以**绿色方块**表示，**黄色边框**高亮显示，起点为**蓝色**，终点为**红色**。
5. 如果找不到路径，**屏幕上会显示 "No path found."**。



## 坐标解释

- 迷宫的每个单元格坐标是 `(x, y)`，其中 `x` 是行号，`y` 是列号。
- PyGame 的画布是根据列数 (`y`) 做 Y 坐标，行数(`x`)做 X 坐标。
- 所以你的点 `(maze_x, maze_y)` 实际上是 `(x, y)` 格式，与路径查找统一。


## 示例运行结果

当点击左上角和右下角设置起点和终点后：

- `A*` 动态寻找路径。
- 路径节点被突出显示为绿色，边界为黄色。
- 程序将持续更新迷宫图像直到你关闭窗口。



## 扩展与功能建议

项目目前的功能已很完备，你可以考虑后续扩展以下功能：

| 功能建议 | 描述 |
| “重新生成迷宫”按钮 | 点击刷新迷宫，重新设置起点和终点 |
| 截图/保存路径为 GIF | 捕获绘图过程为 GIF 动画 |
| 在终端打印路径 | 以坐标形式输出路径 |
| 出路径到文件 | 保存路径到 `.txt` 或 `.csv` 文件 |
| 支持调整速度 | 通过 `clock.tick(30)` 或 `clock.tick(60)` 控制刷新频率 |
| 支持其他算法 | 例如 BFS、DFS、Dijkstra 或使用不同启发函数（如 Euclidean）|



## 依赖说明（通过 `requirements.txt` 安装）

如果你希望通过 `pip install -r requirements.txt` 来一键安装依赖，可以使用如下文件：

```txt
pygame
```



## 项目功能总结

| 功能 | 说明 |
|------|------|
| 迷宫生成 | 使用 `generate_maze()` 函数生成随机迷宫 |
| 路径查找 | 使用 A* 算法查找起点到终点的最短路径 |
| 图形界面 | 使用 PyGame 实现交互式可视化界面 |
| 用户交互 | 鼠标点击设置起点和终点 |
| 绘制路径 | 显示找到的路径，绿色高亮，黄色边框 |
| 路径长度 | 显示在屏幕角落，例如 "Path length: 5" |


## 技术细节说明

## A* 算法特点

- 使用 **Manhattan distance**（曼哈顿距离）作为启发函数。
- 每个节点包括：`g`（实际代价）、`h`（启发式估计）、`f = g + h`（优先级）。
- 每次只探索四个相邻格子（上下左右）。
- 一旦找到终点，算法立即返回路径。
