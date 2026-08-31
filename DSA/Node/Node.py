from DSA.Node.INode import INode

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