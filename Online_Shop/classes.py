from abc import ABC, abstractmethod
from typing import Dict, Type
class ProductBase(ABC):
    product_number = 1
    object_list = None
    def __init__(self, initial_price,company, *args, **kwargs):
        self.name = self.get_name()
        self.initial_price = initial_price
        self.company = company
        self.product_number = self.get_number()
        self.store(self)
        super().__init__(*args, **kwargs)
    
    @classmethod
    def get_number(cls):
        cls.product_number +=1
        return cls.product_number
    
    @classmethod
    def store(cls, obj):
        if cls.object_list == None:
            cls.object_list = list()
        cls.object_list.append(obj)
    
    # @classmethod
    # def get_name(cls):
    #     return cls.__class__.__name__  
    @abstractmethod
    def get_name(self):
        pass

    @classmethod
    def product_count(cls):
        return len(cls.object_list)
    
    @property
    @abstractmethod
    def detail(self):
        base_info = f'product_number: {self.product_number}\tname: {self.name}\nprice: {self.price}$\ncompany: {self.company}\ncount_of_product_list: {self.product_count()}\n'
        return base_info
    
    @property
    def price(self):
        return self.initial_price + self.shipping
    
    @property
    @abstractmethod
    def shipping(self):
        pass

class Rug(ProductBase):
    def __init__(self, initial_price, company, shaneh, *args, **kwargs):
        self.shaneh = shaneh
        super().__init__(initial_price, company, *args, **kwargs)
    
    def get_name(self):
        return self.__class__.__name__ 

    @property
    def detail(self):
        base_info = super().detail
        return base_info + f'Rag_shaneh: {self.shaneh}'
    
    
    @property
    def shipping(self):
        shipping_price = 25
        return shipping_price

class Mobile(ProductBase):
    def __init__(self, initial_price, company, year, *args, **kwargs):
        self.year = year
        super().__init__(initial_price, company, *args, **kwargs)
    
    def get_name(self):
        return self.__class__.__name__ 
    
    @property
    def detail(self):
        base_info = super().detail
        return base_info + f'manufactor date: {self.year}'
    
    
    @property
    def shipping(self):
        shipping_price = 5
        return shipping_price
    
class GiftCard(ProductBase):
    def __init__(self, initial_price, company, max_price, *args, **kwargs):
        self.max_price = max_price
        super().__init__(initial_price, company, *args, **kwargs)

    def get_name(self):
        return self.__class__.__name__ 

    @property
    def detail(self):
        base_info = super().detail
        return base_info + f'max price: {self.max_price}'
    
    @property
    def price(self):
        return super().price + self.shipping
    
    @property
    def shipping(self):
        shipping_price = 0
        return shipping_price
    
    
class ProductFactory():
    _products: Dict[str, Type[ProductBase]] = {}
    
    @classmethod
    def register_product(cls, product_type: str, product_class: Type[ProductBase]):
        cls._products[product_type] = product_class  # _products['rug'] = Rug
    
    @classmethod
    def create_product(cls, product_type: str, **kwargs):
        if product_type not in cls._products:
            raise ValueError(f"Unknown product type: {product_type}")
        
        product_class = cls._products[product_type] # product_class = Rug (the class, not an instance)
        return product_class(**kwargs) # Creates Rug(**kwargs)