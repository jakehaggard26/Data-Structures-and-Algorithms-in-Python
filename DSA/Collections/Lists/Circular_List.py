from DSA.Collections.Lists.ICircular_List import ICircular_List
from DSA.Collections.Lists.List import List
from DSA.Node.LinearNode import LinearNode

class Circular_List(ICircular_List, List):

    """
        An Unordered Circular List
    """
    def __init__(self):
        super().__init__()


    def first(self) -> LinearNode:
        return self._head

    def last(self) -> LinearNode:
        return self._tail

    def add(self, node: LinearNode) -> None:

        # Add if empty
        if self._head is None:
            self._head = node
            self._tail = node
            node.set_next(node)

        # Add if 1 Node is in the list
        elif self._head is self._tail:
            self._tail = node
            self._head.set_next(node)
            node.set_next(self._head)

        # Add when 2 or more nodes are in the list
        else:
            self._tail.set_next(node)
            self._tail = node
            node.set_next(self._head)

        self._count += 1

        return

    # Override?
    def remove_first(self) -> LinearNode:

        # If list is empty
        if self._head is None:
            raise Exception("List Error: List is empty")

        removed: LinearNode = self._head

        if self._head is self._tail:
            self._tail = None
            self._head = None

        else:
            self._head = self._head.get_next()
            self._tail.set_next(self._head)

        removed.set_next(None)
        self._count -= 1
        return removed


    def remove_last(self) -> LinearNode:

        curr: LinearNode = self._head
        removed: LinearNode = self._tail

        # If empty
        if self._head is None:
            raise Exception("List Error: List is empty")

        # If one element in the list
        if self._head is self._tail:
            self._head = None
            self._tail = None

        else:
            while curr.get_next() is not self._tail:
                curr = curr.get_next()

            self._tail = curr
            self._tail.set_next(self._head)

        removed.set_next(None)
        self._count -= 1
        return removed

        

    def remove(self, node: LinearNode) -> LinearNode:

        # Empty List check
        if self._head is None:
            raise Exception("List Error: List is empty")

        curr: LinearNode = self._head
        prev: LinearNode = self._tail

        while True:
            # If we find the node of interest
            if curr.get_element() == node.get_element():

                # If head and tail are the same node 
                if self._head is self._tail:
                    self._tail = None
                    self._head = None

                # Head and tail are not the same node
                else:
                    prev.set_next(curr.get_next())

                    # Remove from the front
                    if curr is self._head:
                        self._head = curr.get_next()

                    # Remove from the back
                    if curr is self._tail:
                        self._tail = prev

                    # Update circular reference
                    self._tail.set_next(self._head)

                # Update currrent node's next reference
                curr.set_next(None)

                # Update count
                self._count -= 1

                # Return current node
                return curr 

            # Update nodes every iteration
            prev = curr
            curr = curr.get_next()

            # Full iteration -> End search, will return none
            if curr is self._head:
                break


        return None

    # Add override?
    def to_string(self) -> str:
        """
            Returns a string representation of the list.

            Time Complexity: O(n), where n is the number of nodes in the list.
        """
        count: int = 0
        current: LinearNode = self._head
        result: list = []
        while current is not None and count < self.size():
            result.append(str(current.get_element()))
            current = current.get_next()
            count += 1
        return " -> ".join(result)

    def contains(self, node: LinearNode) -> bool:
        """
            Returns True if the list contains the given node, False otherwise.

            Time Complexity: O(n), where n is the number of nodes in the list.
        """
        
        is_found: bool = False
        count: int = 0

        curr: LinearNode = self._head

        while curr and count < self.size():
            
            if curr.get_element() == node.get_element():
                is_found = True
                break

            curr = curr.get_next()
            count += 1

        return is_found