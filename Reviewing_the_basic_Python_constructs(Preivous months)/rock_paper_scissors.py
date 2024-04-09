"""
Timur and Ruslan play the game Rock, Paper, Scissors, Lizard, Spock. Help the kids cast fair lots again and determine
who will do the next module in the new course.

Input format
The program receives two lines of text as input, containing one word each from the list of “rock”, “scissors”,
“paper”, “lizard” or “Spock”. The first line records Timur's choice, the second line records Ruslan's choice.

Output format
The program should display the result of the draw: who won - Timur or Ruslan, or they tied.
"""

a, b = input(), input()

# Initialize a counter for the number of possible winning combinations
count = 0

# Define the rules of the game
rules = {'rock': ('lizard', 'scissors'), 'scissors': ('lizard', 'paper'), 'paper': ('spock', 'rock'),
         'lizard': ('spock', 'paper'), 'spock': ('scissors', 'rock')}

# Iterate through the rules
for key, value in rules.items():
    # If the choice of 'a' is a key and the choice of 'b' is in the corresponding tuple of winning values
    if a in key and b in value:
        count += 1

# Determine the winner based on the count of winning combinations
if count >= 1:
    print('Timur')
elif a == b:
    print('draw')
else:
    print('Ruslan')

