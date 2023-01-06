def min_coins(coins, change):
  min_coins = 0
  for coin in coins:
    while change >= coin:
      change -= coin
      min_coins += 1
  return min_coins

print(min_coins([1, 5, 10, 25], 37)) # Output: 4
print(min_coins([1, 5, 10, 25], 100)) # Output: 4
print(min_coins([1, 3, 4], 6)) # Output: 2
