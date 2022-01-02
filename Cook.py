
from OutOfSalmonException import *

class Cook:

    salmon = 1

    def __init__(self, name):
        self.name = name

    def make_dish(self, order_name):
        print(f'Cook {self.name} making order of {order_name}')
        if order_name.upper() == 'sunset'.upper():
            if Cook.salmon > 0:
                Cook.salmon = Cook.salmon - 1
            else:
                #return f'{order_name} with more carrot'
                raise OutOfSalmonException(order_name)
        return f'{order_name} is ready'