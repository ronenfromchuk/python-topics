# Creating Rectangles with width, height (3, 7) & (9, 12)

'''
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle = {(self.width * 2) + (self.height * 2)}'

_rectangle_one = Rectangle(3, 7)
print(_rectangle_one)

_rectangle_two = Rectangle(9, 12)
print(_rectangle_two)
'''

# targil:
# create 2 rectangles with width,
# height (3, 7) and (9, 12)
# print the 2 rectangles

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height

    def hekef(self):
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        return f'Rectangle (width: {self.width}, height: {self.height}, '+\
               f'area: {self.calc_area()})'

rec1 = Rectangle(3.2, 7.88)
print(rec1)
#print('area =',calc_area(rec1.width, rec1.height))
print('area =',rec1.calc_area(),', ' 'hekef =',rec1.hekef())
rec2 = Rectangle(9, 12)
print(rec2)
print(f'hekef of rec2 is: {rec2.hekef()}')