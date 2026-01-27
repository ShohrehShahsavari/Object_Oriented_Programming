from all_classes import *

class SellApartment(Basic, Sell, Apartment):
    def __str__(self):
        return f"Class: {self.__class__.__name__}\tid: {self._id}\n" + \
               f"{Apartment.show_details(self)}\n{Sell.description(self)}\n" + \
                   f"total price: {self.total_price()}\ndiscount amount: {self.__get_discount()}\n"
    def total_price(self):
        return (self.price_per_meter * self.area) - self.__get_discount()
    def __get_discount(self):
        return (self.price_per_meter * self.area) * self.discount 

class RentApartment(Basic, Rent, Apartment):
    def __str__(self):
        return f"Class: {self.__class__.__name__}\tid: {self._id}\n" + \
               f"{Apartment.show_details(self)}\n{Rent.description(self)}\n" + \
                   f"Initial price: {self.initial_price}\tMonthly price: {self.monthly_price}\ndiscount %: {self.__get_discount()}\n"
    def __get_discount(self):
        return self.discount * 100

class SellHouse(Basic, Sell, House):
    def __str__(self):
        return f"Class: {self.__class__.__name__}\tid: {self._id}\n" + \
               f"{House.show_details(self)}\n{Sell.description(self)}\n" + \
                   f"total price: {self.total_price()}\ndiscount amount: {self.__get_discount()}\n"
    def total_price(self):
        return (self.price_per_meter * self.area) - self.__get_discount()
    def __get_discount(self):
        return (self.price_per_meter * self.area) * self.discount

class RentHouse(Basic, Rent, House):  
    def __str__(self):
        return f"Class: {self.__class__.__name__}\tid: {self._id}\n" + \
               f"{House.show_details(self)}\n{Rent.description(self)}\n" + \
                   f"Initial price: {self.initial_price}\tMonthly price: {self.monthly_price}\ndiscount %: {self.__get_discount()}\n"
    def __get_discount(self):
        return self.discount * 100

class SellStore(Basic, Sell, Store):
    def __str__(self):
        return f"Class: {self.__class__.__name__}\tid: {self._id}\n" + \
               f"{Store.show_details(self)}\n{Sell.description(self)}\n" + \
                   f"total price: {self.total_price()}\ndiscount amount: {self.__get_discount()}\n"
    def total_price(self):
        return (self.price_per_meter * self.area) - self.__get_discount()
    def __get_discount(self):
        return (self.price_per_meter * self.area) * self.discount

class RentStore(Basic, Rent, Store):
    def __str__(self):
        return f"Class: {self.__class__.__name__}\tid: {self._id}\n" + \
               f"{Store.show_details(self)}\n{Rent.description(self)}\n" + \
                   f"Initial price: {self.initial_price}\tMonthly price: {self.monthly_price}\ndiscount %: {self.__get_discount()}\n"
    def __get_discount(self):
        return self.discount * 100

class SellLand(Basic, Sell, Land):
    def __str__(self):
        return f"Class: {self.__class__.__name__}\tid: {self._id}\n" + \
               f"{Land.show_details(self)}\n{Sell.description(self)}\n" + \
                   f"total price: {self.total_price()}\ndiscount amount: {self.__get_discount()}\thas_permition: {self.has_permition}\n"
    def total_price(self):
        return (self.price_per_meter * self.area) - self.__get_discount()
    def __get_discount(self):
        return (self.price_per_meter * self.area) * self.discount