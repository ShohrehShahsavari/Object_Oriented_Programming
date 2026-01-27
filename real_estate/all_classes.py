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
    
    # def __str__(self):
    #     return f"Maneger: {self._class.__name__}\tid: {self._class._id}"
        # return f"[Manager: {self._class.__name__}  id: {self._class._id}]"
    
    def search(self, **kwargs):
        results = list()
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    results.append(obj)
        return results
    


class Person(Basic):
    def __init__(self, FullName, Phone, Address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.FullName = FullName
        self.Phone = Phone
        self.Address = Address
    @abstractmethod
    def show_Info(self):
        return f'fullname: {self.FullName}\tphone: {self.Phone}'
        

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
    @abstractmethod
    def show_details(self):
        pass

    # def __str__(self):
    #     return f'================\nOwnerInfo:\n================\n {self.owner.__str__()}\n'

class Apartment(Estate, ABC):
    def __init__(self, owner, area, region, address,floor, rooms_num=None, has_parking=False, has_elevator=False, built_year=None, *args, **kwargs):
        super().__init__(owner, area, region, address, rooms_num, built_year, *args, **kwargs)
        self.floor = floor
        self.has_parking = has_parking
        self.has_elevator = has_elevator
    def show_details(self):
        return f'{self.__class__.__name__} info:\nOwner Info: {self.owner.show_Info()}\n'+f'area: {self.area}\tregion:{self.region}\taddress:{self.address}' 
  
    
    
class House(Estate, ABC):
    def __init__(self, owner, area, region, address, has_yard, has_floor, rooms_num=None, built_year=None, *args, **kwargs):
        super().__init__(owner, area, region, address, rooms_num, built_year, *args, **kwargs)
        self.has_yard = has_yard
        self.has_floor = has_floor
    def show_details(self):
        return f'{self.__class__.__name__} info:\nOwner Info: {self.owner.show_Info()}\n'+f'area: {self.area}\tregion:{self.region}\taddress:{self.address}' 
  
        
class Store(Estate, ABC):
    def show_details(self):
        return f'{self.__class__.__name__} info:\nOwner Info: {self.owner.show_Info()}\n'+f'area: {self.area}\tregion:{self.region}\taddress:{self.address}' 
  

    # def __str__(self):
    #     return f'StoreInfo:\n================\nArea: {self.area}\t Address Of Land: {self.address}\n' + super().__str__() 

class Land(Estate, ABC):
    def __init__(self, owner, area, region, address, has_permition=False, rooms_num=None, *args, **kwargs):
        super().__init__(owner, area, region, address,rooms_num=None, *args, **kwargs)
        self.has_permition = has_permition
    def show_details(self):
        return f'{self.__class__.__name__} info:\nOwner Info: {self.owner.show_Info()}\n'+f'area: {self.area}\tregion:{self.region}\taddress:{self.address}' 
  
    # def __str__(self):
    #     return f'LandInfo:\n================\nArea: {self.area}\t Address Of House: {self.address}\thas_permition: {self.has_permition}\n' + super().__str__() 
    
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
        return f'{self.__class__.__name__} info:\n {self.employee.show_Info()}\n'
    # def total_price(self):
    #     return (self.price_per_meter *) - self.__get_discount()
    # def __get_discount(self):
    #     return self.discount / 100  
    
class Rent(ABC):
    def __init__(self, initial_price, employee, monthly_price, discount, flexible=False, *args, **kwargs):
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
    # def __str__(self):
    #     return f'Rent Description:\n<<<<<<<<<<<<<<<<\n================\n<<<<<<<<<<<<<<<<\nAdvisor Info: {self.employee.__str__()}\n================\n'
