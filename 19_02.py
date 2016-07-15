# Paint a boolean matrix.
import collections

def flip_color(colors, x, y):
    dirs = zip([0, 1, 0, -1], [1, 0, -1, 0])
    color = colors[x][y]
    colors[x][y] = not color
    q = collections.deque([(x, y)])
    while q:
        cur_x, cur_y = q.popleft()
        for dir in dirs:
            new_x, new_y = cur_x + dir[0], cur_y + dir[1]
            if (new_x >= 0 and new_x < len(colors) and 
                new_y >= 0 and new_y < len(colors[0]) and 
                colors[new_x][new_y] == color):
                colors[new_x][new_y] = not color
                q.append((new_x, new_y))
