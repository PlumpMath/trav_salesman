'''
	CMSC Project 3
	Michael Neary & Jeremy Neal
	Traveling Salesman Problem
'''
import time

'''
undirected graph is implemented as a python dictionary of dictionaries
inner dictionary are vertices the key is connected to and associated weights
no self-edges allowed
'''

graph = {
		'A' : {'B': 86 , 'C': 178, 'D': 195},
	        'B' : {'A': 86 , 'C': 123, 'D': 107, 'E': 171},
	        'C' : {'A': 178, 'B': 123, 'E': 170},
	        'D' : {'A': 195, 'B': 107, 'E': 210, 'F': 210, 'G': 135, 'H': 64},
	        'E' : {'B': 171, 'C': 170, 'D': 210,'G': 230, 'F': 230},
	        'F' : {'D': 210, 'E': 230, 'G': 85},
	        'G' : {'D': 135, 'E': 230, 'F': 85 ,'H': 67},
	        'H' : {'D': 64 , 'G': 67},
	}

# recursive brute force solution to the TSP
def find_all_paths(graph, currentNode, distanceSoFar, pathSoFar):

	# add the current node to the path so pathSoFar
	pathSoFar.append(currentNode)

	# calculate the distance from end of path so far to the current node
	if len(pathSoFar) > 1:
		distanceSoFar += graph[pathSoFar[-2]][currentNode]

	# check if complete path can be made and all nodes exhausted
	if graph[pathSoFar[-1]].has_key(pathSoFar[0]) and len(pathSoFar) == len(graph):
		
		pathSoFar.append(pathSoFar[0])

		# add distance from last node to start node, and add start node to end of path
		distanceSoFar += graph[pathSoFar[-2]][pathSoFar[0]]

		global bruteForcePaths

		# bruteForcePaths.append((pathSoFar, distanceSoFar))
		bruteForcePaths.append((distanceSoFar, pathSoFar))
		
                return

	# for each node left in the graph, find another path
	# in other words, find all permutations of paths
	for node in graph:

		# check if an edge exists between currentNode and node 
		if graph[node].has_key(currentNode):

			# make sure that you haven't already visited that node
			if node not in pathSoFar:

				# find all paths from this node
				# casting is necessary because things are passed by reference in python
				# and for the recursion to work you need a new copy of the path 
				find_all_paths(graph, node, distanceSoFar, list(pathSoFar))


startTime = time.time()
bruteForcePaths = []
find_all_paths(graph, 'B', 0, [])
endTime = time.time()
print "Done in:", endTime - startTime, "seconds."
bruteForcePaths.sort()
for path in bruteForcePaths:
	print path

	
