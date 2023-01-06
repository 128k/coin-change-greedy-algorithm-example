# Coin Change

A Python implementation of a greedy algorithm for finding the minimum number of coins needed to make a given amount of change.

## Usage

To use the min_coins function, simply pass in a list of coin denominations and the desired change amount:

```python
from coin_change import min_coins
print(min_coins([1, 5, 10, 25], 37)) # Output: 4
print(min_coins([1, 5, 10, 25], 100)) # Output: 4
print(min_coins([1, 3, 4], 6)) # Output: 2
```

## How it works

The min_coins function works by iterating through the list of coins in decreasing order of value, and adding the largest possible coin to the min_coins count until the change amount is less than the coin value. This guarantees that the minimum number of coins will be used to make the given amount of change.
