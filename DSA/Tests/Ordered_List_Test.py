import unittest

from DSA.Collections.Lists.Ordered_List import Ordered_List
from DSA.Collections.Lists.List_ADT import List_ADT
from DSA.Node.LinearNode import LinearNode


class TestOrderedList(unittest.TestCase):

    def make_list(self, *elements, ascending=True):
        ordered_list = Ordered_List(ascending=ascending)
        for element in elements:
            ordered_list.add(LinearNode(element))
        return ordered_list

    def node_values(self, ordered_list):
        values = []
        current = ordered_list.first()
        while current is not None:
            values.append(current.get_element())
            current = current.get_next()
        return values

    def nodes(self, ordered_list):
        result = []
        current = ordered_list.first()
        while current is not None:
            result.append(current)
            current = current.get_next()
        return result

    def assert_invariants(self, ordered_list, expected_values):
        nodes = self.nodes(ordered_list)

        self.assertEqual(self.node_values(ordered_list), expected_values)
        self.assertEqual(ordered_list.size(), len(expected_values))
        self.assertEqual(len(nodes), ordered_list.size())

        if expected_values:
            self.assertIs(ordered_list.first(), nodes[0])
            self.assertIs(ordered_list.last(), nodes[-1])
            self.assertIsNone(ordered_list.last().get_next())
        else:
            self.assertIsNone(ordered_list.first())
            self.assertIsNone(ordered_list.last())
            self.assertTrue(ordered_list.is_empty())

    def test_new_list_is_empty_in_ascending_mode(self):
        ordered_list = Ordered_List()

        self.assertTrue(ordered_list.is_empty())
        self.assertEqual(ordered_list.size(), 0)
        self.assertEqual(ordered_list.to_string(), "")
        self.assertIsNone(ordered_list.first())
        self.assertIsNone(ordered_list.last())

    def test_new_list_is_empty_in_descending_mode(self):
        ordered_list = Ordered_List(ascending=False)

        self.assertTrue(ordered_list.is_empty())
        self.assertEqual(ordered_list.size(), 0)
        self.assertEqual(ordered_list.to_string(), "")

    def test_ordered_list_inherits_list_adt_behavior(self):
        ordered_list = Ordered_List()

        self.assertIsInstance(ordered_list, List_ADT)
        self.assertTrue(hasattr(ordered_list, "contains"))
        self.assertTrue(hasattr(ordered_list, "remove"))
        self.assertTrue(hasattr(ordered_list, "remove_first"))
        self.assertTrue(hasattr(ordered_list, "remove_last"))

    def test_first_ascending_add_sets_head_and_tail(self):
        ordered_list = Ordered_List()
        node = LinearNode(10)

        result = ordered_list.add(node)

        self.assertIsNone(result)
        self.assertIs(ordered_list.first(), node)
        self.assertIs(ordered_list.last(), node)
        self.assert_invariants(ordered_list, [10])

    def test_first_descending_add_sets_head_and_tail(self):
        ordered_list = Ordered_List(ascending=False)
        node = LinearNode(10)

        ordered_list.add(node)

        self.assertIs(ordered_list.first(), node)
        self.assertIs(ordered_list.last(), node)
        self.assert_invariants(ordered_list, [10])

    def test_ascending_inserts_before_head(self):
        ordered_list = self.make_list(10, 20, 30)
        node = LinearNode(1)

        ordered_list.add(node)

        self.assertIs(ordered_list.first(), node)
        self.assert_invariants(ordered_list, [1, 10, 20, 30])

    def test_ascending_inserts_between_existing_nodes(self):
        ordered_list = self.make_list(10, 30)
        node = LinearNode(20)

        ordered_list.add(node)

        self.assertIs(ordered_list.first().get_next(), node)
        self.assert_invariants(ordered_list, [10, 20, 30])

    def test_ascending_inserts_after_tail(self):
        ordered_list = self.make_list(10, 20)
        node = LinearNode(30)

        ordered_list.add(node)

        self.assertIs(ordered_list.last(), node)
        self.assert_invariants(ordered_list, [10, 20, 30])

    def test_descending_inserts_before_head(self):
        ordered_list = self.make_list(30, 20, 10, ascending=False)
        node = LinearNode(40)

        ordered_list.add(node)

        self.assertIs(ordered_list.first(), node)
        self.assert_invariants(ordered_list, [40, 30, 20, 10])

    def test_descending_inserts_between_existing_nodes(self):
        ordered_list = self.make_list(30, 10, ascending=False)
        node = LinearNode(20)

        ordered_list.add(node)

        self.assertIs(ordered_list.first().get_next(), node)
        self.assert_invariants(ordered_list, [30, 20, 10])

    def test_descending_inserts_after_tail(self):
        ordered_list = self.make_list(30, 20, ascending=False)
        node = LinearNode(10)

        ordered_list.add(node)

        self.assertIs(ordered_list.last(), node)
        self.assert_invariants(ordered_list, [30, 20, 10])

    def test_ascending_duplicate_values_are_stable(self):
        ordered_list = Ordered_List()
        first = LinearNode(5)
        second = LinearNode(5)
        third = LinearNode(5)

        for node in (first, second, third):
            ordered_list.add(node)

        self.assertEqual(ordered_list.to_string(), "5 -> 5 -> 5")
        self.assertIs(ordered_list.first(), first)
        self.assertIs(first.get_next(), second)
        self.assertIs(second.get_next(), third)
        self.assert_invariants(ordered_list, [5, 5, 5])

    def test_descending_duplicate_values_are_stable(self):
        ordered_list = Ordered_List(ascending=False)
        first = LinearNode(5)
        second = LinearNode(5)
        third = LinearNode(5)

        for node in (first, second, third):
            ordered_list.add(node)

        self.assertEqual(ordered_list.to_string(), "5 -> 5 -> 5")
        self.assertIs(ordered_list.first(), first)
        self.assertIs(first.get_next(), second)
        self.assertIs(second.get_next(), third)
        self.assert_invariants(ordered_list, [5, 5, 5])

    def test_ascending_handles_negative_and_zero_values(self):
        ordered_list = self.make_list(0, -10, 10, -1, 1)

        self.assert_invariants(ordered_list, [-10, -1, 0, 1, 10])

    def test_descending_handles_negative_and_zero_values(self):
        ordered_list = self.make_list(0, -10, 10, -1, 1, ascending=False)

        self.assert_invariants(ordered_list, [10, 1, 0, -1, -10])

    def test_ascending_handles_float_values(self):
        ordered_list = self.make_list(1.5, -2.25, 0.0, 1.5)

        self.assert_invariants(ordered_list, [-2.25, 0.0, 1.5, 1.5])

    def test_descending_handles_float_values(self):
        ordered_list = self.make_list(1.5, -2.25, 0.0, 1.5, ascending=False)

        self.assert_invariants(ordered_list, [1.5, 1.5, 0.0, -2.25])

    def test_strings_are_sorted_lexicographically(self):
        ordered_list = self.make_list("pear", "apple", "orange", "banana")

        self.assert_invariants(ordered_list, ["apple", "banana", "orange", "pear"])

    def test_boolean_values_follow_python_ordering(self):
        ordered_list = self.make_list(True, False, True, False)

        self.assert_invariants(ordered_list, [False, False, True, True])

    def test_prelinked_node_does_not_attach_external_chain_in_ascending_mode(self):
        ordered_list = self.make_list(1, 5)
        external = LinearNode(999)
        node = LinearNode(3, external)

        ordered_list.add(node)

        self.assertIsNone(node.get_next().get_next())
        self.assert_invariants(ordered_list, [1, 3, 5])

    def test_prelinked_node_does_not_attach_external_chain_in_descending_mode(self):
        ordered_list = self.make_list(5, 1, ascending=False)
        external = LinearNode(-999)
        node = LinearNode(3, external)

        ordered_list.add(node)

        self.assertIsNone(node.get_next().get_next())
        self.assert_invariants(ordered_list, [5, 3, 1])

    def test_ascending_add_does_not_mutate_existing_nodes(self):
        ordered_list = self.make_list(1, 3)
        first = ordered_list.first()
        last = ordered_list.last()
        node = LinearNode(2)

        ordered_list.add(node)

        self.assertIs(ordered_list.first(), first)
        self.assertIs(ordered_list.last(), last)
        self.assertIs(first.get_next(), node)
        self.assertIs(node.get_next(), last)

    def test_descending_add_does_not_mutate_existing_nodes(self):
        ordered_list = self.make_list(3, 1, ascending=False)
        first = ordered_list.first()
        last = ordered_list.last()
        node = LinearNode(2)

        ordered_list.add(node)

        self.assertIs(ordered_list.first(), first)
        self.assertIs(ordered_list.last(), last)
        self.assertIs(first.get_next(), node)
        self.assertIs(node.get_next(), last)

    def test_ascending_add_rejects_incomparable_value_without_mutating_list(self):
        ordered_list = self.make_list(1, 3)
        before = ordered_list.to_string()
        count = ordered_list.size()
        node = LinearNode("two")

        with self.assertRaises(TypeError):
            ordered_list.add(node)

        self.assertEqual(ordered_list.to_string(), before)
        self.assertEqual(ordered_list.size(), count)
        self.assertIsNone(ordered_list.last().get_next())

    def test_descending_add_rejects_incomparable_value_without_mutating_list(self):
        ordered_list = self.make_list(3, 1, ascending=False)
        before = ordered_list.to_string()
        count = ordered_list.size()
        node = LinearNode("two")

        with self.assertRaises(TypeError):
            ordered_list.add(node)

        self.assertEqual(ordered_list.to_string(), before)
        self.assertEqual(ordered_list.size(), count)
        self.assertIsNone(ordered_list.last().get_next())

    def test_contains_works_after_ordered_insertions(self):
        ordered_list = self.make_list(4, 1, 3)

        self.assertTrue(ordered_list.contains(LinearNode(1)))
        self.assertTrue(ordered_list.contains(LinearNode(4)))
        self.assertFalse(ordered_list.contains(LinearNode(2)))

    def test_remove_preserves_order_in_ascending_list(self):
        ordered_list = self.make_list(1, 2, 3, 4)

        removed = ordered_list.remove(LinearNode(2))

        self.assertEqual(removed.get_element(), 2)
        self.assert_invariants(ordered_list, [1, 3, 4])

    def test_remove_preserves_order_in_descending_list(self):
        ordered_list = self.make_list(4, 3, 2, 1, ascending=False)

        removed = ordered_list.remove(LinearNode(3))

        self.assertEqual(removed.get_element(), 3)
        self.assert_invariants(ordered_list, [4, 2, 1])

    def test_remove_first_and_last_work_after_ordered_insertions(self):
        ordered_list = self.make_list(4, 1, 3, 2)

        self.assertEqual(ordered_list.remove_first().get_element(), 1)
        self.assertEqual(ordered_list.remove_last().get_element(), 4)
        self.assert_invariants(ordered_list, [2, 3])

    def test_ordering_remains_correct_after_removing_all_nodes(self):
        ordered_list = self.make_list(3, 1, 2)

        ordered_list.remove_first()
        ordered_list.remove_first()
        ordered_list.remove_first()

        self.assert_invariants(ordered_list, [])

    def test_add_normalizes_a_removed_node_before_reinserting(self):
        ordered_list = self.make_list(1, 2, 3)
        removed = ordered_list.remove_first()

        ordered_list.add(removed)

        self.assert_invariants(ordered_list, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
