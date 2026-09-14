from DSA.Collections.Lists.IList_ADT import IList_ADT
from DSA.Node.LinearNode import LinearNode

class List_ADT(IList_ADT):

    """
        A class representing a singly linked list. This is an unordered list.


    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def first(self) -> LinearNode:
        """
            Returns a reference to the first node in the list.
        """

        return self._head

    def last(self) -> LinearNode:
        """
            Returns a reference to the last node in the list.
        """

        return self._tail

    def is_empty(self) -> bool:
        """
            Returns True if the list is empty, False otherwise.
        """

        return self._head is None

    def size(self) -> int:
        """
            Returns the number of nodes in the list.
        """
        return self._count

    def to_string(self) -> str:
        """
            Returns a string representation of the list.

            Time Complexity: O(n), where n is the number of nodes in the list.
        """
        current = self._head
        result = []
        while current is not None:
            result.append(str(current.get_element()))
            current = current.get_next()
        return " -> ".join(result)

    def contains(self, node: LinearNode) -> bool:

        """
            Returns True if the list contains the given node, False otherwise.

            Time Complexity: O(n), where n is the number of nodes in the list.
        """

        is_found = False

        curr: LinearNode = self._head

        while curr:
            
            if curr.get_element() == node.get_element():
                is_found = True
                break

            curr = curr.get_next()

        return is_found


    def remove(self, node: LinearNode) -> LinearNode:
        """
            Removes the given node from the list and returns it.

            Time Complexity: O(n^2), where n is the number of nodes in the list.
        """

        previous = None
        current = self._head

        while current is not None:
            if current.get_element() == node.get_element():
                if previous is None:
                    self._head = current.get_next()
                else:
                    previous.set_next(current.get_next())

                if current is self._tail:
                    self._tail = previous

                self._count -= 1
                return current

            previous = current
            current = current.get_next()

        return None


    def remove_first(self) -> LinearNode:
        """
            Removes the first node from the list and returns it.

            Time Complexity: O(1)
        """

        if self._head is None:
            raise Exception("List is empty. Cannot remove first node.")

        node = self._head
        self._head = self._head.get_next()
        if self._head is None:
            self._tail = None
        self._count -= 1

        return node


    def remove_last(self) -> LinearNode:

        """
            Removes the last node from the list and returns it.

            Time Complexity: O(n), where n is the number of nodes in the list.
        """
        if self._head is None:
            raise Exception("List is empty. Cannot remove last node.")

        node = self._tail
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.get_next() is not self._tail:
                current = current.get_next()
            current.set_next(None)
            self._tail = current

        self._count -= 1

        return node

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

