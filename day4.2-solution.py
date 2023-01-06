subset_count = 0

with open("day4-input.txt",  "r") as f:
    for line in f:
        pair =line.replace('\n','').split(',')
        range_elf1 = pair[0].split('-')
        range_elf2 = pair[1].split('-')
        
        elf1 = set(range(int(range_elf1[0]),int(range_elf1[1])+1))
        elf2 = set(range(int(range_elf2[0]),int(range_elf2[1])+1))
        
        if elf1.intersection(elf2):
            subset_count += 1

print(subset_count)
