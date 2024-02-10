# Минимальное количество шагов для приведения к одному значению всех элементов списка

import sys

filename = sys.argv[1]
with open(filename) as file:
    nums = [int(line.strip()) for line in file]

avg = sum(nums) // len(nums)
min_moves = sum(abs(num - avg) for num in nums)

print(min_moves)
