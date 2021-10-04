from .DNA import *
from random import random
from math import floor, inf

__all__ = ["Population"]

n_genes = 44 # number of genes on an individual's chromosome

class Population :
  
  def __init__(self, pop_size : int, fitness_function,
               crossover_rate : float, mutation_rate : float) :
    
    assert(callable(fitness_function))
    
    self.pop_size = pop_size
    self.population = self.initial(pop_size) # initializes a population with random individuals
    self.fitness_function = fitness_function
    self.generation = 0
    self.calc_fitness() # calculates initial population aptitude
    self.crossover_rate = crossover_rate # sets the population crossover rate
    self.mutation_rate = mutation_rate # sets the population mutation rate
    
  def initial(self, pop_size : int) -> list:
    return [DNA(n_genes) for i in range(pop_size)]
    
  def get_elite(self) -> DNA:
    # selects the fittest parent to pass to the next generation
    
    best_fitness_val = -inf # worst possible value for best fitness
    best_fitness_index = 0
    
    for i in range(self.pop_size) :
      if self.population[i].fitness > best_fitness_val :
        best_fitness_val = self.population[i].fitness
        best_fitness_index = i

    return self.population[best_fitness_index]
    
  def calc_fitness(self) :
    # calculates the aptitude for each individual in the population
    for i in range(self.pop_size) :
      self.population[i].calc_fitness(self.fitness_function)
  
  def get_total_apt(self) -> float:
  
    total_apt = 0.0

    for indv in self.population :
      total_apt += indv.fitness
  
    return total_apt
  
  def calc_avg_fitness(self) -> float:
    return self.get_total_apt() / self.pop_size
    
  def roulette_wheel_selection(self) -> DNA:
    # implements roulette-based selection
    
     # sum of all aptitudes
    totalapt = self.get_total_apt()
    
    # generates a random number between 0 and totalfit and rounds down
    r = (random() * totalapt) // 1
    
    sumfit = 0
    
    for indv in self.population :
      sumfit += indv.fitness
      if sumfit >= r : break
    
    return indv
  
  def display(self) :
    avgfit = self.calc_avg_fitness()
  
    best_indv = self.get_elite()
  
    print("""\n\x1b[1;36mgeneration:\x1b[0m {}, \x1b[1;36mavg_fitness:\x1b[0m {},
             \r\x1b[1;36mbest_fitness:\x1b[0m \x1b[38;2;255;157;0;1m{}\x1b[0m
             \r\x1b[1;36mbest individual:\x1b[0m {}""".format(
             self.generation, avgfit, best_indv.fitness, best_indv))
          
    print(best_indv.convert_to_real())
  
  def next_generation(self) -> None:
  
    self.generation += 1
    
    childs = [None] * self.pop_size
    
    for i in range(0, self.pop_size - 1, 2) :
      partnerA = self.roulette_wheel_selection() # select the first parent to mate
      partnerB = self.roulette_wheel_selection() # select the second parent to mate
       # crosses the parents and generates two new children
      child1, child2 = partnerA.crossover(partnerB, self.crossover_rate)
      child1.mutate(self.mutation_rate) # mutate (or not) the first child
      child2.mutate(self.mutation_rate) # mutate (or not) the second child
      childs[i], childs[i+1] = child1, child2
    
    childs[-1] = self.get_elite() # keep better father (elitism)
    
    self.population = childs[:] # copy all the children to the new generation
    
    self.calc_fitness()
      
    self.display()
    

