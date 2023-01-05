# Get tree grid
grid = []
with open("day8-input.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

max_scenic_score = 0

for i in range(len(grid)):
    # Get edge trees
    for j in range(len(grid[0])):
        top = 0
        bot = 0
        left = 0
        right = 0

        # Edge trees
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
            continue

        # top viewing distance
        for k in range(i - 1, -1, -1):
            top += 1
            if grid[k][j] >= grid[i][j]:
                break

        # bot viewing distance
        for k in range(i + 1, len(grid)):
            bot += 1
            if grid[k][j] >= grid[i][j]:
                break

        # left viewing distance
        for k in range(j - 1, -1, -1):
            left += 1
            if grid[i][k] >= grid[i][j]:
                break

        # right viewing distance
        for k in range(j + 1, len(grid)):
            right += 1
            if grid[i][k] >= grid[i][j]:
                break

        # scenic score
        scenic_score = top * bot * left * right
        if max_scenic_score < scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)
