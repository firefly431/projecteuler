with open('p067_triangle.txt') as f:
    tri = f.read()
tri = [[int(x) for x in line.split()] for line in tri.strip().splitlines()]
for y in range(len(tri) - 2, -1, -1):
    for x in range(len(tri[y])):
        tri[y][x] += max(tri[y + 1][x], tri[y + 1][x + 1])

print(tri[0][0])
