'''
Complex numbers are stored in the list numbers. Complete the code below so that it prints the complex number
with the largest modulus and the modulus of the number itself on separate lines.
'''

numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j,
           -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
z = 0.0
for i in numbers:
     if abs(i) > abs(z):
         z = i
print(z, abs(z), sep='\n')
