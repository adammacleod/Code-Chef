"""
CodeChef - ATM 

Problem Code: HS08TEST
URL: http://www.codechef.com/problems/HS08TEST
Author: Adam MacLeod <adam.macleod@gmail.com>
Created: 29/01/2012
"""

input = raw_input()

# Using floats here is a bad idea, however the problem isn't complex enough to 
# warrant a more excessive solution.
amount, balance = input.split(' ', 1)
amount = float(amount)
balance = float(balance)

if int(amount % 5) is 0:
    if (amount + 0.50) <= balance:
        balance = balance - amount - 0.50

print '%.2f' % round(balance,2)
