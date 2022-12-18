total = 0

with open("day3-input.txt", "r") as f:
    for line in f:
        rucksack = list(line)
        if '\n' in rucksack:
            rucksack.remove('\n')
        half = int(len(rucksack)/2)
        comp1 = rucksack[:half]
        comp2 = rucksack[half:]
        item = set(comp1) & set(comp2)
        c = str(item)[2]
        asci = ord(c)
        if asci > 96:
            asci = asci - 96
        elif asci > 64:
            asci = asci - 38
        total += asci

print(total)
