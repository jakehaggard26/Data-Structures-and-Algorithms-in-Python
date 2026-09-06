import unittest

from DSA.Collections.Queue.Queue import Queue
from DSA.Node.LinearNode import LinearNode


class TestQueue(unittest.TestCase):

    def test_new_queue_is_empty(self):
        queue = Queue()

        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)

    def test_enqueue_adds_node(self):
        queue = Queue()
        node = LinearNode("first")

        queue.enqueue(node)

        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 1)
        self.assertIs(queue.first(), node)

    def test_enqueue_places_new_node_at_tail(self):
        queue = Queue()
        first_node = LinearNode("first")
        second_node = LinearNode("second")

        queue.enqueue(first_node)
        queue.enqueue(second_node)

        self.assertIs(queue.first(), first_node)
        self.assertIs(first_node.get_next(), second_node)
        self.assertEqual(queue.size(), 2)

    def test_dequeue_returns_nodes_in_first_in_first_out_order(self):
        queue = Queue()
        first_node = LinearNode("first")
        second_node = LinearNode("second")

        queue.enqueue(first_node)
        queue.enqueue(second_node)

        self.assertIs(queue.dequeue(), first_node)
        self.assertIs(queue.dequeue(), second_node)

    def test_dequeue_decreases_size(self):
        queue = Queue()
        queue.enqueue(LinearNode("first"))
        queue.enqueue(LinearNode("second"))

        queue.dequeue()

        self.assertEqual(queue.size(), 1)
        self.assertFalse(queue.is_empty())

        queue.dequeue()

        self.assertEqual(queue.size(), 0)
        self.assertTrue(queue.is_empty())

    def test_first_returns_head_without_removing_it(self):
        queue = Queue()
        node = LinearNode("first")
        queue.enqueue(node)

        first_node = queue.first()

        self.assertIs(first_node, node)
        self.assertEqual(queue.size(), 1)
        self.assertFalse(queue.is_empty())

    def test_to_string_for_empty_queue(self):
        queue = Queue()

        self.assertEqual(queue.to_string(), "Queue(head -> tail): ")

    def test_to_string_shows_elements_from_head_to_tail(self):
        queue = Queue()
        queue.enqueue(LinearNode(1))
        queue.enqueue(LinearNode(2))
        queue.enqueue(LinearNode(3))

        self.assertEqual(queue.to_string(), "Queue(head -> tail): 1 -> 2 -> 3")

    def test_dequeue_empty_queue_raises_exception(self):
        queue = Queue()

        with self.assertRaisesRegex(Exception, "Queue is empty. Cannot dequeue."):
            queue.dequeue()

    def test_first_empty_queue_raises_exception(self):
        queue = Queue()

        with self.assertRaisesRegex(
            Exception, "Queue is empty. Cannot retrieve first element."
        ):
            queue.first()

    def test_queue_accepts_different_element_types(self):
        queue = Queue()
        elements = [42, "text", [1, 2, 3]]

        for element in elements:
            queue.enqueue(LinearNode(element))

        for element in elements:
            self.assertEqual(queue.dequeue().get_element(), element)

        self.assertTrue(queue.is_empty())


if __name__ == "__main__":
    unittest.main()
