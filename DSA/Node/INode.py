from abc import ABC, abstractmethod

class INode(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass