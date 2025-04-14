from random import randint, random
from math import comb
from itertools import combinations
from bisect import bisect_left

N = 8
number_of_chroms = 50
max_fitness = comb(N, 2)
max_generations = 1000

population = [[randint(1, N) for _ in range(N)]
              for _ in range(number_of_chroms)]


def fitness(chrom: list[int]) -> int:
    score = max_fitness
    for i, j in combinations(range(N), 2):
        if chrom[i] == chrom[j] or abs(i-j) == abs(chrom[i]-chrom[j]):
            score -= 1
    return score


def crossover(chrom1: list[int], chrom2: list[int]) -> list[int]:
    index = randint(0, N-1)
    return chrom1[:index]+chrom2[index:]


generation = 0
found = False
while not found and generation < max_generations:
    # calculating fitness of every chromosome
    total_fitness = 0
    fitnesses = []
    for chrom in population:
        score = fitness(chrom)
        if score == max_fitness:
            ans = chrom
            found = True
        fitnesses.append(score)
        total_fitness += score

    # calculating probabilty for every chromosome
    probs = [fitness/total_fitness for fitness in fitnesses]

    # calculating cumulative probs
    cumulative_probs = []
    p_sum = 0
    for p in probs:
        p_sum += p
        cumulative_probs.append(p_sum)

    # building new population
    new_poplulation = []
    for _ in range(number_of_chroms):
        # selecting parents
        r1, r2 = random(), random()
        index1 = bisect_left(cumulative_probs, r1)
        index2 = bisect_left(cumulative_probs, r2)

        child = crossover(population[index1], population[index2])
        new_poplulation.append(child)

    population = new_poplulation
    generation += 1

if found:
    # build the board
    board = [[0]*N for _ in range(N)]
    for i in range(N):
        board[ans[i]-1][i] = 1
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
else:
    print('no solution found')
