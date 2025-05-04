import random

class Chromosome:    
    def __init__(self, genes, knapsack,weight_limit):
        self.genes = list(genes)
        self.weight_limit= weight_limit
        self.knapsack=knapsack
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        fitness = 0
        total_weight = 0
        for gene, (key, item) in zip(self.genes, self.knapsack.items()):
            if gene == 1:
                fitness += item['value']
                total_weight += item['weight']
        if total_weight > self.weight_limit:
            return 0
        return fitness

    def __str__(self):
        return f"Genes: {self.genes}, Fitness: {self.fitness}"


class GeneticAlgorithm:
    def __init__(self, weight_limit, knapsack, population_size, mutation_rate):
        self.weight_limit = weight_limit
        self.knapsack = knapsack
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        #Initialize a population with random gene sequences#

        population = []
        num_items = len(self.knapsack)
        for  _ in range(self.population_size):
            genes= [random.randint(0,1) for _ in range(num_items)]
            chromosome = Chromosome(genes,self.knapsack,self.weight_limit)
            population.append(chromosome)
        return population

    def selection(self):
        #Use elitism and roulette-wheel to select chromosomes#

        selected=[]
        # self.population.sort(key=lambda c: c.fitness, reverse=True)                     
        # selected = self.population[:2]  #  Elitism: Keep the top 2 best chromosomes
        

        total_fitness = sum(c.fitness for c in self.population)
        if total_fitness == 0:
            return random.choices(self.population, k=self.population_size)
        
        
        # Select individuals based on their fitness (roulette wheel)
        for _ in range(self.population_size):
            pick = random.uniform(0, total_fitness)
            current = 0
            for chromosome in self.population:
                current += chromosome.fitness
                if current > pick:
                    selected.append(chromosome)
                    break
        return selected

    def crossover(self, parent1, parent2):
        #Perform single-point crossover to create new offsprings#
        point = random.randint(1, len(parent1.genes) - 2)
        child1_genes = parent1.genes[:point] + parent2.genes[point:]
        child2_genes = parent2.genes[:point] + parent1.genes[point:]
        child1=Chromosome(child1_genes, self.knapsack, self.weight_limit)
        child2=Chromosome(child2_genes, self.knapsack, self.weight_limit)
        return child1, child2

    def mutation(self, chromosome):
        #Mutate genes of a chromosome#
        for i in range(len(chromosome.genes)):
            if random.random() < self.mutation_rate:
                chromosome.genes[i] = 1 - chromosome.genes[i]
        chromosome.fitness = chromosome.calculate_fitness()

    def evolve(self):
        ##Evolve and generate new population#
        new_population = []
        for _ in range(self.population_size // 2):
            selected = self.selection()
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)
            child1, child2 = self.crossover(parent1, parent2)
            self.mutation(child1)
            self.mutation(child2)
            new_population.extend([child1, child2])
            #selection, cross-over, mutation and replacement#
        self.population = new_population

    def get_solution(self):
        #Fetch the best solution on the basis of fitness#
        return max(self.population, key=lambda c: c.calculate_fitness())

def build_knapsack (file):
    w = None 
    knapsack = None
    
    #Read from test case and build knapsack as a dictionary"
    with open(file,"r") as f:
        lines=f.readlines()
        w =int(lines[0].split()[1].strip()) 
        knapsack= {}
        for i, line in enumerate(lines[1:]):
            value, weight = map(int, line.strip().split())
            knapsack[f"item_{i}"] = {'value': value, 'weight': weight}
    return w, knapsack

if __name__ == "__main__":
    w, knapsack = build_knapsack("test.txt")
    ga = GeneticAlgorithm(w, knapsack, population_size=10, mutation_rate=0.2)
    
    for _ in range(50):
        ga.evolve()
    
    best_solution = ga.get_solution()
    print("Best solution found:", best_solution)
    print("Fitness of best solution:", best_solution.calculate_fitness())