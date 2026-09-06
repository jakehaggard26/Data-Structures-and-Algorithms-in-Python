from DSA.Node.ILinearNode import ILinearNode
from DSA.Node.Node import Node
# Refer to LinearNode notes in Build Notes for more information on the design of this class.
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