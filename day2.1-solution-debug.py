#'A' 'X' - Rock
#'B' 'Y' - Paper
#'C' 'Z' - Scissors

#total_score -> sum of scroes of each round
#round_score = shape_score + outcome_score
#outcome_score: 
#0 if lose
#3 if draw
#6 if won

total_score = 0

lose_comps = [['A','Z'],['B','X'],['C','Y']]
win_comps = [['A','Y'],['B','Z'],['C','X']]
draw_comps = [['A','X'],['B','Y'],['C','Z']]

shapes = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

wincount = 0
drawcount = 0
losecount = 0
rockcount = 0
papercount = 0
scissorcount = 0
linecount = 0

with open("day2-input.txt", "r") as f:
    for line in f:
        linecount += 1
        comp = line.split()
        if comp in win_comps:
            outcome_score = 6
            wincount += 1
        elif comp in lose_comps:
            outcome_score = 0
            losecount += 1
        elif comp in draw_comps:
            outcome_score = 3
            drawcount +=1
        
        shape_score = shapes[comp[1]]
        if comp[1] == 'X':
            rockcount += 1
        elif comp[1] == 'Y':
            papercount += 1
        elif comp[1] == 'Z':
            scissorcount +=1
        
        round_score = outcome_score + shape_score
        total_score += round_score

print(f"Your total score will be {total_score}")

print(f"you had a total of {wincount} wins which equals {wincount*6}")
print(f"you had a total of {drawcount} draws which equals {drawcount*3}")
print(f"you had a total of {losecount} loses")

print(f"you had a total of {linecount} rounds")

print(f"you had a total of {rockcount} rocks which equals {rockcount*1}")
print(f"you had a total of {papercount} papers which equals {papercount*2}")
print(f"you had a total of {scissorcount} scissors which equals {scissorcount*3}")
                