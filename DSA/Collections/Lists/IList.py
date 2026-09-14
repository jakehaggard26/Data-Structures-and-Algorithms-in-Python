from abc import ABC, abstractmethod
from DSA.Node.LinearNode import LinearNode
from DSA.Collections.Lists.IList_ADT import IList_ADT

class IList(IList_ADT):

    @abstractmethod
    def __init__():
        pass

    @abstractmethod
    def add_to_back(self, node: LinearNode) -> LinearNode:

        pass


    @abstractmethod
    def add_to_front(self, node: LinearNode) -> None:

        pass


    @abstractmethod
    def add_after(self, target: LinearNode, node: LinearNode) -> None:

        pass
