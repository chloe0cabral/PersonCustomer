import os
print(os.environ["PATH"])
import datetime
now = datetime.datetime.now()
print(now.strftime("%m/%d/%y %H:%M:%S"), "\n")

class Person:
    def __init__(self, name, address, phoneNum):
        self.name = name
        self.address = address
        self. phoneNum = phoneNum

class Customer(Person):
    def __init__(self, name, address, phoneNum, cusNum, mail):
        Person.__init__(self, name, address, phoneNum)
        self.cusNum = cusNum
        self.mail = mail

    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getPhoneNum(self):
        return self.phoneNum
    def getCusNum(self):
        return self.cusNum
    def getMail(self):
        if self.mail == "No":
            return "False"
        else:
            return "True"

def main():

    name = str(input("Enter the name: "))
    address = str(input("Enter the address: "))
    phoneNum = str(input("Enter the phone number: "))
    cusNum = str(input("Enter the customer number: "))
    mail = str(input("Does the customer wish to be on the mailing list?(Yes/No) "))

    cus1 = Customer(name, address, phoneNum, cusNum, mail)

    print("Customer Information: ")
    print("Name: " + cus1.getName())
    print("Address: " + cus1.getAddress())
    print("Phone Number: " + cus1.getPhoneNum())
    print("Customer Number: " + cus1.getCusNum())
    print("On Mailing List: " + cus1.getMail())

main()
