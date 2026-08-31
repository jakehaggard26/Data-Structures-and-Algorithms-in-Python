from DSA.Node import Node

# Example usage of the Node class using integers
node1 = Node(42)
print(node1.get_data())  # Output: 42
print(type(node1.get_data()))  # Output: <class 'int'>   

node2 = Node(4)

print(f"Node 1 ({node1.get_data()}) is less than Node 2 ({node2.get_data()}): {node1 < node2}")  # Output: False
print(f"Node 1 ({node1.get_data()}) is greater than Node 2 ({node2.get_data()}): {node1 > node2}")  # Output: True

print(node1.__repr__())  # Output: Node(42)


# Example usage of the Node class using strings
node1 = Node("abc")
print(node1.get_data())  # Output: abc
print(type(node1.get_data()))  # Output: <class 'str'>   

node2 = Node("xyz")

print(f"Node 1 ({node1.get_data()}) is less than Node 2 ({node2.get_data()}): {node1 < node2}")  # Output: True
print(f"Node 1 ({node1.get_data()}) is greater than Node 2 ({node2.get_data()}): {node1 > node2}")  # Output: False

print(node1.__repr__())  # Output: Node(abc)