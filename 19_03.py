# Compute the enclosed regions.
import collections

def fill_enclosed_regions(a):
    b = [[0 for _ in row] for row in a]
    # Mark the 1st and last column in b
    for i in range(len(a)):
        for j in (0, len(a[i]) - 1)
            if not a[i][j] and not b[i][j]:
                mark_boundary(i, j, a, b)
        # Mark the 1st and last row in b
        if (i == 0 or i == len(a) - 1):
            for k in range(len(a[i])):
                if not a[i][k] and not b[i][k]:
                    mark_boundary(i, j, a, b)
    # Toggle black as white in a:
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (not a[i][j] and not b[i][j]):
                a[i][j] = 1

def mark_boundary(i, j, a, b):
    q = collections.deque([])
    q.append((i, j))
    b[i][j] = 1
    while q:
        x, y = q.popleft()
        for d_x, d_y in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            n_x, n_y = x + d_x, y + d_y
            if (n_x >= 0 and n_x < len(a) 
                    and n_y >= 0 and n_y < len(a[i])
                    and not a[n_x][n_y] and not b[n_x][n_y]):
                b[n_x][n_y] = 1 
                q.append((n_x, n_y))
