import unittest

from DSA.Node.LinearNode import LinearNode
from DSA.Stack.Stack import Stack


class TestStack(unittest.TestCase):

    def test_new_stack_is_empty(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

    def test_push_adds_node(self):
        stack = Stack()
        node = LinearNode("first")

        stack.push(node)

        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 1)
        self.assertIs(stack.peek(), node)

    def test_push_places_new_node_on_top(self):
        stack = Stack()
        first_node = LinearNode("first")
        second_node = LinearNode("second")

        stack.push(first_node)
        stack.push(second_node)

        self.assertIs(stack.peek(), second_node)
        self.assertIs(second_node.get_next(), first_node)
        self.assertEqual(stack.size(), 2)

    def test_pop_returns_nodes_in_last_in_first_out_order(self):
        stack = Stack()
        first_node = LinearNode("first")
        second_node = LinearNode("second")

        stack.push(first_node)
        stack.push(second_node)

        self.assertIs(stack.pop(), second_node)
        self.assertIs(stack.pop(), first_node)

    def test_pop_decreases_size(self):
        stack = Stack()
        stack.push(LinearNode("first"))
        stack.push(LinearNode("second"))

        stack.pop()

        self.assertEqual(stack.size(), 1)
        self.assertFalse(stack.is_empty())

        stack.pop()

        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.is_empty())

    def test_peek_returns_top_without_removing_it(self):
        stack = Stack()
        node = LinearNode("top")
        stack.push(node)

        peeked_node = stack.peek()

        self.assertIs(peeked_node, node)
        self.assertEqual(stack.size(), 1)
        self.assertFalse(stack.is_empty())

    def test_to_string_for_empty_stack(self):
        stack = Stack()

        self.assertEqual(stack.to_string(), "Stack(top -> bottom): ")

    def test_to_string_shows_elements_from_top_to_bottom(self):
        stack = Stack()
        stack.push(LinearNode(1))
        stack.push(LinearNode(2))
        stack.push(LinearNode(3))

        self.assertEqual(stack.to_string(), "Stack(top -> bottom): 3 -> 2 -> 1")

    def test_pop_empty_stack_raises_exception(self):
        stack = Stack()

        with self.assertRaisesRegex(Exception, "Stack is empty. Cannot pop."):
            stack.pop()

    def test_peek_empty_stack_raises_exception(self):
        stack = Stack()

        with self.assertRaisesRegex(Exception, "Stack is empty. Cannot peek."):
            stack.peek()

    def test_stack_accepts_different_element_types(self):
        stack = Stack()
        elements = [42, "text", [1, 2, 3]]
        nodes = [LinearNode(element) for element in elements]

        for node in nodes:
            stack.push(node)

        for element in reversed(elements):
            self.assertEqual(stack.pop().get_element(), element)

        self.assertTrue(stack.is_empty())


if __name__ == "__main__":
    unittest.main()
