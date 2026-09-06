import unittest

from DSA.Node.ILinearNode import ILinearNode
from DSA.Node.LinearNode import LinearNode
from DSA.Node.Node import Node


class TestLinearNode(unittest.TestCase):

    def test_element_representation(self):
        node = LinearNode(42)

        self.assertEqual(node.get_element(), 42)

    def test_set_element(self):
        node = LinearNode(1)

        node.set_element(2)

        self.assertEqual(node.get_element(), 2)

    def test_next_defaults_to_none(self):
        node = LinearNode("first")

        self.assertIsNone(node.get_next())

    def test_next_can_be_set_in_constructor(self):
        next_node = LinearNode("second")
        node = LinearNode("first", next_node)

        self.assertIs(node.get_next(), next_node)

    def test_set_next(self):
        node = LinearNode("first")
        next_node = LinearNode("second")

        node.set_next(next_node)

        self.assertIs(node.get_next(), next_node)

    def test_nodes_can_form_a_chain(self):
        first = LinearNode(1)
        second = LinearNode(2)
        third = LinearNode(3)

        first.set_next(second)
        second.set_next(third)

        self.assertIs(first.get_next(), second)
        self.assertIs(first.get_next().get_next(), third)
        self.assertIsNone(third.get_next())

    def test_inherits_from_node(self):
        node = LinearNode(42)

        self.assertIsInstance(node, Node)

    def test_implements_linear_node_interface(self):
        node = LinearNode(42)

        self.assertIsInstance(node, ILinearNode)

    def test_inherited_string_representation(self):
        node = LinearNode(42)

        self.assertEqual(str(node), "42")
        self.assertEqual(repr(node), "Node(42)")

    def test_inherited_equality(self):
        self.assertEqual(LinearNode(1), LinearNode(1))
        self.assertNotEqual(LinearNode(1), LinearNode(2))


if __name__ == "__main__":
    unittest.main()
