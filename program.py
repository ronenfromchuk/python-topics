from Circle import Circle

print(Circle.pie)
c1 = Circle(9.5)
print(c1.getArea())

Circle.pie = 4.01
print(c1.getArea())

# c1.printPieWithStars()
Circle.printPieWithStars()

_lst = []
for i in range(100_000):
    _lst.append(Circle(i))
