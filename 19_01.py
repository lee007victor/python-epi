# Search a maze.
# input:
# maze: [[0, 1, ...], ...], 0 for black points; 1 for white points
# ptr_s, ptr_end: (x, y)

def search_maze(maze, ptr_s, ptr_end):
    path = []
    x, y = ptr_s[0], ptr_s[1]
    maze[x][y] = 0
    path.append(ptr_s)
    if not is_reachable(maze, ptr_s, ptr_e, path):
        path.pop()
    return path

def is_reachable(maze, ptr_s, ptr_e, path):
    if ptr_s == ptr_e:
        return True
    for d_x, d_y in zip((1, 0, -1, 0), (0, 1, 0, -1)):
        new_x, new_y = ptr_s[0] + d_x, ptr_s[1] + d_y
        new_ptr = (new_x, new_y)
        if is_feasible(new_x, new_y, maze):
            maze[new_x][new_y] = 0
            path.append(new_ptr)
            if is_reachable(maze, new_ptr, ptr_end, path):
                return True
            path.pop()
    return False

def is_feasible(x, y, maze):
    return (x >= 0 and y >= 0 and
            x < len(maze) and y < len(maze[0]) and
            maze[x][y] == 1)
