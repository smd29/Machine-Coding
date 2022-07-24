class UserController(object):
    def __init__(self,userService):
        self.userService = userService
    #this is like API
    def addUser(self,id,name):
        return self.userService.addUser(id,name)
