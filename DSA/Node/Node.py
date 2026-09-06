from DSA.Node.INode import INode

"""
    A simple Node class that implements the INode interface.
    This class can be used to create nodes for various data structures, such as linked lists, trees, and graphs.
    The Node class is designed to hold a single piece of data and provides methods for getting and setting that data.
    It also includes comparison operators for comparing nodes based on their data.

    It's purpose is store data and provide a way to access and modify that data. 
"""

class Node(INode):
    def __init__(self, data):
        self._data = data

    def get_data(self):
        return self._data  

    def set_data(self, data):
        self._data = data

    def __repr__(self):
        return f"Node({self._data})"

    def __str__(self):
        return str(self._data)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._data == other._data
        return False

    def __ne__(self, other):
        if isinstance(other, Node):
            return self._data != other._data
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return self._data < other._data
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Node):
            return self._data <= other._data
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Node):
            return self._data > other._data
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Node):
            return self._data >= other._data
        return NotImplemented

    def __hash__(self):
        return hash(self._data)