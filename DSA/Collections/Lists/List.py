from DSA.Collections.Lists.IList import IList
from DSA.Node.Node import Node

class List(IList):

    """
        A class representing a singly linked list. This is an unordered list.


    """

    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def first(self) -> Node:
        """
            Returns a reference to the first node in the list.
        """

        return self.head

    def last(self) -> Node:
        """
            Returns a reference to the last node in the list.
        """

        return self.tail

    def is_empty(self) -> bool:
        """
            Returns True if the list is empty, False otherwise.
        """

        return self.head is None

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
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

    def contains(self, node: Node) -> bool:

        """
            Returns True if the list contains the given node, False otherwise.

            Time Complexity: O(n), where n is the number of nodes in the list.
        """

        is_found = False

        curr: Node = self.head

        while curr:
            
            if curr.get_element() == node.get_element():
                is_found = True
                break

            curr = curr.next

        return is_found


    def remove(self, node: Node) -> Node:
        """
            Removes the given node from the list and returns it.

            Time Complexity: O(n^2), where n is the number of nodes in the list.
        """

        output: Node = None
        curr: Node = self.head

        while curr:

            if curr.get_element() == node.get_element():

                # Store a copy of the node to be removed
                output = Node(curr.get_element())

                # Update references (see cases below)

                # If the node to be removed is the head, update head to the next node
                if(curr == self.head):
                    self.head = curr.next

                # If the node to be removed is the tail, update tail to the previous node
                if(curr == self.tail):
                    temp: Node = self.head
                    # Loop until we find the node before the tail
                    while temp.next != self.tail:
                        temp = temp.next
                    # Update tail reference to point to the previous node of the prior tail
                    self.tail = temp

                # If the node to be removed is in the middle, update the next reference of the previous node to skip the current node
                if(curr != self.head and curr != self.tail):
                    temp: Node = self.head
                    # Loop until we find the node before the current node
                    while temp.next != curr:
                        temp = temp.next
                    # Update the next reference of the previous node to skip the current node
                    temp.next = curr.next

        self._count -= 1
        
        return output


    def remove_first(self) -> Node:
        """
            Removes the first node from the list and returns it.

            Time Complexity: O(1)
        """

        node: Node = None

        if self.head is None:
            raise Exception("List is empty. Cannot remove first node.")
            
        node = Node(self.head.get_element())
        self.head = self.head.next
        self._count -= 1

        return node


    def remove_last(self) -> Node:

        """
            Removes the last node from the list and returns it.

            Time Complexity: O(n), where n is the number of nodes in the list.
        """
        node: Node = self.tail

        if self.head is None:
            raise Exception("List is empty. Cannot remove last node.")

        curr: Node = self.head

        while curr.next != self.tail:
            curr = curr.next

        self.tail = curr

        self._count -= 1

        return node

    def add_to_back(self, node: Node) -> Node:

        """
            Adds the given node to the end of the list.

            Time Complexity: O(1)
        """

        # Check if the list is empty
        if self.head is None:
            self.head = node
            self.tail = node
            self._count += 1

        # Check if the list has only one node
        elif(self.head == self.tail):
            self.head.next = node
            self.tail = node
            self._count += 1

        # Add to the end of the list when both head and tail are not None or the same node
        else:
            self.tail.next = node
            self.tail = node
            self._count += 1

        return 

    