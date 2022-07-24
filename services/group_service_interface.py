from abc import abstractmethod, ABC

class GroupServiceInterface(ABC):
    @abstractmethod
    def addGroup(self,id,name,members):
        pass