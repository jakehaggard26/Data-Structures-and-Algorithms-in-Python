class Node(INode):
    def __init__(self, data):
        self._data = data

    def get_data(self):
        return self._data  

    def set_data(self, data):
        self._data = data