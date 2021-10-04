from random import random, randint

__all__ = ["DNA"]

# range constraint for the function being optimized
min_i, max_i = -100, +100
k_i = 22 # number of bits for the ​​x and y variables of this problem

# a chromosome is represented by 44 binary digits, with 22 for x and 22 for y
# the convert_to_real method retrieves the variable representation as a real number

# the objective here is to maximize the fitness_function, 
# so the higher the value for x and y in the function, the greater its fitness.

def random_binary() -> str:
  # generate a random binary digit and convert it to character
  return chr(randint(0, 1) + 48)

class DNA:
  
  def __init__(self, n_genes : int = 0) :
    self.chromosome = [random_binary() for i in range(n_genes)]
    self.fitness = 0.0
  
  def __str__(self) :
    return "".join(self.chromosome)
  
  def convert_to_real(self) -> tuple:
  
    midpoint = len(self.chromosome) // 2
    x = self.chromosome[:midpoint]
    y = self.chromosome[midpoint:]
    
    # convert from binary to decimal
    cx = int("".join(x), 2)
    cy = int("".join(y), 2)
  
    # x_ireal = x_ibin * (max_i - min_i) / (2**k_i - 1) + min_i
    precision = (max_i - min_i) / (2 ** k_i - 1)
    rx = cx * precision + min_i
    ry = cy * precision + min_i
    
    return rx, ry
  
  def calc_fitness(self, f) -> float:
    # calculates this individual's aptitude/fitness
    x, y = self.convert_to_real()
    score = f(x, y)
    self.fitness = score
    return score
  
  def crossover(self, partner, crossover_rate : float) -> tuple:
    # both children without genetic information at the beginning
    child1 = DNA()
    child2 = DNA()
    
    # set random cutoff
    cutpoint = randint(0, len(self.chromosome) - 1)
    
    # test true -> crossover
    # test false -> copy the parents
    if random() < crossover_rate :
      # swap parents' tails
      child1.chromosome = self.chromosome[:cutpoint] + partner.chromosome[cutpoint:]
      child2.chromosome = partner.chromosome[:cutpoint] + self.chromosome[cutpoint:]
    else :
      # copy genes from parents to children
      child1.chromosome = self.chromosome[:]
      child2.chromosome = partner.chromosome[:]
    
    return child1, child2
    
  def mutate(self, mutation_rate : float) :
  
    for i in range(len(self.chromosome)) :
      if random() < mutation_rate :
        # self.chromosome[i] = '0' if ord(self.chromosome[i]) % 48 else '1'
        self.chromosome[i] = '1' if self.chromosome[i] == '0' else '0'
        

