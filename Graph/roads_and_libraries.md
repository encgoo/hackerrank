# Roads and Libraries

There are n cities and m roads. Not all cities are connected 
by roads. All roads are destroyed. 

Need to decide which road the rebuild and where to build 
libraries. Need to fulfil:
* Any city needs to
 have a library or be connected to a city with a library
 
# Approach
 Use Union and Find algorithm, because it can
 detect connected cities. 
 
 Assume that cities are grouped into clusters.
 
 Union and Find algorithm uses a list to store 
 connected nodes. 
 On top of that, use a list of clusters to store number 
 of roads and cities in each cluster, together with the
 root city.
 
In the union method, also merge two clusters.


 
