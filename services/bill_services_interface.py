from abc import abstractmethod,ABC

class BillServiceInterface(ABC):
    @abstractmethod
    def addBill(self,id,groupId,amount,contribution,paidBy):
        pass
