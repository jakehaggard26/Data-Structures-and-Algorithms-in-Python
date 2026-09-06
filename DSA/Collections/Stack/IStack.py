from abc import ABC, abstractmethod
from DSA.Node.Node import Node

class IStack(ABC):
    @abstractmethod
    def push(self, node: Node):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def to_string(self):
        pass