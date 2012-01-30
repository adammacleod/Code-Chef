"""
CodeChef - Bytelandian gold coins

Problem Code: COINS
URL: http://www.codechef.com/problems/COINS
Author: Adam MacLeod <adam.macleod@gmail.com>
Created: 30/01/2012
"""

import sys 

def maxi(coin):
    if coin in coins:
        return coins[coin]        

    coins[coin] = max(coin, maxi(coin/2) + maxi(coin/3) + maxi(coin/4))

    return coins[coin]

coins = {0:0, 1:1}

for coin in sys.stdin:
    print maxi(int(coin))

