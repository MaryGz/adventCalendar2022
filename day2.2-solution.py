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

lose_comps = {
    'A' : 'S',
    'B' : 'R',
    'C' : 'P'
}

win_comps = {
    'A' : 'P',
    'B' : 'S',
    'C' : 'R'
}

draw_comps = {
    'A' : 'R',
    'B' : 'P',
    'C' : 'S'
}

outcomes = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

shapes = {
    "R" : 1,
    "P" : 2,
    "S" : 3
}

with open("day2-input.txt", "r") as f:
    for line in f:
        comp = line.split()
        outcome = comp[1]
        
        outcome_score = outcomes[outcome]
        
        if outcome == 'X':
            shape = lose_comps[comp[0]]
        elif outcome == 'Y':
            shape = draw_comps[comp[0]]
        elif outcome == 'Z':
            shape = win_comps[comp[0]]
            
        shape_score = shapes[shape]
        round_score = outcome_score + shape_score
        total_score += round_score

print(f"Your total score will be {total_score}")