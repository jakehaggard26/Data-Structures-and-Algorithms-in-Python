from abc import ABC, abstractmethod
from DSA.Node.Node import Node

class IList(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def first(self) -> Node:
        pass

    @abstractmethod
    def last(self) -> Node:
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

    @abstractmethod
    def contains(self, node: Node) -> bool:
        pass

    @abstractmethod
    def remove(self, node: Node) -> Node:
        pass

    @abstractmethod
    def remove_first(self) -> Node:
        pass

    @abstractmethod
    def remove_last(self) -> Node:
        pass