# Graph
## 1. Algorithms
### 1.1 Union and Find

#### 1.1.1 Internal Data structure
A list to storage linked parent for nodes. The task here
is to build this list using the given edges.
![union_find](images/Union_find.png)

To do so, two methods are needed normally.
##### 1.1.2 Find
Given an edge, we want to if the nodes of both end are in the same 
tree (like node 3 and 5 above). This method takes a node and 
find its root. 
It can be a recursive function or use while loop to find 
parent until it is sys.maxsize. 

##### 1.1.3 Union
This method united two roots. Just change one root to point
to the other. 

By using these two methods, we can build a linked list like
the one above for a tree.

##### 1.1.4 Detect cycle
This algorithm can be used to detect cycle, or to filter out
cycle(s), as shown in the example (Roads and Libraries) below.

### 1.2 Dijkstra
#### 1.2.1 Internal Data Structure
Two lists, each of size of nodes.
First list (visited) store information whether a node has been visited. 

The second list (min_dis) stores the minimum distance (so far) to the start node. Initialize even thing to -1.

#### 1.2.2 Useful method
Find the node with the minimum dis to start, provided it is 
not visited. 

#### 1.2.3 How it works
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

### 1.3 Prim
Prim is used to find the MST. It is similar to Dijkstra, and the difference is 
that Dijkstra is the min sum of distance from one node to all the others.
Prim is the min sum of all edges.

So when we need to update the mis_dis, instead of using the distance trough node_s tp node_e
we just use the distance between node_s and node_e.
![Prim](images/prim.png)


### 1.4 Kruskal
Kruskal is a variance of Union and Find. In Union and Find, we don't care about the order of 
edges. We just need to hanle all edges.

For Kruskal, now we handle edges with weight. So we first sort the edges according to the
weight, and then we handle them from low to high.


Kruskal can do the same thing as Prim.
![Kruskal](images/kruskal.png)

### 1.5 BFS
Use a queue to do BFS.

Steps:
* Initialize the deque with root node
* do a while loop for non-empty deque
* for each iteration, get the size of the deque. 
* loop through this size
* for each iteration, pop a node from deque. 
* do whatever we need to do with this node.
* push its children to the deque.

### 1.6 DFS (in-order, pre-order, and post-order)
Use recursive approach. Have a recursive method to handle a node.

* in-order: call itself to handle the left child, then process its data, then call itself to handle the right child
* pre-order: process its data first, then call itself to handle left child, call itself to handle the right child
* post-order: call itself to handle the left, then right child. Then process its data.

## 2. Examples
### 2.1 Roads and Libraries
Union and Find is used for this [problem](https://www.hackerrank.com/challenges/torque-and-development/problem), because all the roads carry the
same cost to repair.

There are n cities and m roads. Not all cities are connected 
by roads. All roads are destroyed. 

Need to decide which road the rebuild and where to build 
libraries. Need to fulfil:
* Any city needs to
 have a library or be connected to a city with a library
 
#### 2.1.1 Approach
 Use Union and Find algorithm, because it can
 detect connected cities. 
 
 Assume that cities are grouped into clusters.
 
#### 2.1.2 Implementation
Union and Find algorithm uses a list to store 
 connected nodes. 
 On top of that, use a list of clusters to store number 
 of roads and cities in each cluster, together with the
 root city.
 
In the union method, also merge two clusters.

### 2.2 Even Tree
DFS search. 
