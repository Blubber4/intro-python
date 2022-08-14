# classes, saved as test4.py:
class Person:
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

class Customer(Person):
    def __init__(self, name, address, phone, id, willing):
        Person.__init__(self, name, address, phone)
        self.__id = id
        self.__willing = willing
    def get_id(self):
        return self.__id
    def get_willing(self):
        return self.__willing

    def set_id(self, id):
        self.__id = id
    def set_willing(self, willing):
        self.__willing = willing

#main file:
import test4
def main():
    aPerson = test4.Person('Jack Smith', "1000 University Dr.", '(713) 111-1111')
    aCustomer = test4.Customer("Danny Baker", '1111 College Main', '(281) 222-2222', '1010', False)

    print('Name: ', aPerson.get_name())
    print('Address: ', aPerson.get_address())
    print('Phone: ', aPerson.get_phone())

    print('\n\nName: ', aCustomer.get_name())
    print('Address: ', aCustomer.get_address())
    print('Phone: ', aCustomer.get_phone())
    print('Customer #: ', aCustomer.get_id())
    print('Willing contact: ', aCustomer.get_willing())

main()

'''output:
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======================== RESTART: D:/python/final.py ========================
Name:  Jack Smith
Address:  1000 University Dr.
Phone:  (713) 111-1111


Name:  Danny Baker
Address:  1111 College Main
Phone:  (281) 222-2222
Customer #:  1010
Willing contact:  False
>>> 
'''
