class Bill(object):
    def __int__(self):
        self.id = None
        self.groupId = None
        self.amount = None
        self.contibution = {}
        self.paidBy = {}

    def setID(self,id):
        self.id = id

    def getID(self):
        return self.id

    def setGroupId(self, groupId):
        self.groupId = groupId

    def getGroupId(self):
        return self.groupId

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setContribution(self, contribution):
        self.contibution = contribution

    def getContribution(self):
        return self.contibution

    def setPaidBy(self, paidBy):
        self.paidBy = paidBy

    def getPaidBy(self):
        return self.paidBy
