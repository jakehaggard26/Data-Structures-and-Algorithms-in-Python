from abc import ABC, abstractmethod

class INode(ABC):
    @abstractmethod
    def get_element(self):
        pass

    @abstractmethod
    def set_element(self, element):
        pass