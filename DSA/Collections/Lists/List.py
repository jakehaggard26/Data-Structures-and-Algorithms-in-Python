from abc import ABC, abstractmethod
from DSA.Node.LinearNode import LinearNode
from DSA.Collections.Lists.IList import IList
from DSA.Collections.Lists.List_ADT import List_ADT

class List(List_ADT, IList):

    def __init__(self):
        super().__init__()


    def add_to_back(self, node: LinearNode) -> LinearNode:

        """
            Adds the given node to the end of the list.

            Time Complexity: O(1)
        """

        node.set_next(None)

        # Check if the list is empty
        if self._head is None:
            self._head = node
            self._tail = node
            self._count += 1

        # Check if the list has only one node
        elif self._head is self._tail:
            self._head.set_next(node)
            self._tail = node
            self._count += 1

        # Add to the end of the list when both head and tail are not None or the same node
        else:
            self._tail.set_next(node)
            self._tail = node
            self._count += 1

        return 


    def add_to_front(self, node: LinearNode) -> None:

        """
            Adds the given node to the front of the list.

            Time Complexity: O(1)
        """

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.set_next(self._head)
            self._head = node

        self._count += 1

        return


    def add_after(self, target: LinearNode, node: LinearNode) -> None:

        curr = self._head

        while curr:
            if curr.get_element() == target.get_element():
                node.set_next(curr.get_next())
                curr.set_next(node)
                if curr is self._tail:
                    self._tail = node
                self._count += 1
                return

            curr = curr.get_next()

        raise Exception(f"List Error: Can't add {node}")
