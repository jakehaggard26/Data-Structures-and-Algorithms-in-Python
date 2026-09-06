
# Refer to LinearNode notes in Build Notes for more information on the design of this class.
 
from DSA.Node.ILinearNode import ILinearNode
from DSA.Node.Node import Node

"""
    A simple LinearNode class that inherits from the Node class and implements the ILinearNode interface.
    This class can be used to create nodes for linear data structures, such as linked lists or Stacks and Queues.
    The LinearNode class is designed to hold a single piece of data and a reference to the
    next node in the structure. It provides methods for getting and setting the data and the next node.
"""

class LinearNode(Node, ILinearNode):

    def __init__(self, data, next=None):
        super().__init__(data)
        self._next = next

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node