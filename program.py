from Person import Person

# Encapsulation

danny = Person(1, 'danny', 20)
suzi = Person(2, 'suzi', 22)
print(danny)
print(suzi)
print(danny.name) # public
danny.name = 'blabla'
print(danny.name)
# print(danny.age) # private # Error
# print(danny._Person__age) # you should not do that except on special
danny.set_age(-1)
print(danny.get_age())
danny.set_age(12)
print(danny.get_age())
#print(danny.__age)
#danny.danny = ''

# circle1.radius = -1
