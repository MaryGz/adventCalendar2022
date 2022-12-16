import math

currentMax = 0
maxElf = 1
currentSum = 0
currentElf = 1

with open("day1-input.txt", "r") as f:
    for line in f:
        if line != "\n":
            currentSum += int(line)
        else:
            if currentSum > currentMax :
                currentMax = currentSum
                maxElf = currentElf
            currentElf += 1
            currentSum = 0

solution = f"The elf number {maxElf} wins with {currentMax} stars"
print(solution)