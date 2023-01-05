# Get tree grid
grid = []
with open("day8-input.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

visible = []

for i in range(len(grid)):
    # Get edge trees
    for j in range(len(grid[0])):
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
            if [i, j] not in visible:
                visible.append([i, j])
            continue

    max_left = -1
    max_right = -1

    # Get trees visble from the left
    for j in range(len(grid[0])):
        if int(grid[i][j]) > int(max_left):
            if [i, j] not in visible:
                visible.append([i, j])
            max_left = grid[i][j]

    # Get trees visible from the right
    for j in range(len(grid[0]) - 1, -1, -1):
        if int(grid[i][j]) > int(max_right):
            if [i, j] not in visible:
                visible.append([i, j])
            max_right = grid[i][j]


for j in range(len(grid[0])):
    max_top = -1
    max_bot = -1

    # Get trees visible from the top
    for i in range(len(grid)):
        if int(grid[i][j]) > int(max_top):
            if [i, j] not in visible:
                visible.append([i, j])
            max_top = grid[i][j]

    # Get trees visible from the bottom
    for i in range(len(grid) - 1, -1, -1):
        if int(grid[i][j]) > int(max_bot):
            if [i, j] not in visible:
                visible.append([i, j])
            max_bot = grid[i][j]


print(len(visible))