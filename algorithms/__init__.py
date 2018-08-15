from enum import Enum

"""
    algorithms

Contains various algorithms in use for backtesting. Currently, this directory
consists of:
    * coinToss
    * sma (SimpleMovingAverage)
    * identity
"""

class Choice(Enum): 
    BUY = 0
    SELL = 1
    STAY = 2
