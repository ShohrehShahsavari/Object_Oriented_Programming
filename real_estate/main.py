from random import choice
from all_classes import *
import numpy as np
from advertisment import *

# e1 = Employee('e1', '912000', 'e1e1e1e1e', 20)
# e2 = Employee('e2', '0918000', 'e2e2e2e2', 30)

# owner1 = Owner('owner1', '0901000', 's1s1s', 123)

# a1 = Apartment(owner1, 85, 'a1', 'a1a1a1', 5, True, True, 2, 1395)


# sale1 = Sales(a1, 3, 5, e1)
# mortgage1= Mortgages(a1, 2, e2, 100, 0)

# # print(sale1.total_price())
# # print(mortgage1.total_price())

# print(Mortgages._object_list)
# # print(Employee._object_list)
# # print(Sales._object_list)
# # print(Owner._object_list)
# # print(sale1)
name = ["ali", "mohammad", 'reza', 'sara', "hasan", 'sanaz', 'nima', 'zahra']
family = ["alavi", "mohammadi", 'rezai', 'saravi', "hasani"]
phones = ["0901123123", "0902123123", '0903123123', '0904123123', "0905123123", "0906123123", "0907123123", '0908123123', '0909123123', "09123123123"]
address = ['Tehran', 'Shiraz', 'Semnan', 'Rasht', 'Esfahan', 'Ahvaz']

employees = []
owners = []
for phone in phones:
    employees.append(Employee(f'{choice(name)} {choice(family)}', phone, choice(address), np.random.randint(20, 50)))
    owners.append(Owner(f'{choice(name)} {choice(family)}', phone, choice(address), np.random.randint(1000, 5000)))

# if __name__ == "__main__":

p1 = SellApartment(price_per_meter=3, discount=0.05, employee=employees[0], exchangable=False, owner=owners[1], area=80, region='R1', address= choice(address),floor=5, has_parking=False, has_elevator=True, rooms_num=2, built_year=1394)
# print(p1)
# print(SellApartment._object_list)
# for obj in SellApartment._object_list:
#     print(obj)


file2 = SellHouse(price_per_meter=3, discount=0.05, employee=employees[1], exchangable=True, owner=owners[2], area=85, region='R2', address= choice(address), has_yard=True, has_floor=False, rooms_num=1, built_year=None)
# print(file2)

file3 = RentHouse(initial_price=10, employee=employees[2], monthly_price=5.5, discount=0.01, owner=owners[2], area=120, region='R2', address= choice(address), has_yard=True, has_floor=False, rooms_num=3, built_year=1400)
print(file3)