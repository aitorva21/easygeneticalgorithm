import numpy as np

import Genetics
import string
from matplotlib import pyplot as plt

        
def main():
    #Parameters to use
    gen_set = string.letters + string.punctuation + " " + string.digits        
    target = "Don't worry, be happy"    
    max_pop = 500
    mutation = 0.01
    
    #Generating the population
    population = Genetics.Population(target, max_pop, gen_set, mutation)
    
    generations = np.array([])
    generation = 1
    while population.evaluate():
        population.calculate_fitness()        
        population.next_generation()        
        generations = np.append(generations,np.array([population.avg_fitness]))

        print "Generation --> ", generation
        print "Average fitness --> ", "%.2f" % population.avg_fitness + "%"
        print "Gens status--> ", ''.join(map(lambda x: chr(int(x)),
                                         population.pop[population.biggest].gens))
        generation+=1
    
    plt.plot(range(generations.shape[0]), generations)
    plt.xlabel("Generation number")
    plt.ylabel("Average fitness")
    plt.title("Learning graph")
    plt.grid()
    plt.show()
    
    print "Final generation --> ", generation
    print "gens -->  ", ''.join(map(lambda x: chr(int(x)),
                                     population.pop[population.biggest].gens))

if __name__ == '__main__':
    main()
