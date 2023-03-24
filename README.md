# Lab 7 : Graphs

In this Lab, we will implement several basic graph operations and use them to analyse a social network. 

The files provided are the following:

 -  `graph.py` : This file defines the class `Graph`. We will be representing the graph as a dictionary where each node is the key and the neighbors are the values.
 - `friendship.csv` : Each line of this table represents a link of friendship between `Person1` and `Person2`
 
## Questions:
 
 1. Some of the methods in `graph.py` are not implemented ( There is `pass` written and the comment `# To be implemented`). Implement them.
 
 2.  Using the class `Graph` and the methods you have implemented, create an instance `graph_frendship` that represents the friendship links in the file `friendship.csv`. 

3. Implement a function `nfriends_in_common` that takes as an input the names of two people and return the number of friends in common. Test your function with the inputs **Charles Gomez** and **Leslie Carr**, the output should be 2. 

4. Implement a function `get_connection` that takes as an input two names and returns a path that links the two people (it doesn't have to be the shortest) . If there is no such path, return an empty list. 





