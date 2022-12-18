total = 0
group = 1
r_group = []

with open("day3-input.txt", "r") as f:
    for line in f:
        rucksack = list(line)
        if '\n' in rucksack:
            rucksack.remove('\n')
        r_group.append(rucksack)
        
        if group == 3:
            badge = set(r_group[0]) & set(r_group[1]) & set(r_group[2])
            r_group = []
            group = 1
            
            c = str(badge)[2]
            asci = ord(c)
            if asci > 96:
                asci = asci - 96
            elif asci > 64:
                asci = asci - 38
            total += asci
        else:
            group += 1 
            


print(total)
