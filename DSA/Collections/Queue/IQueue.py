from abc import ABC, abstractmethod
from DSA.Node.Node import Node

class IQueue(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def enqueue(self, node: Node):
        pass

    @abstractmethod
    def dequeue(self) -> Node:
        pass

    @abstractmethod
    def peek(self) -> Node:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass