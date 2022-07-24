class Group(object):
    def __int__(self):
        self.id = None
        self.name = None
        self.members = []

    def setID(self,id):
        self.id = id

    def getID(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMembers(self, members):
        self.members = members

    def getMembers(self):
        return self.members
