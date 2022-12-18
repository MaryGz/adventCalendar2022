#            [C]         [N] [R]
#[J] [T]     [H]         [P] [L]
#[F] [S] [T] [B]         [M] [D]
#[C] [L] [J] [Z] [S]     [L] [B]
#[N] [Q] [G] [J] [J]     [F] [F] [R]
#[D] [V] [B] [L] [B] [Q] [D] [M] [T]
#[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
#[W] [P] [P] [D] [G] [P] [B] [P] [V]
# 1   2   3   4   5   6   7   8   9

stacks = []
stacks.append(['W', 'B', 'D', 'N', 'C', 'F', 'J'])
stacks.append(['P', 'Z', 'V', 'Q', 'L', 'S', 'T'])
stacks.append(['P', 'Z', 'B', 'G', 'J', 'T'])
stacks.append(['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C'])
stacks.append(['G', 'V', 'B', 'J', 'S'])
stacks.append(['P', 'S', 'Q'])
stacks.append(['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N'])
stacks.append(['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R'])
stacks.append(['V', 'D', 'T', 'R'])

with open("day5-input.txt", "r") as f:
    for line in f:
        order = line.split()
        order.remove('move')
        order.remove('from')
        order.remove('to')
        
        qty = int(order[0])
        origin = int(order[1])-1
        destiny = int(order[2])-1
        
        crate = []
        
        for i in range(0,qty):
            crate.append(stacks[origin].pop())
            
        for i in range(0,qty):
            stacks[destiny].append(crate.pop())

message = []
for stack in stacks :
    message.append(stack.pop())

print(message)