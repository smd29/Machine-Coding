from Splitwise.services.bill_services_interface import BillServiceInterface
from Splitwise.models.bills import Bill

class BillService(BillServiceInterface):
    billDetails = {}
    def addBill(self,id,groupId,amount,contribution,paidBy):
        bill = Bill()
        bill.setID(id)
        bill.setGroupId(groupId)
        bill.setAmount(amount)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        self.__class__.billDetails[id] = bill
        return bill
    