print("Hello python")

name = "John"
num = 25
balance = 456.67
flag = True

print(type(name))
print(type(num))
print(type(balance))
print(type(flag))

print("using range")
for i in range(2,18, 2):
    print(i)

    #(starting from, range, skip certain number)
# for (int i = 0; i<10; i++)
# {
# Sout.print(i);
# }

# print("using for loop")
# items = [1,2,3,4,5,6,7,8]
# for item in items:
#     print(item)

def getValues():
    for i in range(18):
        if i == 17:
            print (i)


print(getValues())

def func(a, b= 10):
    pass
#parameters without default values must appear before the values with defaulf values
    #(a= 10, b) is wrong

def greet(name="Guest", age = 18):

    print(f"Hello {name}, age {age}")

greet(name= "Anna", age=30)

def calc(a,b):
    return a+b,a-b

sum,diff = calc(10,5)
print(sum,diff)

def calculate_statistics(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count!=0 else 0
    return total, count, average

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
total, count, average = calculate_statistics(numbers)
print(f"total: {total}, count: {count}, average: {average}")

#keyword arguements need to be ordered
#dictornariy
#none Kwargs dont need
# tupules or the order

#docstring; multiple line comments
#model in Django = table in your database

def def__init__(self, brand, color):
    pass


#def Car:
 #   def__init__(self,brand,color)
  #     self.brand = brand
   #    self.color = color

class Car:
    def drive(self):
        return "Car is Driving"

c=Car()
print(c.drive())


my_car = Car("Toyota", "Red")
print(my_car.brand)

#we use constructors for initialization
#constructor- method that has the same name as your class name
# this in java is the same as self in Python

class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
print(Dog().speak()) #WOOF!

#INHERITANCE: Is-A relationship
#COMPOSITION: Has-A relationship

#class and static methods, statics does not need a method, class works at class level
#static method; belongs to a class not necessarily a method
# dont take self or cls as the first parameter
# can be called through an object although you dont need to

class MathOperation:
    @staticmethod
    def add(a, b):
        return a+b
    @staticmethod
    def subtract(a, b):
        return a-b

print(MathOperation.add(1, 2))
print(MathOperation.subtract(1, 2))

#Abstract classes= Interface in Java











