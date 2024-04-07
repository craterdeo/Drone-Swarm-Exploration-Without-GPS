import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def generate_rrt(start, goal, grid, num_iterations=1000, step_size=10):
    nodes = [Node(start[0], start[1])]
    for _ in range(num_iterations):
        rand_node = Node(np.random.randint(0, grid.shape[0]), np.random.randint(0, grid.shape[1]))
        nearest_node_idx = nearest_node_index(nodes, rand_node)
        nearest_node = nodes[nearest_node_idx]

        new_node = step_from_to(nearest_node, rand_node, step_size)
        if is_valid(grid, new_node):
            new_node.parent = nearest_node
            nodes.append(new_node)

        if distance(new_node, goal) < step_size:
            final_node = step_from_to(new_node, goal, step_size)
            if is_valid(grid, final_node):
                final_node.parent = new_node
                nodes.append(final_node)
                return nodes

    return None

def nearest_node_index(nodes, rand_node):
    distances = [(node.x - rand_node.x)**2 + (node.y - rand_node.y)**2 for node in nodes]
    return np.argmin(distances)

def step_from_to(from_node, to_node, step_size):
    dist = distance(from_node, to_node)
    if dist < step_size:
        return to_node
    else:
        theta = np.arctan2(to_node.y - from_node.y, to_node.x - from_node.x)
        return Node(from_node.x + step_size * np.cos(theta), from_node.y + step_size * np.sin(theta))

def is_valid(grid, node):
    x = int(node.x)
    y = int(node.y)
    if x < 0 or x >= grid.shape[0] or y < 0 or y >= grid.shape[1]:
        return False
    return grid[x][y] == 0


def distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def reconstruct_path(goal_node):
    path = [(goal_node.x, goal_node.y)]
    current_node = goal_node
    while current_node.parent:
        current_node = current_node.parent
        path.append((current_node.x, current_node.y))
    return list(reversed(path))

def plot_rrt(grid, nodes, start, goal, path=None):
    plt.imshow(grid, cmap='gray', origin='lower')
    plt.plot(start[1], start[0], 'go', markersize=10)
    plt.plot(goal[1], goal[0], 'ro', markersize=10)

    for node in nodes:
        if node.parent:
            plt.plot([node.parent.y, node.y], [node.parent.x, node.x], 'c-')

    if path:
        for i in range(len(path) - 1):
            plt.plot([path[i][1], path[i + 1][1]], [path[i][0], path[i + 1][0]], 'b-', linewidth=2)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('RRT Navigation')
    plt.show()

# Example usage:
start = (10, 10)
goal = (90, 90)
grid = np.zeros((100, 100))  # Assuming a 100x100 grid, where 0 means free space
grid[20:80, 40:60] = 1  # Obstacle

nodes = generate_rrt(start, goal, grid)
if nodes is not None:
    path = reconstruct_path(nodes[-1])
    plot_rrt(grid, nodes, start, goal, path)
else:
    print("Failed to find a path!")
