import math
import random
import sys


class GraphGenerator:
    '''
    This class generates a graph representing cities for the travelling
    salesman problem. Given a number of cities, this class can generate a
    graph with that number of cities and a number of randomly assigned
    edges.
    '''

    def __init__(self, num=10):
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

        for i in xrange(self.num):
            # Generate random city name.
            name_len = (i / 26) + 1
            name = ""
            for j in range(name_len):
                name += chr(65 + i % 26)
                i -= 26
            self.graph[name] = {}

        # Pick a random city, add an edge of random length to another city.
        #for i in range(int(math.ceil(self.num ** 1.5))):
        keys = list(self.graph.iterkeys())

        for j in xrange(self.num):

            source = keys[j]

            for i in xrange(self.num):

                dest = keys[i]

                if source != dest:

                    distance = random.randrange(10, 100)
                    self.graph[source][dest] = distance
                    self.graph[dest][source] = distance

        return self.graph


def main():

    # see if size was given on command line
    # and initialize graph object
    if len(sys.argv) >= 2:
        size = int(sys.argv[1])
        graph = GraphGenerator(size)
    else:
        graph = GraphGenerator()

    #generate graph
    graph.generateGraph()
    print graph

if __name__ == "__main__":
    main()
