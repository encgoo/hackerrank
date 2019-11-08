# Graph
## Algorithms
### Union and Find

#### Internal Data structure
A list to storage linked parent for nodes. The task here
is to build this list using the given edges.
![union_find](images/Union_find.png)

To do so, two methods are needed normally.
##### Find
Given an edge, we want to if the nodes of both end are in the same 
tree (like node 3 and 5 above). This method takes a node and 
find its root. 
It can be a recursive function or use while loop to find 
parent until it is -1. 

##### Union
This method united two roots. Just change one root to point
to the other. 

By using these two methods, we can build a linked list like
the one above for a tree.

##### Detect cycle
This algorithm can be used to detect cycle.

* Dijkstra

* Prim
* Kruskal
* BFS
* DFS (in-order, pre-order, and post-order)

## Roads and Libraries
Union and Find is used for this one, because all the roads carry the
same cost to repair

## Even Tree
DFS search. 
