from random import randint


N = 8
number_of_genoms = 50

population = [[randint(1, N) for _ in range(N)]
              for _ in range(number_of_genoms)]
