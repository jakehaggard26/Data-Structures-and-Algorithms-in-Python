from DSA.Collections.Lists.IList import IList
from DSA.Node.LinearNode import LinearNode
from abc import ABC, abstractmethod

class ICircular_List(IList):

    @abstractmethod
    def first() -> LinearNode:
        pass

    @abstractmethod
    def last() -> LinearNode:
        pass