import unittest
from DSA.Node import Node

class TestNode(unittest.TestCase):
        
    def test_string_representation(self: Node) -> None:
        node = Node("Hello, World!")
        self.assertEqual(node.get_data(), "Hello, World!")
    
    def test_integer_representation(self: Node) -> None:
        node = Node(42)
        self.assertEqual(node.get_data(), 42)
    
    def test_float_representation(self: Node) -> None:
        node = Node(3.14)
        self.assertEqual(node.get_data(), 3.14)
    
    def test_float_representation(self: Node) -> None:
        node = Node(3.14)
        self.assertEqual(node.get_data(), 3.14)
    
    def test_list_representation(self: Node) -> None:
        node = Node([1,2,3,4,5])
        self.assertEqual(node.get_data(), [1,2,3,4,5])
    
    def test_Node_representation(self: Node) -> None:
        node = Node(Node(1))
        self.assertEqual(node.get_data(), Node(1))

    def test_le(self: Node) -> None:
        node1 = Node(1)
        node2 = Node(2)
        self.assertTrue(node1 < node2)
        self.assertFalse(node2 < node1)

    def test_lt(self: Node) -> None:
        node1 = Node(1)
        node2 = Node(2)
        self.assertTrue(node1 <= node2)
        self.assertFalse(node2 <= node1)

    def test_gt(self: Node) -> None:
        node1 = Node(1)
        node2 = Node(2)
        self.assertFalse(node1 > node2)
        self.assertTrue(node2 > node1)

    def test_ge(self: Node) -> None:
        node1 = Node(1)
        node2 = Node(2)
        self.assertFalse(node1 >= node2)
        self.assertTrue(node2 >= node1)



if __name__ == '__main__':
    unittest.main()