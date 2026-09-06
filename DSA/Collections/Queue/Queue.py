from  DSA.Collections.Queue.IQueue import IQueue
from DSA.Node.LinearNode import LinearNode

class Queue(IQueue):

    def __init__(self):
        self._head: LinearNode = None
        self._tail: LinearNode = None
        self._count: int = 0

    def enqueue(self, node: LinearNode) -> None:
        """
            Adds a node to the end of the queue. The new node becomes the tail of the queue unless 
            the queue is empty, in which case it becomes both the head and tail of the queue.

            Has the following constraints:
            - If the queue is empty, both the head and tail references are updated to point to the new node.
            - If the queue is not empty, the current tail's next reference is updated to point to the new node,
                and the tail reference is updated to point to the new node.
            - The count of nodes in the queue is incremented by 1.
            
            Time Complexity: O(1)
        """

        # Empty Check. If empty -> Update Head. Else -> Update Current Tail's Next Reference
        if(self.is_empty()):
            self._head = node
        else: 
            # Update the current tail's next reference to point to the new node
            self._tail.set_next(node)

        self._tail = node
        self._count += 1
        
        return 

    def dequeue(self) -> LinearNode:

        """
            Removes and returns the head node of the queue. Raises an exception if the queue is empty.

            Has the following constraints:
            - The head reference is updated to point to the next node in the queue.
            - The count of nodes in the queue is decremented by 1.
            - If the queue becomes empty after the operation, the tail reference is also set to None.
            - Returns the node that was removed from the queue.

            Time Complexity: O(1)
        """

        # Empty Check. If empty -> Raise Exception
        if(self.is_empty()):
            raise Exception("Queue is empty. Cannot dequeue.")

        # Store a reference to the current head node
        node: LinearNode = self._head

        # Update head reference
        self._head = self._head.get_next()

        # Decrement the count
        self._count -= 1

        # Empty Check. If empty -> Update Tail
        if(self.is_empty()):
            self._tail = None

        # Return the dequeued node
        return node

    def first(self) -> LinearNode:

        """
            Returns the head node of the queue without removing it. Raises an exception if the queue is empty.

            Has the following constraints:
            - Returns the node that is currently at the head of the queue.
            - Queue can not be empty.
            - The head reference remains unchanged after the operation.

            Time Complexity: O(1)
        """
        # Empty Check. If empty -> Raise Exception
        if(self.is_empty()):
            raise Exception("Queue is empty. Cannot retrieve first element.")

        # Return the current head of the queue without removing it
        return self._head

    def is_empty(self) -> bool:
        """
            Returns True if the queue is empty, otherwise returns False.

            Time Complexity: O(1)
        """
        return self._head is None

    def size(self) -> int:

        """
            Returns the number of nodes currently in the queue.
            
            Time Complexity: O(1)
        """

        return self._count


    def to_string(self) -> str:

        """
            Returns a string representation of the queue, showing the elements from head to tail.
            
            Time Complexity: O(n), where n is the number of nodes in the queue.
        """

        curr: LinearNode = self._head
        elements = []

        while curr is not None:
            elements.append(str(curr.get_element()))
            curr = curr.get_next()

        return "Queue(head -> tail): " + " -> ".join(elements)

    

    