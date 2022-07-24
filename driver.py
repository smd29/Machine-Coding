import sys

sys.path.append(r"C:\Users\shrey\PycharmProjects\pythonProject\LLD")

from Splitwise.controllers.user_controller import UserController
from Splitwise.controllers.group_controller import GroupController
from Splitwise.controllers.bill_controller import BillController

from Splitwise.services.user_service import UserService
from Splitwise.services.group_service import GroupService
from Splitwise.services.bill_service import BillService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())


user1 = userController.addUser('User1', 'Shreyas')
user2 = userController.addUser('User2', 'Rohit')
user3 = userController.addUser('User3', 'Virat')
user4 = userController.addUser('User4', 'Bumrah')
user5 = userController.addUser('User5', 'Mahi Bhai')

members = [user1, user2, user3, user4, user5]
group1 = groupController.addGroup('Group1', 'Players', members)


paidBy = {'user1':200, 'user2':100, 'user3':40, 'user4':60, 'user5': 100}
contribution = {'user1':100, 'user2':100, 'user3':100, 'user4':100, 'user5': 100}

bill = billController.addBill('bill1', 'group1', 500, contribution,paidBy)

balance1 = billController.getUserBalance('user1')
print(balance1)
balance2 = billController.getUserBalance('user2')
print(balance2)
balance3 = billController.getUserBalance('user3')
print(balance3)
balance4 = billController.getUserBalance('user4')
print(balance4)
balance5 = billController.getUserBalance('user5')
print(balance5)