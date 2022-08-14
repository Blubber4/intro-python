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
