import math
import random
from faker import Factory


class GraphGenerator:
    '''
    This class generates a graph representing cities for the travelling
    salesman problem. Given a number of cities, this class can generate a
    graph with that number of cities and a number of randomly assigned
    edges.
    '''

    def __init__(self, num):
        self.num = num
        self.graph = {}

    def __str__(self):
        output = ""
        for k, v in self.graph.iteritems():
            output += str(k) + ": " + str(v) + "\n"
        return output

    def generateGraph(self):
        '''
        Generates a graph with random city names and distances.
        The number of edges is the number of cities raised to to 3/2.
        Note: this generates an undirected graph.
        '''
        faker = Factory.create()

        for i in range(self.num):
            # Generate random city name.
            randomCityName = faker.city()
            self.graph[randomCityName] = {}

        # Pick a random city, add an edge of random length to another city.
        for i in range(int(math.ceil(self.num ** 1.5))):
            source = random.choice(list(self.graph.iterkeys()))
            dest = random.choice(list(self.graph.iterkeys()))
            if source == dest:
                pass
            else:
                distance = random.randrange(10, 100)
                self.graph[source][dest] = distance
                self.graph[dest][source] = distance

        return self.graph


def main():
    graph = GraphGenerator(10)
    graph.generateGraph()
    print graph

if __name__ == "__main__":
    main()
