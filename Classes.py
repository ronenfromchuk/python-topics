#Classes

class Person():
    def run(self):
        pass
    def jump(self):
        pass
    def work(self):
        pass
    pass

rf = Person()
rf.__dict__['id'] = 100 #rf.id = 100 --> same same
rf.__dict__['fname'] = 'Ronen'
rf.__dict__['lname'] = 'Fromchuk'
rf.__dict__['address'] = 'Ashkelon'
rf.__dict__['phone number'] = 1234567
print(rf.id)
print(rf.__dict__)

cr = Person()
cr.id = 10                  #
cr.fname = 'Cristiano'      #
cr.lname = 'Ronaldo'        # ---> cr.(same)
cr.address = 'Manchester'   #
cr.phone_number = 7777777   #
print(cr.__dict__)

_people = [rf, cr]
# id == 10?
_people_dict = {rf.id: rf, cr.id: cr}
print(_people_dict[100].__dict__)