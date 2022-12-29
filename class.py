#instance methods
#class methods
#static methods


class car:
    dummyvar = "dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.dummyvar)

carObj = car()
carObj.sample_car_instance_method("Hello again!")

carObj2 = car()
carObj2.sample_car_instance_method(2)

#class

print(__name__)


#
class computer:
    def config(self):


class mobile:
    def config(self):
        print("processor, ram,rom")

c=mobile()
print(type(c))


from calc import *
a=9
b=8
c=add(a,b)
print(c)