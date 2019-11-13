#!/bin/python3

import os
import sys

from collections import deque
def jeanisRoute(k, roads, cities, n):
    # Step 1: Build a minimu sub-tree
    # A sub-tree with minimum number of roads that
    # are needed to connect all the cities jeanis needs to deliver letter to

    # 1.1 translate roads to roads_ for easier/faster consumption
    roads_ = [[] for i in range(n)]
    for r in roads:
        roads_[r[0] - 1].append((r[1] - 1, r[2]))
        roads_[r[1] - 1].append((r[0] - 1, r[2]))
    # 1.2 start a q, and add the first city from cities
    q = deque([cities[0] - 1])
    linked = [-1]*n
    while len(q) > 0:
        node = q.popleft()  # 0 base
        rs = roads_[node]
        for r in rs:
            if linked[node] != r[0]:
                # use node as parent for r[0]
                linked[r[0]] = node
                # append r[0] to q for further process
                q.append(r[0])
    print(linked)
    # 1.2 use linked to figure out which roads to keep. Use a list of node
    # to keep track all the nodes passed by connections betwen any city in
    # cities to root
    connected_node = [False]*n

    assert(len(cities) >= 2)
    for i in range(1, len(cities)):
        end = cities[i] - 1
        # Always keep the first node. It is a city to deliver letter
        while linked[end] != -1 and connected_node[end] is False:
            connected_node[end] = True
            # move up to its parent of the tree
            end = linked[end]
    # Always include the root
    connected_node[cities[0] - 1] = True
    print(connected_node)
    # 1.3 roads with both end in connected_node are the ones to keep.
    # For the example given in the problem, the connection between 3-5 will
    # be dropped because 5 shall not be in connected_node
    roads_keep = [[r for r in roads_[i] if connected_node[i] and connected_node[r[0]]] for i in range(n)]
    print(roads_keep)
    # Step 2. Figure out the longest distance between any two
    # nodes in cities
    end_city, _ = longest_distance(cities[0], roads_keep, n)
    _, longest = longest_distance(end_city, roads_keep, n)

    total_length = sum(sum(r[1] for r in city_roads) for city_roads in roads_keep)

    return total_length - longest

def longest_distance(start, roads_keep, n):
    end_city = start
    longest_distance = 0
    visited = [False]*n
    q = deque([(start, 0)])
    while len(q) > 0:
        node, dis = q.popleft()
        rs = roads_keep[node]
        if dis > longest_distance:
            longest_distance = dis
            end_city = node
        for r in rs:
            if visited[r[0]] is False:
                q.append((r[0], dis + r[1]))
                visited[r[0]] = True

    return end_city, longest_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    city = list(map(int, input().rstrip().split()))

    roads = []

    for _ in range(n-1):
        roads.append(list(map(int, input().rstrip().split())))

    result = jeanisRoute(k, roads, city, n)

    fptr.write(str(result) + '\n')

    fptr.close()
