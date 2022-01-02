from OutOfSalmonException import *
from SomethingWentWrongException import *
import sys

class KitchenSupervisor:
    def __init__(self, name, cook):
        self.name = name
        self.cook = cook

    def process_order(self, order_name):
        print(f'KitchenSupervisor {self.name} passing order of {order_name} to cook')

        try:
            d = self.cook.make_dish(order_name)
            return d
        except OutOfSalmonException as e:
            #return 'get voucher of 500 shekel'
            # buy new salmon ASAP
            tb = sys.exc_info()[2]
            raise SomethingWentWrongException(e).with_traceback(tb)

        d = self.cook.make_dish(order_name)
        return d