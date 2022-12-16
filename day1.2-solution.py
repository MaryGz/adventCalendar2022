import math

top3elves = [0,0,0]
top3max = [0,0,0]

currentSum = 0
currentElf = 1

with open("day1-input.txt", "r") as f:
    for line in f:

        if line.strip():
            currentSum += int(line)
        else:
            if currentSum > min(top3max) :
                top3elves[top3max.index(min(top3max))] = currentElf
                top3max[top3max.index(min(top3max))] = currentSum

            currentElf += 1
            currentSum = 0
        
    

finalAnswer=zip(top3elves,top3max)

for elf, cal in finalAnswer:
    print(f"Elf {elf} has {cal} calories")

print(f"the total is {sum(top3max)}")