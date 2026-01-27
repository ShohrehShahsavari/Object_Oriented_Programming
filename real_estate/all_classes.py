from abc import ABC, abstractclassmethod, abstractmethod
import csv

class Basic(ABC):
    _id=1000
    object_list = None
    manager = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = self.get_id()
        self.store(self)
        self.get_manager()
        
    @classmethod
    def get_id(cls):
        cls._id += 1
        return cls._id
        
    @classmethod
    def store(cls, obj):
        if cls.object_list == None:
            cls.object_list = list()
        cls.object_list.append(obj)

    @classmethod
    def get_manager(cls):
        if cls.manager == None:
            cls.manager = Manager(cls)
    

class Manager():
    def __init__(self, _class=None):
        self._class = _class
        
    def search(self, **kwargs):
        results = list()
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    results.append(obj)
        return results
    def count(self):
        return len(self._class.object_list)

class Person(Basic):
    def __init__(self, FullName, Phone, Address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.FullName = FullName
        self.Phone = Phone
        self.Address = Address
        
    def show_Info(self):
        return f'{self.FullName}\tphone: {self.Phone}'
        

class Employee(Person):
    def __init__(self, FullName, Phone, Address, age, *args, **kwargs):
        Person.__init__(self, FullName, Phone, Address, *args, **kwargs)
        self.age = age

    
class Owner(Person):
    def __init__(self, FullName, Phone, Address, identity, *args, **kwargs):
        Person.__init__(self, FullName, Phone, Address, *args, **kwargs)
        self.identity = identity

class Estate(ABC):
    def __init__(self, owner, area, region, address, rooms_num=None, built_year=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner
        self.area = area
        self.rooms_num = rooms_num
        self.built_year = built_year
        self.region = region
        self.address = address

    def show_details(self):
        return f'Owner Info: {self.owner.show_Info()}\n'+f'area: {self.area}\tregion:{self.region}\taddress:{self.address}' 


class Apartment(Estate, ABC):
    def __init__(self, owner, area, region, address,floor, rooms_num=None, has_parking=False, has_elevator=False, built_year=None, *args, **kwargs):
        super().__init__(owner, area, region, address, rooms_num, built_year, *args, **kwargs)
        self.floor = floor
        self.has_parking = has_parking
        self.has_elevator = has_elevator

    
    
class House(Estate, ABC):
    def __init__(self, owner, area, region, address, has_yard, has_floor, rooms_num=None, built_year=None, *args, **kwargs):
        super().__init__(owner, area, region, address, rooms_num, built_year, *args, **kwargs)
        self.has_yard = has_yard
        self.has_floor = has_floor

        
class Store(Estate, ABC):
    pass
 

class Land(Estate, ABC):
    def __init__(self, owner, area, region, address, has_permition=False, rooms_num=None, *args, **kwargs):
        super().__init__(owner, area, region, address,rooms_num=None, *args, **kwargs)
        self.has_permition = has_permition

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
    def description(self):
        return f'Advisor: {self.employee.show_Info()}'
 
    
class Rent(ABC):
    def __init__(self, initial_price, employee, monthly_price, discount, flexible=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.flexible = flexible
        self.discount = discount
        self.employee = employee
    def description(self):
        return f'Advisor: {self.employee.show_Info()}'