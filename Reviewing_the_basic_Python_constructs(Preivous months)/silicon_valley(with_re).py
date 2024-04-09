"""
Artificial intelligence Anton, created by Guilfoyle, hacked a network of smart refrigerators. Now he uses them as
servers for the Piebald Piper. Help the owner of the company find all the infected refrigerators.

For each refrigerator there is a data line consisting of lowercase letters and numbers, and if the word “anton” is
present in it (not necessarily adjacent letters, the main thing is the presence of a sequence of letters),
then the refrigerator is infected and you need to display the refrigerator number, numbering starts from one.

Input format The first line contains the number n – the number of refrigerators. In the next n lines,
lines containing Latin lowercase letters and numbers are entered, each line from 5 to 100 characters.

Output format The program should display the numbers of infected refrigerators separated by a space. If there are no
such refrigerators, there is no need to remove anything.
"""

# with "re" solving task
import re

n = int(input())

for i in range(n):
    s = input()

    if re.search(r"a.*n.*t.*o.*n", s):
        print(i + 1, end=" ")

#example
#input
"""
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
"""
#output
"""
1 2 7 8
"""
