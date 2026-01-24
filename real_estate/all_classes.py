from abc import ABC, abstractclassmethod

class Basic(ABC):
    _id=1000
    _object_list = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = self.get_id()
        self.store(self)
        
    @classmethod
    def get_id(cls):
        cls._id += 1
        return cls._id
        
    @classmethod
    def store(cls, obj):
        if cls._object_list == None:
            cls._object_list = list()
        cls._object_list.append(obj)
        

class Person(ABC):
    def __init__(self, FullName, Phone, Address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.FullName = FullName
        self.Phone = Phone
        self.Address = Address
    def __str__(self):
        return f'Name: {self.FullName}\tPhone: {self.Phone}\tAddress: {self.Address}'
    
        

class Employee(Person, Basic):
    def __init__(self, FullName, Phone, Address, age, *args, **kwargs):
        Person.__init__(self, FullName, Phone, Address, *args, **kwargs)
        self.age = age
    def __str__(self):
        return  f'Id_Number: {self._id}' + super().__str__() + f'\tAge: {self.age}'    

class Owner(Person, Basic):
    def __init__(self, FullName, Phone, Address, identity, *args, **kwargs):
        Person.__init__(self, FullName, Phone, Address, *args, **kwargs)
        self.identity = identity
    def __str__(self):
        return f'Id_Number: {self._id}\t' + super().__str__()  + f'\tIdentity_Number: {self.identity}'


class Estate(ABC):
    def __init__(self, owner, area, region, address, rooms_num = None, built_year=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner
        self.area = area
        self.rooms_num = rooms_num
        self.built_year = built_year
        self.region = region
        self.address = address
    def __str__(self):
        return f'OwnerInfo:\n {self.owner.__str__()}\n'

class Apartment(Estate, ABC):
    def __init__(self, owner, area, region, address,floor, has_parking=False, has_elevator=False, rooms_num=None, built_year=None, *args, **kwargs):
        super().__init__(owner, area, region, address, rooms_num, built_year, *args, **kwargs)
        self.floor = floor
        self.has_parking = has_parking
        self.has_elevator = has_elevator
    def __str__(self):
        return f'ApartmentInfo:\nArea: {self.area}\t Address of Apartment: {self.address}\t has_elevator: {self.has_elevator}\n' + super().__str__()

class House(Estate, ABC):
    def __init__(self, owner, area, region, address, has_yard, has_floor, rooms_num=None, built_year=None, *args, **kwargs):
        super().__init__(owner, area, region, address, rooms_num, built_year, *args, **kwargs)
        self.has_yard = has_yard
        self.has_floor = has_floor
    def __str__(self):
        return f'HousInfo:\nArea: {self.area}\t Address Of House: {self.address}\thas_yard: {self.has_yard}\n' + super().__str__() 

class Store(Estate, ABC):

    def __str__(self):
        return f'HousInfo:\nArea: {self.area}\t Address Of House: {self.address}\n' + super().__str__() 

class Land(Estate, ABC):
    def __init__(self, owner, area, region, address, has_permition, rooms_num=None, built_year=None, *args, **kwargs):
        super().__init__(owner, area, region, address, rooms_num, built_year, *args, **kwargs)
        self.has_permition = has_permition
    def __str__(self):
        return f'HousInfo:\nArea: {self.area}\t Address Of House: {self.address}\thas_permition: {self.has_permition}\n' + super().__str__() 
    
class Usage():
    #Commercial, Administrative,Residential
    pass
class Sell(ABC):
    def __init__(self, price_per_meter, discount, employee, exchangable=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price_per_meter = price_per_meter
        self.discount = discount
        self.exchangable = exchangable
        self.employee = employee
    def __str__(self):
        return f'Sell Description:\n================\nSell Advisor Info: {self.employee.__str__()}\n================\n'

class Rent(ABC):
    def __init__(self, property, initial_price, employee, monthly_price, discount, flexible=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.flexible = flexible
        self.discount = discount
        self.employee = employee
    # def total_price(self):
    #     return (self.initial_price) - self.__get_discount()
    # def __get_discount(self):
    #     return self.discount / 100
    def __str__(self):
        return f'Rent Description:\n================\nSell Advisor Info: {self.employee.__str__()}\n================\n'
