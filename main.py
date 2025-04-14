from random import randint
from math import comb
from itertools import combinations


N = 8
number_of_chroms = 50
max_fitness = comb(N, 2)

population = [[randint(1, N) for _ in range(N)]
              for _ in range(number_of_chroms)]


def fitness(chrom: list[int]) -> int:
    score = max_fitness
    for i, j in combinations(range(N), 2):
        if chrom[i] == chrom[j] or abs(i-j) == abs(chrom[i]-chrom[j]):
            score -= 1
    return score
