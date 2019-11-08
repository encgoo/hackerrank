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
parent until it is sys.maxsize. 

##### Union
This method united two roots. Just change one root to point
to the other. 

By using these two methods, we can build a linked list like
the one above for a tree.

##### Detect cycle
This algorithm can be used to detect cycle, or to filter out
cycle(s), as shown in the example (Roads and Libraries) below.

### Dijkstra
#### Internal Data Structure
Two lists, each of size of nodes.
First list (visited) store information whether a node has been visited. 

The second list (min_dis) stores the minimum distance (so far) to the start node. Initialize even thing to -1.

#### Useful method
Find the node with the minimum dis to start, provided it is 
not visited. 

#### How it works
First pick a start node (or use the given one).
![Dijkstr](images/Dijkstra.png)
Initialize min_dis by setting the dis of this start node to be 0. This means this node is 0 from start. 

Start a loop for n iteration, with n being the number of node.

For each iteration, call the above method to get the min node (node_s).
Set visited of node_s to True.
For the first iteration, the start node is the only one there.
Find all the edges that contains this node as start 
(and end if bidirection). 
Update the min_dis list for the nodes (node_e) of these edges.
Note update only when the distance to node_e through node_s is
smaller than the current value of node_e in min_dis.

This can be used to find the Minimum Span Tree.

* Prim
* Kruskal
* BFS
* DFS (in-order, pre-order, and post-order)

## Roads and Libraries
Union and Find is used for this one, because all the roads carry the
same cost to repair

## Even Tree
DFS search. 
