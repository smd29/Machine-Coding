from abc import abstractmethod, ABC

class UserServiceInterface(ABC):
    @abstractmethod
    def addUser(self,id,name):
        pass
