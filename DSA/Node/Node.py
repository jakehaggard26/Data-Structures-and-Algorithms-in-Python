from DSA.Node.INode import INode

"""
    A simple Node class that implements the INode interface.
    This class can be used to create nodes for various data structures, such as linked lists, trees, and graphs.
    The Node class is designed to hold a single element and provides methods for getting and setting that element.
    It also includes comparison operators for comparing nodes based on their elements.

    It's purpose is store an element and provide a way to access and modify that element.
"""

class Node(INode):
    def __init__(self, element):
        self._element = element

    def get_element(self):
        return self._element

    def set_element(self, element):
        self._element = element

    def __repr__(self):
        return f"Node({self._element})"

    def __str__(self):
        return str(self._element)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._element == other._element
        return False

    def __ne__(self, other):
        if isinstance(other, Node):
            return self._element != other._element
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return self._element < other._element
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Node):
            return self._element <= other._element
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Node):
            return self._element > other._element
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Node):
            return self._element >= other._element
        return NotImplemented

    def __hash__(self):
        return hash(self._element)