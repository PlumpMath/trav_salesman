# Simulated Annealing Implementation
import math
import random
import time

# Global values:
MAX_ITERATIONS = 50000
START_TEMP = 10
ALPHA = 0.9999
    
graph = {
    'A': {'C': 82, 'B': 85, 'E': 73, 'D': 18, 'G': 67, 'F': 15, 'I': 65, 'H': 62, 'J': 20},
    'C': {'A': 82, 'B': 80, 'E': 97, 'D': 16, 'G': 66, 'F': 20, 'I': 96, 'H': 17, 'J': 58},
    'B': {'A': 85, 'C': 80, 'E': 86, 'D': 56, 'G': 70, 'F': 49, 'I': 89, 'H': 99, 'J': 81},
    'E': {'A': 73, 'C': 97, 'B': 86, 'D': 16, 'G': 33, 'F': 86, 'I': 60, 'H': 96, 'J': 62},
    'D': {'A': 18, 'C': 16, 'B': 56, 'E': 16, 'G': 47, 'F': 15, 'I': 51, 'H': 14, 'J': 42},
    'G': {'A': 67, 'C': 66, 'B': 70, 'E': 33, 'D': 47, 'F': 45, 'I': 95, 'H': 54, 'J': 17},
    'F': {'A': 15, 'C': 20, 'B': 49, 'E': 86, 'D': 15, 'G': 45, 'I': 61, 'H': 77, 'J': 65},
    'I': {'A': 65, 'C': 96, 'B': 89, 'E': 60, 'D': 51, 'G': 95, 'F': 61, 'H': 16, 'J': 83},
    'H': {'A': 62, 'C': 17, 'B': 99, 'E': 96, 'D': 14, 'G': 54, 'F': 77, 'I': 16, 'J': 43},
    'J': {'A': 20, 'C': 58, 'B': 81, 'E': 62, 'D': 42, 'G': 17, 'F': 65, 'I': 83, 'H': 43}
}

def progress(prev_fitness, next_fitness, temperature):
    if next_fitness > prev_fitness:
        return 1.0
    else:
        return math.exp(-abs(next_fitness - prev_fitness) / temperature)

class ObjectiveFunction:

    def __init__(self, objective_function):
        self.objective_function = objective_function
        self.best = None
        self.best_fitness = None

    def __call__(self, solution):
        fitness = self.objective_function(solution)
        if self.best is None or fitness > self.best_fitness:
            self.best_fitness = fitness
            self.best = solution
        return fitness

def cool(start_temp, alpha):
    temp = start_temp
    while True:
        yield temp
        temp *= alpha

def anneal(init_function, move_operator, objective_function, max_iterations,
        start_temp, alpha):
    objective_function = ObjectiveFunction(objective_function)

    current_move = init_function()
    current_score = objective_function(current_move)
    num_iterations = 1

    cooling_schedule = cool(start_temp, alpha)

    for temperature in cooling_schedule:
        done = False
        for next_move in move_operator(current_move):
            if num_iterations >= max_iterations:
                done = True
                break

            next_score = objective_function(next_move)
            num_iterations += 1
            p = progress(current_score, next_score, temperature)
            if random.random() < p:
                current = next_move
                current_score = next_score
        if done: break

    best_fitness = objective_function.best_fitness
    best = objective_function.best
    return (num_iterations, best_fitness, best)

def random_tour():
    tour = graph.keys()
    random.shuffle(tour)
    return tour

def rand_seq():
    values = range(len(graph.keys()))
    size = len(values)
    for i in xrange(size):
        j = i + int(random.random() * (size - i))
        values[i], values[j] = values[j], values[i]
        yield values[i]

def all_pairs():
    for i in rand_seq():
        for j in rand_seq():
            yield (i, j)

def reversed_sections(tour):
    for i, j in all_pairs():
        if i != j:
            copy = tour[:]
            if i < j:
                copy[i:j+1] = reversed(tour[i:j+1])
            else:
                copy[i+1:] = reversed(tour[:j])
                copy[:j] = reversed(tour[i+1:])
            if copy != tour:
                yield copy

def tour_length(matrix, tour):
    total = 0
    num_cities = len(tour)
    for i in xrange(num_cities):
        j = (i + 1) % num_cities
        city_i = tour[i]
        city_j = tour[j]
        total += matrix[city_i][city_j]
    return total

def main():
    startTime = time.time()

    obj_func = lambda tour: tour_length(graph, tour)

    print "Running simulated annealing with a max of 10000 iterations."
    iterations, best_fitness, best_path = anneal(random_tour, reversed_sections,\
            obj_func, MAX_ITERATIONS, START_TEMP, ALPHA)

    endTime = time.time()

    print "Optimal path is " +  str(best_path) + " and took " + str(iterations)
    print " iterations to calculate and had a fitness of " + str(best_fitness) + "."
    print "Took " + str(endTime - startTime) + " seconds."

if __name__ == "__main__":
    main()
