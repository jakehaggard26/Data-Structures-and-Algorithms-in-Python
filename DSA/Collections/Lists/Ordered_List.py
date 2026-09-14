from DSA.Node.LinearNode import LinearNode
from DSA.Collections.Lists.IOrdered_List import IOrdered_List
from DSA.Collections.Lists.List_ADT import List_ADT


class Ordered_List(List_ADT, IOrdered_List):

    def __init__(self, ascending: bool = True):
        super().__init__()
        self._ascending = ascending


    def __add_ascending(self, node: LinearNode) -> None:
        node.set_next(None)

        # Check if list is empty
        if self._head is None:
            self._head = node
            self._tail = node
            self._count = 1
            return

        # If node is less than the head. add to start
        if node.get_element() < self._head.get_element():
            node.set_next(self._head)
            self._head = node
            self._count += 1
            return

        # Set prev to head, update current node
        previous = self._head
        current = self._head.get_next()

        # Loop until current is not null and current is less than or equal to the node we ant to add
        while current is not None and current.get_element() <= node.get_element():
            previous = current
            current = current.get_next()

        # Loop ends at point of insertion; Update references
        node.set_next(current)
        previous.set_next(node)

        # If added to the end of the lists
        if current is None:
            self._tail = node

        # Update the count
        self._count += 1


    def __add_descending(self, node: LinearNode) -> None:
        node.set_next(None)

        # Check if list is empty
        if self._head is None:
            self._head = node
            self._tail = node
            self._count = 1
            return

        # If node is greater than the head, add to start
        if node.get_element() > self._head.get_element():
            node.set_next(self._head)
            self._head = node
            self._count += 1
            return

        previous = self._head
        current = self._head.get_next()

        # Keep equal values together in insertion order.
        while current is not None and current.get_element() >= node.get_element():
            previous = current
            current = current.get_next()

        node.set_next(current)
        previous.set_next(node)

        if current is None:
            self._tail = node

        self._count += 1



    def add(self, node: LinearNode) -> None:

        if self._ascending:
            self.__add_ascending(node)
        else:
            self.__add_descending(node)
 
        return