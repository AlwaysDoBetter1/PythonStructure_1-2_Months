'''
Print the sum of the largest and smallest digit of the Decimal number.
'''

from decimal import *
num = Decimal(input())
if int(num) != 0:
    print(max(num.as_tuple().digits) + min(num.as_tuple().digits))
else:
    print(max(num.as_tuple().digits))


# input:
# 12.1244354689
# output:
# 10
