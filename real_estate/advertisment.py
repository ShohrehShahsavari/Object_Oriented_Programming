from all_classes import *

class SellApartment(Basic, Sell, Apartment):
    def __str__(self):
        return f"Class: {self.__class__.__name__}\tid: {self._id}\n" + \
               f"{Apartment.show_details(self)}\n{Sell.description(self)}\n" + \
                   f"total price: {self.total_price()}\ndiscount: {self.__get_discount()}\n"
    def total_price(self):
        return (self.price_per_meter * self.area) - self.__get_discount()
    def __get_discount(self):
        return self.discount / 100 

class RentApartment(Basic, Rent, Apartment):
        
    def __str__(self):
        return f'{Rent.__str__(self)}{Apartment.__str__(self)}'

class SellHouse(Basic, Sell, House):
    def __str__(self):
        return f'{Sell.__str__(self)}{House.__str__(self)}'

class RentHouse(Basic, Rent, House):
    
    def __str__(self):
        return f'{Rent.__str__(self)}{House.__str__(self)}'

class SellStore(Basic, Sell, Store):
    def __str__(self):
        return f'{Sell.__str__(self)}{Store.__str__(self)}'

class RentStore(Basic, Rent, Store):
    def __str__(self):
        return f'{Rent.__str__(self)}{Store.__str__(self)}'

class SellLand(Basic, Sell, Land):
    # def __init__(self, price_per_meter, discount, employee, exchangable=False, *args, **kwargs):
    #     Basic().__init__()
    #     Sell().__init__(price_per_meter, discount, employee, exchangable=False)
    #     Land().__init__(*args, **kwargs)
    def __str__(self):
        return f'{Sell.__str__(self)}{Land.__str__(self)}'