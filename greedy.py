'''
Greedy Algorithm to solve the TSP
'''

import time
import graph_generator

def greedy_find_path(graph, start):

	path = [start]

	unvisited = dict(graph)
	i = 0
	sum = 0
	while i < len(graph):
		nearest,cost = closest(unvisited[path[-1]],path[-1], path)
		if cost != float('inf'):
			sum += cost

		#print unvisited
		#print unvisited[path[-1]]
		#print nearest

		path.append(nearest)
		del unvisited[path[-2]]
		i += 1

	path.remove('')
	sum += graph[path[-1]][start]
	path.append(start)
	#print graph.graph
	#print path, sum 
	return path,sum

def closest(graph, node, path):
	minCost = float('inf')
	minNode = ''

	for k,v in graph.iteritems():
		if v < minCost and k != node and k not in path:
			minCost = v
			minNode = k

	return minNode, minCost

def main():

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

	#graph = graph_generator.GraphGenerator()
	#graph.generateGraph()
	start = time.time()
	path,cost = greedy_find_path(graph,'I')
	end = time.time()
	print "Done in:",end-start,"seconds."
	print "The path taken:", path
	print "It cost:",cost

if __name__ == "__main__":
	main()