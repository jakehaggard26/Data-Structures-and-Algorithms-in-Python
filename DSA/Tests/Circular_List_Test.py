import unittest

from DSA.Collections.Lists.Circular_List import Circular_List
from DSA.Collections.Lists.List import List
from DSA.Node.LinearNode import LinearNode


class TestCircularList(unittest.TestCase):

    def make_list(self, *elements):
        circular_list = Circular_List()
        for element in elements:
            circular_list.add(LinearNode(element))
        return circular_list

    def nodes(self, circular_list):
        result = []
        current = circular_list.first()

        for _ in range(circular_list.size()):
            result.append(current)
            current = current.get_next()

        return result

    def values(self, circular_list):
        return [node.get_element() for node in self.nodes(circular_list)]

    def assert_circular_invariants(self, circular_list, expected_values):
        if not expected_values:
            self.assertTrue(circular_list.is_empty())
            self.assertEqual(circular_list.size(), 0)
            self.assertIsNone(circular_list.first())
            self.assertIsNone(circular_list.last())
            return

        nodes = self.nodes(circular_list)

        self.assertFalse(circular_list.is_empty())
        self.assertEqual(circular_list.size(), len(expected_values))
        self.assertEqual(self.values(circular_list), expected_values)
        self.assertIs(circular_list.first(), nodes[0])
        self.assertIs(circular_list.last(), nodes[-1])
        self.assertIs(circular_list.last().get_next(), circular_list.first())
        self.assertIs(circular_list.first(), nodes[-1].get_next())

    def test_new_circular_list_is_empty(self):
        circular_list = Circular_List()

        self.assertIsInstance(circular_list, List)
        self.assert_circular_invariants(circular_list, [])
        self.assertEqual(circular_list.to_string(), "")

    def test_add_first_node_points_to_itself(self):
        circular_list = Circular_List()
        node = LinearNode("only")

        result = circular_list.add(node)

        self.assertIsNone(result)
        self.assertIs(circular_list.first(), node)
        self.assertIs(circular_list.last(), node)
        self.assertIs(node.get_next(), node)
        self.assert_circular_invariants(circular_list, ["only"])

    def test_add_second_node_updates_head_and_tail_links(self):
        circular_list = self.make_list("first")
        second = LinearNode("second")

        circular_list.add(second)

        self.assertIs(circular_list.first().get_next(), second)
        self.assertIs(circular_list.last(), second)
        self.assertIs(second.get_next(), circular_list.first())
        self.assert_circular_invariants(circular_list, ["first", "second"])

    def test_add_multiple_nodes_preserves_insertion_order(self):
        circular_list = self.make_list(1, 2, 3, 4)

        self.assertEqual(circular_list.to_string(), "1 -> 2 -> 3 -> 4")
        self.assert_circular_invariants(circular_list, [1, 2, 3, 4])

    def test_add_accepts_prelinked_node_without_attaching_external_chain(self):
        circular_list = self.make_list(1, 3)
        external = LinearNode("external")
        node = LinearNode(2, external)

        circular_list.add(node)

        self.assertIs(node.get_next(), circular_list.first())
        self.assertNotIn(external, self.nodes(circular_list))
        self.assert_circular_invariants(circular_list, [1, 3, 2])

    def test_add_supports_duplicate_values_as_distinct_nodes(self):
        circular_list = Circular_List()
        first = LinearNode("duplicate")
        second = LinearNode("duplicate")

        circular_list.add(first)
        circular_list.add(second)

        self.assertIs(circular_list.first(), first)
        self.assertIs(circular_list.last(), second)
        self.assertIs(first.get_next(), second)
        self.assertIs(second.get_next(), first)
        self.assert_circular_invariants(circular_list, ["duplicate", "duplicate"])

    def test_to_string_visits_each_node_once(self):
        circular_list = self.make_list("a", "b", "c")

        self.assertEqual(circular_list.to_string(), "a -> b -> c")

    def test_contains_finds_values_without_infinite_traversal(self):
        circular_list = self.make_list("first", "second", "third")

        self.assertTrue(circular_list.contains(LinearNode("first")))
        self.assertTrue(circular_list.contains(LinearNode("third")))
        self.assertFalse(circular_list.contains(LinearNode("missing")))

    def test_remove_first_returns_original_head(self):
        circular_list = self.make_list("first", "second", "third")
        original_head = circular_list.first()

        removed = circular_list.remove_first()

        self.assertIs(removed, original_head)
        self.assertIsNone(removed.get_next())
        self.assert_circular_invariants(circular_list, ["second", "third"])

    def test_remove_first_singleton_empties_list(self):
        circular_list = self.make_list("only")
        original_node = circular_list.first()

        removed = circular_list.remove_first()

        self.assertIs(removed, original_node)
        self.assertIsNone(removed.get_next())
        self.assert_circular_invariants(circular_list, [])

    def test_remove_first_empty_list_raises_exception(self):
        with self.assertRaisesRegex(Exception, "List Error: List is empty"):
            Circular_List().remove_first()

    def test_remove_last_returns_original_tail(self):
        circular_list = self.make_list("first", "middle", "last")
        original_tail = circular_list.last()

        removed = circular_list.remove_last()

        self.assertIs(removed, original_tail)
        self.assertIsNone(removed.get_next())
        self.assert_circular_invariants(circular_list, ["first", "middle"])

    def test_remove_last_singleton_empties_list(self):
        circular_list = self.make_list("only")
        original_node = circular_list.last()

        removed = circular_list.remove_last()

        self.assertIs(removed, original_node)
        self.assertIsNone(removed.get_next())
        self.assert_circular_invariants(circular_list, [])

    def test_remove_last_empty_list_raises_exception(self):
        with self.assertRaisesRegex(Exception, "List Error: List is empty"):
            Circular_List().remove_last()

    def test_remove_head_updates_circular_head_link(self):
        circular_list = self.make_list("first", "second", "third")
        original_head = circular_list.first()

        removed = circular_list.remove(original_head)

        self.assertIs(removed, original_head)
        self.assertIsNone(removed.get_next())
        self.assert_circular_invariants(circular_list, ["second", "third"])

    def test_remove_middle_relinks_neighbors(self):
        circular_list = self.make_list("first", "middle", "last")
        middle = circular_list.first().get_next()

        removed = circular_list.remove(middle)

        self.assertIs(removed, middle)
        self.assertIsNone(removed.get_next())
        self.assert_circular_invariants(circular_list, ["first", "last"])

    def test_remove_tail_updates_tail_and_head_link(self):
        circular_list = self.make_list("first", "middle", "last")
        original_tail = circular_list.last()

        removed = circular_list.remove(original_tail)

        self.assertIs(removed, original_tail)
        self.assertIsNone(removed.get_next())
        self.assert_circular_invariants(circular_list, ["first", "middle"])

    def test_remove_singleton_empties_list(self):
        circular_list = self.make_list("only")
        original_node = circular_list.first()

        removed = circular_list.remove(original_node)

        self.assertIs(removed, original_node)
        self.assertIsNone(removed.get_next())
        self.assert_circular_invariants(circular_list, [])

    def test_remove_duplicate_value_removes_first_match(self):
        circular_list = Circular_List()
        first = LinearNode("duplicate")
        second = LinearNode("duplicate")
        last = LinearNode("last")

        for node in (first, second, last):
            circular_list.add(node)

        removed = circular_list.remove(LinearNode("duplicate"))

        self.assertIs(removed, first)
        self.assertIs(circular_list.first(), second)
        self.assert_circular_invariants(circular_list, ["duplicate", "last"])

    def test_remove_missing_value_returns_none_without_mutating_list(self):
        circular_list = self.make_list("first", "second")
        before = circular_list.to_string()
        before_size = circular_list.size()

        removed = circular_list.remove(LinearNode("missing"))

        self.assertIsNone(removed)
        self.assertEqual(circular_list.to_string(), before)
        self.assertEqual(circular_list.size(), before_size)
        self.assert_circular_invariants(circular_list, ["first", "second"])

    def test_remove_empty_list_raises_exception(self):
        with self.assertRaisesRegex(Exception, "List Error: List is empty"):
            Circular_List().remove(LinearNode("missing"))

    def test_remove_all_nodes_preserves_invariants_until_empty(self):
        circular_list = self.make_list(1, 2, 3, 4, 5)

        for expected_values in ([2, 3, 4, 5], [3, 4, 5], [4, 5], [5], []):
            circular_list.remove_first()
            self.assert_circular_invariants(circular_list, expected_values)

    def test_mixed_removals_preserve_order_and_count(self):
        circular_list = self.make_list(1, 2, 3, 4, 5)

        circular_list.remove_last()
        circular_list.remove(LinearNode(2))
        circular_list.remove_first()

        self.assert_circular_invariants(circular_list, [3, 4])

    def test_size_tracks_additions_and_removals(self):
        circular_list = Circular_List()

        for value in range(10):
            circular_list.add(LinearNode(value))

        self.assertEqual(circular_list.size(), 10)

        for _ in range(4):
            circular_list.remove_last()

        self.assertEqual(circular_list.size(), 6)
        self.assert_circular_invariants(circular_list, [0, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
