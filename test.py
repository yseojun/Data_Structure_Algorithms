from time import time
import random

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        self._balance -= amount

class Market:
    def __init__(self, name, sales):
        self._name = name
        self._sales = sales
    
    def set_item(self, item, price):
        self._item = item
        self._price = price
    
    def sale_item(self, item):
        self._quantity -= 1
    
    def get_item_info(self, item_name):
        for x in self:
            if self._item == item_name:
                print("Itme name : ")
                print(item_name)
                print("Itme  : ")
                print(item_name)
    
    def get_sale(self):
        return self._slaes
        
if __name__ == '__main__':
    my_list = []
    start_time = time()
    for i in range(0, 1000):
        my_list.append(random.randint(0, 10000))
    # wallet = []
    # wallet.append(
    #     CreditCard('John Hownam', 'California Savings', '5391 0375 9387 5309', 2500))
    # wallet.append(
    #     CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    # wallet.append(
    #     CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))
    
    # market = []
    
    # for val in range(1, 17):
    #     wallet[0].charge(val)
    #     wallet[1].charge(2*val)
    #     wallet[2].charge(3*val)
    
    # for c in range(3):
    #     print('Customer = ', wallet[c].get_customer())
    #     print('Bank = ', wallet[c].get_bank())
    #     print('Limit = ', wallet[c].get_limit())
    #     print('Balance = ', wallet[c].get_balance())
    #     while wallet[c].get_balance() > 100:
    #         print('Customer = ', wallet[c].get_customer())
    #         print('New balance =', wallet[c].get_balance())
    #     print()
    end_time = time()
    run_time = end_time - start_time
    print(run_time)