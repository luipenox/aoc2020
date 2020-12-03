from itertools import combinations
from functools import reduce
import operator

numbers = []
with open("input.txt", encoding="utf-8") as f:
    for line in f:
        numbers.append(int(line.rstrip()))


def mul(x):
    return reduce(operator.mul, x, 1)


def is_2020(no_count):
    for combination in combinations(numbers, no_count):
        if sum(combination) == 2020:
            return mul(combination)


print(f'part 1: {is_2020(2)}')
print(f'part 2: {is_2020(3)}')