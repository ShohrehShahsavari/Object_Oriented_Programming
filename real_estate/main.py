from random import choice
from all_classes import *
import numpy as np
from advertisment import *
from sample import *

class Handler():
    advertisment_dic= {
    1: SellApartment, 2: RentApartment,
    3: SellHouse, 4: RentHouse,
    5: SellStore, 6: RentStore,
    7: SellLand}
    
    SWITCHES = {
        1: 'viwe_archives', 2: 'add_New_file',
        3: 'update_file', 4: 'search_file',
        5: 'Exit'}
    
    def viwe_archives(self):
        for adv in self.advertisment_dic.values():
            print(adv, adv.manager.count())
            for obj in adv.object_list:
                print(obj)
                print("#"*50)
    
    def add_New_file(self):
        pass
    
    def update_file(self):
        pass
    def search_file(self):
        key = input('search based on(area, region, price_per_meter): ').strip().lower()
        value_input = input('enter value:  ').strip()
        value = self.smart_convert(value_input)
        print(f"Searching for {key} = {value}")
        print('#'*50)
        
        for adv in self.advertisment_dic.values():
            print(adv, adv.manager.search(**{key: value}))
            

    
    def Exit(self):
        print("Goodby")
    
    def smart_convert(self, value):
        """Smart conversion of input values"""
        if value.lower() in ['true', 'yes', 'y', '1']:
            return True
        elif value.lower() in ['false', 'no', 'n', '0']:
            return False
        
        try:
            # Try int first
            return int(value)
        except ValueError:
            try:
                # Try float
                return float(value)
            except ValueError:
                # Return as string
                return value
    
    def run(self):
        print("Welcome to real estate Menu:")
        print('1. viwe_archives')
        print('2. add_New_file')
        print('3. update_file')
        print('4. search_file')
        print('5. Exit')
        
        user_input = int(input("Enter your choice (1, 2, 3, 4, 5): ").strip())
        switche = self.SWITCHES[user_input]
        # switche = self.SWITCHES.get(user_input, None)

        if switche is None:
            print('Invalid Input!')
            self.run()
        choice = getattr(self, switche, None)
        choice()
        
        



if __name__ == "__main__":

    handler = Handler()
    handler.run()

    