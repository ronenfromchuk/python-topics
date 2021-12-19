def f1():
    print('hello')

def f2(_func):
    _func()

def calc(_func):
    x = int(input('enter number: '))
    y = int(input('enter number: '))
    print(_func(x, y))

f2( f1 )
f2( lambda : print('hello') )
#calc( lambda x,y: x + y)
calc( lambda x,y: x * y)
