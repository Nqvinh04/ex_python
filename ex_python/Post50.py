'''
Định nghĩa một class có tên là Vietnam, với static method
là printNationality
'''
class Vietnam(object):
    @staticmethod
    def printNationality():
        print("Vietnam")
VN = Vietnam()
VN.printNationality()
Vietnam.printNationality()
