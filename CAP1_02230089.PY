################################
# Thukten Yezer
# 1 Electrical
# 02230089
################################
# REFERENCES
# @CHAT_GPT
# @Quilbit
# @Blackbox.ai
# @WB3 school
# @ Learn python from Android
################################
# SOLUTION
# Solution Score: 50267
# CSF101-CAP/input_9_cap1.txt
################################

# Reading the input file using the function read_input
def read_input(name_of_the_file):
    XY = [] #To store a data in the form of list due to repeatable letters
    with open(name_of_the_file, 'r') as file:
        while True:
            YY = file.readline()#readline() is used  to pause program execution and fordisplaying new information.
            if not YY:
                break 
            opponentchoice, result = YY.split()#split() is used to breaks a text string into a substrings
            XY.append((opponentchoice, result))
    return XY #Returning the function

# To Calculate the score for each round, using the function calculate_score
def calculate_score(Total_Number_of_rounds):
    Score = 0 #Evaluting a score starting from zero
    for opponentchoice, outcome in Total_Number_of_rounds:
        if outcome == 'X':  # if the outcome is X we must Concede defeat
            if opponentchoice == 'A':
                Score =Score + 3  #  If the opponent cast Rock, we must show scissors to lose
            elif opponentchoice == 'B':
                Score =Score + 1  #  If the opponent cast Paper, we must show rock to lose
            elif opponentchoice == 'C':
                Score = Score + 2  # If the opponent cast Scissor, we must show paper to lose

        elif outcome == 'Y':  #  if the outcome is Y, result must be declared as draw between opponent and us
            if opponentchoice == 'A':
                Score = Score + (3+1)  # if both we and the opponent cast rock, it's a draw
            elif opponentchoice == 'B':
                Score = Score + (3+2)  # if both we and the opponent cast paper, it's a draw
            elif opponentchoice == 'C':
                Score = Score + (3+3) # if both we and the opponent cast scissor, it's a draw

        elif outcome == 'Z':  #  if the outcome is Z we must win over the opponent.
            if opponentchoice == 'A':
                Score = Score + (6+2)  # if the opponent choose rock, we must choose paper to win 
            elif opponentchoice == 'B':
                Score = Score + (6+3)  # if the opponent choose paper, we must choose scissor to win
            elif opponentchoice == 'C':
                Score = Score + (6+1)  # if the opponent choose scissor, we must choose rock to win

    print(f"The total score is:{Score}") #outcome : your  Final total score is equal to score

# To run a program by inputing the valid file name which the fuction was called earlier.
calculate_score(read_input("CSF101-CAP/input_9_cap1.txt"))

