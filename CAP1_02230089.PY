################################
# Thukten Yezer
# 1. Electrical
# 02230089
################################
# REFERENCES
# @CHAT_GPT
# @DQ-Logo
################################
# SOLUTION
# Your Solution Score: 50267
# CSF101-CAP/input_9_cap1.txt
################################

# Read the input file
def read_input(name_of_the_file):
    x = []
    with open(name_of_the_file, 'r') as file:
        while True:
            y = file.readline()
            if not y:
                break  # End of file
            opponent_choice, outcome = y.split()
            x.append((opponent_choice, outcome))
    return x

# To Calculate the score for each round
def calculate_score(Total_Number_of_rounds):
    Score = 0
    for opponent_choice, outcome in Total_Number_of_rounds:
        if outcome == 'X':  # Concede defeat
            if opponent_choice == 'A':
                Score =Score + 3  #  if pPaper blocks Rock
            elif opponent_choice == 'B':
                Score =Score + 1  # if cissors cuts Paper
            elif opponent_choice == 'C':
                Score = Score + 2  # if ock crushes sicssor
        elif outcome == 'Y':  # Draw
            if opponent_choice == 'A':
                Score = Score + 4  # if both showed rock so it's a draw
            elif opponent_choice == 'B':
                Score = Score + 5  # if both showed paper so it's a draw
            elif opponent_choice == 'C':
                Score = Score + 6  # if both showed scissor so it's a draw
        elif outcome == 'Z':  # Victory
            if opponent_choice == 'A':
                Score = Score + 8  # if paper beats rock
            elif opponent_choice == 'B':
                Score = Score + 9  # if scissor cuts paper
            elif opponent_choice == 'C':
                Score = Score + 7  # if rock crushes scissor
    print(f"The total score is:{Score}") #outcome : your total score is score

# To run a program by inputing the valid file name.
calculate_score(read_input("CSF101-CAP/input_9_cap1.txt"))

