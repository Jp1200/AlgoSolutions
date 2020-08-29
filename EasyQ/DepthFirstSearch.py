# notes for Depth First Search
# go as deep as possible for each branch
# time/space complexity based on O(v+e ) vertivces plus edges
# edges are the node/vertices connections

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
