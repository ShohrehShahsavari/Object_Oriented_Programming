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

file1 = SellApartment(price_per_meter=3, discount=0.05, employee=employees[0], exchangable=False, owner=owners[1], area=80, region='R1', address= choice(address),floor=5, has_parking=False, has_elevator=True, rooms_num=2, built_year=1394)
file2 = SellHouse(price_per_meter=5, discount=0.0, employee=employees[1], exchangable=True, owner=owners[2], area=120, region='R3', address= choice(address), has_yard=True, has_floor=False, rooms_num=3, built_year=1396)
file3 = SellStore(price_per_meter=36, discount=0.01, employee=employees[2], exchangable=True, owner=owners[0], area=12, region='R2', address= choice(address), rooms_num=None, built_year=1356)
file4 = SellLand(price_per_meter=1.5, discount=0.02, employee=employees[1], exchangable=True, owner=owners[0], area=200, region='R1', address= choice(address), rooms_num=None, built_year=None, has_permition=False)

file5 = RentApartment(initial_price=10, employee=choice(employees), monthly_price=7.5, discount=0.0, flexible=False , owner=choice(owners), area=95, region='R4', address= choice(address),floor=2, has_parking=True, has_elevator=True, rooms_num=3, built_year=1399)
file6 = RentHouse(initial_price=35, employee=choice(employees), monthly_price=6, discount=0.002, flexible=False, owner=choice(owners), area=110, region='R0', address= choice(address), has_yard=True, has_floor=False, rooms_num=2, built_year=1402)
file7 = RentStore(initial_price=120, employee=choice(employees), monthly_price=15, discount=0.0, flexible=True, owner=choice(owners), area=10, region='R0', address= choice(address), rooms_num=None, built_year=1400)                                                                      
    
# print(file4)
    
# for obj in RentHouse.object_list:
#     print(obj)
    
# list1= SellApartment.manager.search(area=80)
# list1= SellHouse.manager.search(region="R3")
# list1= SellHouse.manager.search(region="R3")
# for obj in list1:
#     print(obj)