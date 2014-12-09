# Simulated Annealing Implementation
import math
import random
from graph_generator import GraphGenerator

NUM_CITIES = 100
DIM_STATE = 70
ITERATIONS = 100000
START_TEMP = 0.7
END_TEMP = 0.01
STAG_FACTOR = 0.05
RAND_MAX = 2**15 - 1


class State:

    def __init__(self):
        self.list = []
        self.fitness = float('inf')


city = []
city.append([])
city.append([])


def crand():
    return random.randint(0, RAND_MAX)


def distance(a, b):
    return math.pow(math.pow(city[a][0] - city[b][0], 2) +
                    math.pow(city[a][1] - city[b][1], 2), 0.5)


def fitness(state):
    sum = distance(state.list[0], state.list[NUM_CITIES - 1])
    for i in xrange(NUM_CITIES):
        sum += distance(state.list[i], state.list[i - 1])
    return sum


def iterate(temp, state):
    _state = state
    pt = crand() % NUM_CITIES
    sh = (pt + (crand() % DIM_STATE) + 1) % NUM_CITIES
    _state.list[pt], _state.list[sh] = _state.list[sh], _state.list[pt]
    _state.fitness = fitness(state)
    if _state.fitness < state.fitness:
        return _state
    elif (float(crand()) / float(RAND_MAX)) < \
            math.exp(-1.0 * (_state.fitness - state.fitness) / temp):
        return _state
    else:
        return state


def main():
    # Generate a graph.
    graph = GraphGenerator(NUM_CITIES).generateGraph()
    graph = graph.toArray()

    # Initialize state
    state, optimum = State(), State()
    n = math.sqrt(NUM_CITIES)
    for i in range(n):
        for j in range(n):
            k = n * i + j
            state.list[k] = k

    # Randomization of state list.
    for i in range(NUM_CITIES * math.log(NUM_CITIES)):
        k = crand() % (NUM_CITIES - 1) + 1
        state.list[0], state.list[k] = state.list[k], state.list[0]

    # Sample state space with 1% of runs to determine temperature schedule.
    minf, maxf = math.pow(10, 10), 0

    for i in range(max(0.01 * NUM_CITIES, 2)):
        state = iterate(math.pow(10, 10), state)
        minf = state.fitness if (state.fitness < minf) else minf
        maxf = state.fitness if (state.fitness > maxf) else maxf

    sep = (maxf - minf) * START_TEMP
    dtemp = math.pow(END_TEMP, 1.0 / ITERATIONS)

    optgen = l = 1
    optimum.fitness = state.fitness

    for i in range(ITERATIONS):
        state.iterate(sep * pow(dtemp, l), state)
        if state.fitness < optimum.fitness:
            optimum = state
            optgen = l

        if l - optgen == STAG_FACTOR * ITERATIONS:
            dtemp = pow(dtemp, 0.05 * l / ITERATIONS)
