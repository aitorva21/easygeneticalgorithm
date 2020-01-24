import numpy as np

import random


class DNA(object):
    gens = np.array([])
    fitness = 0
    def __init__(self, size, gen_set):
        """Randomly generate an array of characters"""
        self.gens = np.array(random.sample(gen_set, size))
        
    def mutate(self, parent_a, parent_b, gen_set, mutation_rate):
        """Merge with 2 parents"""
        new_gens = np.zeros(parent_a.gens.shape[0])
        mid_point = random.randint(0, parent_a.gens.shape[0])
        for ix in range(len(self.gens)):
            if random.random() < mutation_rate:
                new_gens[ix] = random.sample(gen_set, 1)[0]
            else:
                new_gens[ix] = parent_a.gens[ix] if ix < mid_point \
                                                else parent_b.gens[ix]
                
        self.gens = new_gens
            
class Population(object):
    pop = np.array([])
    def __init__(self, target, max_pop, gen_set, mutation):
        self.gen_set = np.array(map(lambda x: ord(x), gen_set))
        self.target = np.array(map(lambda x: ord(x), target))        
        self.max_pop = max_pop
        self.biggest = 0
        self.avg_fitness = 0
        self.mutation_rate = mutation
        
        #random population creation
        while self.pop.shape[0] < max_pop:
            self.pop = np.append(self.pop, DNA(self.target.shape[0], self.gen_set))
            
    def calculate_fitness(self):
        """Calculate the fitness score"""
        self.biggest = 0
        self.second = 0
        self.avg_fitness = 0
        for ix in range(self.pop.shape[0]):
            # Sum of the correct letters --> fitness score
            self.pop[ix].fitness = (self.pop[ix].gens == self.target).sum()
            self.avg_fitness+= float(self.pop[ix].fitness) / self.target.shape[0]            
            # Save the 2 betters fitness for reproduction
            if self.pop[ix].fitness > self.pop[self.biggest].fitness:
                self.biggest = ix
            elif self.pop[ix].fitness > self.pop[self.second].fitness:
                self.second = ix
        #Calculate average fitness
        self.avg_fitness = (self.avg_fitness / self.pop.shape[0]) * 100.0
                
    def next_generation(self):
        """Next generation with the 2 best gens"""        
        #Get parents gens
        parent_a =  self.pop[self.biggest]
        parent_b =  self.pop[self.second]
        for ix in range(self.pop.shape[0]):
            child = DNA(parent_a.gens.shape[0], self.gen_set)
            # Mutate
            child.mutate(parent_a, parent_b, self.gen_set, self.mutation_rate)
            self.pop[ix] = child
            
    def __str__(self):
        """ Print all population"""
        st= ""
        for i in self.pop:
            st += ''.join([chr(int(el)) for el in i.gens]) + "\n"
        return st
    
    def evaluate(self):
        """Return True if not target is reached"""
        return not (self.pop[self.biggest].gens == self.target).all()
