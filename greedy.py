'''
Greedy Algorithm to solve the TSP
'''

import graph_generator

def greedy_find_path(graph, start):

	path = [start]

	unvisited = dict(graph.graph)
	i = 0
	sum = 0
	while i < graph.num:
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
	sum += graph.graph[path[-1]][start]
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
	graph = graph_generator.GraphGenerator()
	graph.generateGraph()
	path,cost = greedy_find_path(graph,'A')
	print "The path taken:", path
	print "It cost:",cost

if __name__ == "__main__":
	main()