from DSA.Node.LinearNode import LinearNode
from DSA.Collections.Stack.IStack import IStack

class Stack(IStack):

    """
        A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
        The Stack class provides methods to add, remove, and inspect elements in the stack.
    """

    def __init__(self):
        self._top: LinearNode = None
        self._count: int = 0

    def push(self, node: LinearNode) -> None:
        """
            Adds a node to the stack. The new node becomes the top of the stack.

            Has the following constraints:
            - The new node's next reference points to the current top node.
            - The top reference is updated to point to the new node.
            - The count of nodes in the stack is incremented by 1.

            Time Complexity: O(1)
        """

        # Update new node's next reference to point to the current top node
        node.set_next(self._top)

        # Update the top reference to point to the new node
        self._top = node

        # Increment the count of nodes in the stack
        self._count += 1

    def pop(self) -> LinearNode:

        """
            Removes and returns the top node of the stack. Raises an exception if the stack is empty.

            Has the following constraints:
            - The top reference is updated to point to the next node in the stack.
            - The count of nodes in the stack is decremented by 1.
            - Returns the node that was removed from the stack.

            Time Complexity: O(1)
        """

        if(self.is_empty()):
            raise Exception("Stack is empty. Cannot pop.")

        # Store the current top node to return it later
        node = self._top

        # Update the top reference to point to the next node in the stack
        self._top = self._top.get_next()

        # Decrement the count of nodes in the stack
        self._count -= 1

        return node
        

    def peek(self) -> LinearNode:

        """
            Returns the top node of the stack without removing it.

            Raises an exception if the stack is empty.
        """
        if(self.is_empty()):
            raise Exception("Stack is empty. Cannot peek.")

        return self._top

    def is_empty(self) -> bool:
        """
            Returns True if the stack is empty, False otherwise.
            
            Time Complexity: O(1)
            
        """

        return self._top is None

    def size(self) -> int:
        """
            Returns the number of nodes in the stack.
            
            Time Complexity: O(1)
        """

        return self._count

    def to_string(self) -> str:
        """
            Returns a string representation of the stack, showing the elements from top to bottom.

            Time Complexity: O(n), where n is the number of nodes in the stack.
        """
        elements = []
        current_node = self._top
        while current_node is not None:
            elements.append(str(current_node.get_element()))
            current_node = current_node.get_next()
        return "Stack(top -> bottom): " + " -> ".join(elements)