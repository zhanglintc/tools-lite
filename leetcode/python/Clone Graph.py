# 3Sum Closest
# for leetcode problems
# 2014.12.09 by zhanglin

# Problem:
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


# OJ's undirected graph serialization:
# Nodes are labeled uniquely.

# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.

# The graph has a total of three nodes, and therefore contains three parts as separated by #.

# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:

#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# DFS solution
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node

        return self.dfs(node, {})

    def dfs(self, node, visited):
        # visited means copied, only return the copy
        if node in visited:
            return visited[node]

        # not visited before, make a copy, and finally return
        newNode = UndirectedGraphNode(node.label)

        # visited[old node] = its copy
        visited[node] = newNode

        # fill newNode's neighbor list
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.dfs(neighbor, visited))

        return newNode

# BFS solution
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node

        # store node which has already visited
        visited = {}

        # store node whose neighbors need to be visited
        # value would be the copy of the old node
        queue = []

        # make a copy of base node
        newNode = UndirectedGraphNode(node.label)

        # visited[old node]  = its copy
        visited[node] = newNode

        # nodes in this list whose neighbor list need to be traversed
        queue = [node]

        # traverse the queue
        for this in queue:

            # visit all neighbors of this
            for neighbor in this.neighbors:

                # not copied before, make a copy
                if neighbor not in visited:
                    # make a copy
                    clone = UndirectedGraphNode(neighbor.label)

                    # visited[old node]  = its copy
                    visited[neighbor] = clone

                    # fill new node's neighbor list
                    visited[this].neighbors.append(clone)

                    # traverse this neighbor later
                    queue.append(neighbor)

                # already has copy, add the copy to neighbor list
                else:
                    # visited[this] is this new node whose neighbor list need to be filled
                    # visited[neighbor] is a node already has a copy
                    visited[this].neighbors.append(visited[neighbor])

        return newNode


