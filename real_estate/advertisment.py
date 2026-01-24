from all_classes import *

class SellApartment(Basic, Sell, Apartment):

    def __str__(self):
        return f'{Sell.__str__(self)}{Apartment.__str__(self)}'

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
    def __str__(self):
        return f'{Sell.__str__(self)}{Land.__str__(self)}'