import unittest

from DSA.Collections.Lists.List_ADT import List_ADT
from DSA.Node.LinearNode import LinearNode


class TestList(unittest.TestCase):

    def make_list(self, *elements):
        linked_list = List_ADT()
        for element in elements:
            linked_list.add_to_back(LinearNode(element))
        return linked_list

    def test_new_list_is_empty(self):
        linked_list = List_ADT()

        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size(), 0)
        self.assertIsNone(linked_list.first())
        self.assertIsNone(linked_list.last())
        self.assertEqual(linked_list.to_string(), "")

    def test_add_to_back_on_empty_list_sets_head_and_tail(self):
        linked_list = List_ADT()
        node = LinearNode("first")

        linked_list.add_to_back(node)

        self.assertIs(linked_list.first(), node)
        self.assertIs(linked_list.last(), node)
        self.assertIsNone(node.get_next())
        self.assertEqual(linked_list.size(), 1)

    def test_add_to_back_does_not_attach_a_prelinked_chain(self):
        linked_list = List_ADT()
        attached_node = LinearNode("attached")
        node = LinearNode("first", attached_node)

        linked_list.add_to_back(node)

        self.assertIs(linked_list.first(), node)
        self.assertIs(linked_list.last(), node)
        self.assertIsNone(node.get_next())
        self.assertEqual(linked_list.to_string(), "first")
        self.assertEqual(linked_list.size(), 1)

    def test_add_to_back_appends_nodes_in_order(self):
        linked_list = List_ADT()
        first = LinearNode("first")
        second = LinearNode("second")
        third = LinearNode("third")

        for node in (first, second, third):
            linked_list.add_to_back(node)

        self.assertIs(linked_list.first(), first)
        self.assertIs(linked_list.last(), third)
        self.assertIs(first.get_next(), second)
        self.assertIs(second.get_next(), third)
        self.assertIsNone(third.get_next())
        self.assertEqual(linked_list.size(), 3)
        self.assertEqual(linked_list.to_string(), "first -> second -> third")

    def test_add_to_front_on_empty_list_sets_head_and_tail(self):
        linked_list = List_ADT()
        node = LinearNode("first")

        linked_list.add_to_front(node)

        self.assertIs(linked_list.first(), node)
        self.assertIs(linked_list.last(), node)
        self.assertEqual(linked_list.size(), 1)

    def test_add_to_front_prepends_nodes_in_order(self):
        linked_list = self.make_list("middle", "last")
        original_middle = linked_list.first()
        first = LinearNode("first")

        linked_list.add_to_front(first)

        self.assertIs(linked_list.first(), first)
        self.assertEqual(linked_list.last().get_element(), "last")
        self.assertIs(first.get_next(), original_middle)
        self.assertEqual(linked_list.to_string(), "first -> middle -> last")
        self.assertEqual(linked_list.size(), 3)

    def test_add_to_front_replaces_a_prelinked_chain(self):
        linked_list = self.make_list("last")
        attached_node = LinearNode("attached")
        node = LinearNode("first", attached_node)

        linked_list.add_to_front(node)

        self.assertIs(linked_list.first(), node)
        self.assertIs(node.get_next(), linked_list.last())
        self.assertEqual(linked_list.to_string(), "first -> last")
        self.assertEqual(linked_list.size(), 2)

    def test_contains_matches_node_elements_not_node_identity(self):
        linked_list = self.make_list("first", "second")

        self.assertTrue(linked_list.contains(LinearNode("second")))
        self.assertFalse(linked_list.contains(LinearNode("missing")))
        self.assertFalse(linked_list.contains(LinearNode("FIRST")))

    def test_contains_supports_different_element_types(self):
        linked_list = self.make_list(42, "text", [1, 2, 3], None)

        for element in (42, "text", [1, 2, 3], None):
            self.assertTrue(linked_list.contains(LinearNode(element)))

    def test_remove_first_node_returns_original_and_updates_head(self):
        linked_list = self.make_list("first", "second", "third")
        original_first = linked_list.first()

        removed = linked_list.remove(original_first)

        self.assertIs(removed, original_first)
        self.assertEqual(removed.get_element(), "first")
        self.assertEqual(linked_list.to_string(), "second -> third")
        self.assertEqual(linked_list.size(), 2)
        self.assertEqual(linked_list.first().get_element(), "second")
        self.assertEqual(linked_list.last().get_element(), "third")

    def test_remove_middle_node_relinks_neighbors(self):
        linked_list = self.make_list("first", "middle", "last")
        middle = linked_list.first().get_next()

        removed = linked_list.remove(middle)

        self.assertEqual(removed.get_element(), "middle")
        self.assertEqual(linked_list.to_string(), "first -> last")
        self.assertIs(linked_list.first().get_next(), linked_list.last())
        self.assertEqual(linked_list.size(), 2)

    def test_remove_last_node_updates_tail(self):
        linked_list = self.make_list("first", "middle", "last")
        last = linked_list.last()

        removed = linked_list.remove(last)

        self.assertEqual(removed.get_element(), "last")
        self.assertEqual(linked_list.to_string(), "first -> middle")
        self.assertEqual(linked_list.last().get_element(), "middle")
        self.assertIsNone(linked_list.last().get_next())
        self.assertEqual(linked_list.size(), 2)

    def test_remove_uses_the_first_matching_value(self):
        linked_list = self.make_list("duplicate", "duplicate", "last")
        second_duplicate = linked_list.first().get_next()

        removed = linked_list.remove(second_duplicate)

        self.assertEqual(removed.get_element(), "duplicate")
        self.assertEqual(linked_list.to_string(), "duplicate -> last")
        self.assertIs(linked_list.first(), second_duplicate)
        self.assertEqual(linked_list.size(), 2)

    def test_remove_missing_node_returns_none_without_changing_list(self):
        linked_list = self.make_list("first", "second")

        removed = linked_list.remove(LinearNode("missing"))

        self.assertIsNone(removed)
        self.assertEqual(linked_list.to_string(), "first -> second")
        self.assertEqual(linked_list.size(), 2)

    def test_remove_first_returns_head_and_preserves_tail(self):
        linked_list = self.make_list("first", "second", "third")
        original_first = linked_list.first()
        original_tail = linked_list.last()

        removed = linked_list.remove_first()

        self.assertIs(removed, original_first)
        self.assertEqual(removed.get_element(), "first")
        self.assertEqual(linked_list.first().get_element(), "second")
        self.assertIs(linked_list.last(), original_tail)
        self.assertEqual(linked_list.size(), 2)

    def test_remove_first_on_singleton_list_empties_list(self):
        linked_list = self.make_list("only")

        removed = linked_list.remove_first()

        self.assertEqual(removed.get_element(), "only")
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size(), 0)
        self.assertIsNone(linked_list.first())

    def test_remove_first_on_empty_list_raises_exception(self):
        with self.assertRaisesRegex(Exception, "List is empty. Cannot remove first node."):
            List_ADT().remove_first()

    def test_remove_last_returns_tail_and_preserves_head(self):
        linked_list = self.make_list("first", "second", "third")
        original_head = linked_list.first()
        original_tail = linked_list.last()

        removed = linked_list.remove_last()

        self.assertIs(removed, original_tail)
        self.assertEqual(removed.get_element(), "third")
        self.assertIs(linked_list.first(), original_head)
        self.assertEqual(linked_list.last().get_element(), "second")
        self.assertEqual(linked_list.size(), 2)

    def test_remove_last_on_singleton_list_empties_list(self):
        linked_list = self.make_list("only")
        original_node = linked_list.last()

        removed = linked_list.remove_last()

        self.assertIs(removed, original_node)
        self.assertEqual(removed.get_element(), "only")
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size(), 0)
        self.assertIsNone(linked_list.last())

    def test_remove_last_on_empty_list_raises_exception(self):
        with self.assertRaisesRegex(Exception, "List is empty. Cannot remove last node."):
            List_ADT().remove_last()

    def test_add_after_inserts_after_matching_node(self):
        linked_list = self.make_list("first", "last")
        target = linked_list.first()
        new_node = LinearNode("middle")

        linked_list.add_after(target, new_node)

        self.assertEqual(linked_list.to_string(), "first -> middle -> last")
        self.assertIs(linked_list.first().get_next(), new_node)
        self.assertEqual(linked_list.last().get_element(), "last")
        self.assertEqual(linked_list.size(), 3)

    def test_add_after_can_insert_after_tail(self):
        linked_list = self.make_list("first", "last")
        target = linked_list.last()
        new_node = LinearNode("after-last")

        linked_list.add_after(target, new_node)

        self.assertEqual(linked_list.to_string(), "first -> last -> after-last")
        self.assertIs(linked_list.last(), new_node)
        self.assertEqual(linked_list.size(), 3)

    def test_add_after_uses_the_first_matching_target_value(self):
        linked_list = self.make_list("duplicate", "duplicate", "last")
        target = LinearNode("duplicate")
        new_node = LinearNode("inserted")

        linked_list.add_after(target, new_node)

        self.assertEqual(
            linked_list.to_string(), "duplicate -> inserted -> duplicate -> last"
        )
        self.assertIs(linked_list.first().get_next(), new_node)
        self.assertEqual(linked_list.size(), 4)

    def test_add_after_on_empty_list_raises_exception(self):
        with self.assertRaisesRegex(Exception, "List Error"):
            List_ADT().add_after(LinearNode("target"), LinearNode("new"))

    def test_add_after_missing_node_raises_exception_without_mutating_list(self):
        linked_list = self.make_list("first", "last")

        with self.assertRaisesRegex(Exception, "List Error"):
            linked_list.add_after(LinearNode("missing"), LinearNode("new"))

        self.assertEqual(linked_list.to_string(), "first -> last")
        self.assertEqual(linked_list.size(), 2)

    def test_operations_preserve_values_with_none_and_collections(self):
        linked_list = self.make_list(None, {"key": "value"}, [1, 2])

        self.assertEqual(linked_list.to_string(), "None -> {'key': 'value'} -> [1, 2]")
        self.assertTrue(linked_list.contains(LinearNode({"key": "value"})))


if __name__ == "__main__":
    unittest.main()