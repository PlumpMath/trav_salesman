'''
CMSC 471 Project 3
Michael Neary & Jeremy Neal
Traveling Salesman Problem
'''
import time
# from graph_generator import GraphGenerator
import random

'''
undirected graph is implemented as a python dictionary of dictionaries
inner dictionary are vertices the key is connected to and associated weights
no self-edges allowed
'''

# graph = {
#     'A': {'B': 86, 'C': 178, 'D': 195},
#     'B': {'A': 86, 'C': 123, 'D': 107, 'E': 171},
#     'C': {'A': 178, 'B': 123, 'E': 170},
#     'D': {'A': 195, 'B': 107, 'E': 210, 'F': 210, 'G': 135, 'H': 64},
#     'E': {'B': 171, 'C': 170, 'D': 210, 'G': 230, 'F': 230},
#     'F': {'D': 210, 'E': 230, 'G': 85},
#     'G': {'D': 135, 'E': 230, 'F': 85, 'H': 67},
#     'H': {'D': 64, 'G': 67}
# }

'''
graph = {
    u'East Ricki': {u'Kossbury': 55, u'West Laverneland': 26},
    u'South Jaylene': {u'Lonnaborough': 93, u'Lake Brody': 96, u'South Katherin': 44},
    u'West Deenahaven': {u'North Kerrie': 60, u'West Laverneland': 95, u'Rociomouth': 47},
    u'Kossbury': {u'West Laverneland': 70, u'North Kerrie': 40, u'South Katherin': 43, u'East Ricki': 55, u'Rociomouth': 76},
    u'North Kerrie': {u'Kossbury': 40, u'West Deenahaven': 60, u'South Katherin': 57},
    u'South Katherin': {u'Kossbury': 43, u'North Kerrie': 57, u'South Jaylene': 44, u'Lake Brody': 61, u'West Laverneland': 26},
    u'Lonnaborough': {u'Lake Brody': 74, u'South Jaylene': 93, u'West Laverneland': 96, u'Rociomouth': 74},
    u'West Laverneland': {u'West Deenahaven': 95, u'Kossbury': 70, u'East Ricki': 26, u'Lonnaborough': 96, u'Lake Brody': 76, u'South Katherin': 26},
    u'Lake Brody': {u'Lonnaborough': 74, u'West Laverneland': 76, u'South Jaylene': 96, u'South Katherin': 61},
    u'Rociomouth': {u'Kossbury': 76, u'Lonnaborough': 74, u'West Deenahaven': 47}
}
'''

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

# recursive brute force solution to the TSP


def find_all_paths(graph, currentNode, distanceSoFar, pathSoFar):
    # add the current node to the path so pathSoFar
    pathSoFar.append(currentNode)

    # calculate the distance from end of path so far to the current node
    if len(pathSoFar) > 1:
        distanceSoFar += graph[pathSoFar[-2]][currentNode]

    # check if complete path can be made and all nodes exhausted
    if pathSoFar[0] in graph[pathSoFar[-1]] and len(pathSoFar) == len(graph):
        pathSoFar.append(pathSoFar[0])

        # add distance from last node to start node, and add start node
        # to end of path
        distanceSoFar += graph[pathSoFar[-2]][pathSoFar[0]]

        global bruteForcePaths

        # bruteForcePaths.append((pathSoFar, distanceSoFar))
        bruteForcePaths.append((distanceSoFar, pathSoFar))
        return

    # for each node left in the graph, find another path
    # in other words, find all permutations of paths
    for node in graph:

        # check if an edge exists between currentNode and node
        if currentNode in graph[node]:

            # make sure that you haven't already visited that node
            if node not in pathSoFar:

                # find all paths from this node
                # casting is necessary because things are passed by reference
                # in python and for the recursion to work you need a new copy
                # of the path
                find_all_paths(graph, node, distanceSoFar, list(pathSoFar))

# graph = GraphGenerator(10).generateGraph()
startTime = time.time()
bruteForcePaths = []
startNode = random.choice(list(graph.iterkeys()))
print "Starting from", startNode
find_all_paths(graph, startNode, 0, [])
# find_all_paths(graph, 'B', 0, [])
endTime = time.time()
print "Done in:", endTime - startTime, "seconds."
bruteForcePaths.sort()
print "path:",bruteForcePaths[0][1]
print "cost:",bruteForcePaths[0][0]

#for path in bruteForcePaths:
#    print path
