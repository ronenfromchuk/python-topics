
from Cook import *
from KitchenSupervisor import *
from Waiter import *
from OutOfSalmonException import *

print('welcome to the restaurant')

c = Cook('eyal ben shany')
s = KitchenSupervisor('ronny', c)
w = Waiter('danny', s)

try:
    print(w.get_order('sunset'))
    print(w.get_order('sunset'))
except SomethingWentWrongException as e:
    print(e)
'''
try:
    print(w.get_order('sunset'))
    print(w.get_order('sunset'))
except OutOfSalmonException as e:
    print('i go somewhere else')
'''









