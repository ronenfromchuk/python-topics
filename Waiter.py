from OutOfSalmonException import *

class Waiter:
    def __init__(self, name, kitchen_sup):
        self.name = name
        self.kitchen_sup = kitchen_sup

    def get_order(self, order_name):
        print(f'Waiter {self.name} passing order of {order_name} to kitchen_sup')
        '''
        try:
            d = self.kitchen_sup.process_order(order_name)
        except OutOfSalmonException as e:
            d = self.kitchen_sup.process_order(f'{order_name} with tuna')
        d = self.kitchen_sup.process_order(order_name)
        return d
        '''

        d = self.kitchen_sup.process_order(order_name)
        return d