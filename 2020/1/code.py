# Advent of code Year 2020 Day 1 solution
# Author = Jayascript
# Date = December 2020

import itertools
import numpy as np


def iterate(combos):
    result =  [x for x in itertools.combinations(np.loadtxt("input.txt"), r=combos) if sum(x) == 2020]
    return np.prod(result[0])


print("Part One : "+ str(iterate(2)))



print("Part Two : "+ str(iterate(3)))
