# corners, so add 1
width = 21
height = 21
grid = [x[:] for x in [[0] * width] * height]

def get(x, y):
    if x < 0 or y < 0:
        return 0
    try:
        return grid[y][x]
    except IndexError:
        raise
        return 0

def set(x, y, v):
    global grid
    try:
        grid[y][x] = v
    except IndexError:
        raise
        return

for y in range(height):
    for x in range(width):
        if x == 0 or y == 0:
            set(x, y, 1)
        else:
            set(x, y, get(x - 1, y) + get(x, y - 1))

print(get(width - 1, height - 1))
