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

with open("day2-input.txt", "r") as f:
    for line in f:
        comp = line.split()
        if comp in win_comps:
            outcome_score = 6
        elif comp in lose_comps:
            outcome_score = 0
        elif comp in draw_comps:
            outcome_score = 3
        
        shape_score = shapes[comp[1]]
        
        round_score = outcome_score + shape_score
        total_score += round_score

print(f"Your total score will be {total_score}")