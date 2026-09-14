from abc import abstractmethod
from DSA.Node.LinearNode import LinearNode
from DSA.Collections.Lists.IList_ADT import IList_ADT

class IOrdered_List(IList_ADT):
    
    @abstractmethod
    def add(node: LinearNode) -> None:
        pass
