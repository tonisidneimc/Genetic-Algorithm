from math import sin, sqrt

from Population import *

pop_size=100 
crossover_rate=0.65
mutation_rate=0.08
num_ger=4000

if __name__ == "__main__" :
  
  def f6(x, y : float) -> float:
  
    d1 = sin(sqrt(x**2 + y**2)) ** 2 - .5
    d2 = (1. + .001 * (x**2 + y**2)) ** 2
  
    return .5 - d1 / d2 

  # create population to evolve
  pop = Population(pop_size, f6, crossover_rate, mutation_rate)

  try :
    i = 0
    while i < num_ger:
      pop.next_generation()
      i += 1
      
  except KeyboardInterrupt :
    pass    
        
  
  
