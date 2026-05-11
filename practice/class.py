import random
from asyncio import constants


def max_min(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
      #  print(f"Current min {min}")
    return min

def getValues():
    list = random.sample(range(50,100), 10)
    print(list)
    result = max_min(list)
    print(f"value is {result}")

# def getValues():
#     list = random.sample(range(10), 5)
#     print(list)
#     print(list[2:])#Start at index 2
#     print(list[:3])#Stop at index 3
#     list.append(5)
#     list.append(6)
#     list.append(7)
#     list.append(8)
#     list_a = list[-1]
#     print(list_a)

getValues()

    #list in python= arrays in Java; a list is smtimes called a dynamic array because you can add values because they aren't declared like arrays

#exit when I get what im looking for; multiple return statements
class Product:
    # constructor
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def get_name(self):
        return self.product_name
    #getter gives you want you to see

    def set_name(self, name):
        self.product_name = name
        #A setter allows you to modify

    def get_price(self, price):
        return self.product_price

    def set_price(self, price):
        self.prouduct_price = price


#creating an object
#both parameters: ie name and product must be persenrt
p1 = Product(product_name = "Lenovo", product_price = 500)
print(p1.product_name)
print(p1.get_name())
p1.set_name("Tablet")
#set name modifies the output
print(p1.get_name())
#get name shows you the name

p2 = Product(product_name = "BOB", product_price= 45)
print(p2.product_name)

# rule of BigO
# rule1: Drop constants
# rule2:keep the biggest constants
# rule3:Nested loops multiply
# rule4:
#
#a list are difined with square brackets
#mutable:you can add or reduce elements
#tuples cannot be modified
#faster than lists
#person = ("Alice", 30, "Engineer")
#print(person[0])

def create_list():
    """Create a simple list"""
    numbers = [1, 2, 3, 4, 5]
    print("Created list:", numbers)
create_list()

def access_elements():
    """Access elements using index"""
    fruits = ["apple", "banana", "cherry"]
    print("First element:", fruits[0])
    print("Last element:", fruits[-1])
access_elements()

def modify_elements():
    """Modify elements in a list"""
    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)
    fruits[1] = "orange"
    print("Modified list:", fruits)
modify_elements()

def list_length():
    numbers = [1, 2, 3, 4, 5]
    numbers_of_elements = len(numbers)
    print("Number of elements:" , numbers_of_elements)
list_length()

def check_if_there():
    cars = ["Lambo","Bob", "Cherry"]
    print("is lambo in cars:", "lambo" in cars)
#check_if_there()
def count_and_index():
    numbers = (1,2,3)
    print("The numbers as Tupels: ", numbers)

    number_list = list(numbers)
    print("Tuple to list:", number_list)

    number_list.append(4)

    numbers_tuple = tuple(number_list)
    print("List back to tuple:", numbers_tuple)
count_and_index()

    #you can convert the tuple to a list and modify then convert back

    #nested or multi dimensional arrays

    #sets are unordered, to access we use "bob" in fruits

    #when deleting smth thats no in a set: {1,2,3} :remove= error, Discard= no error
    #sets remove
    #key that does not exist you add smth new to your dictionary
    #key that exists you modify

    #keys, values, keys and values

    #count how many times a value appearee within a given text
    #

def student_f1():
    students = ["Bob", "Yout", "Cherry", "Godi"]

    print("The students registered:", students)
    students.append("Brown")
    print("The students appended:", students)
    students.insert(3, "bob")
    print("The students inserted:", students)

    popped = students.pop()
    print("The students popped:", popped)
    print("The students removed:", students)
    students.reverse()
    print("The students reversed:", students)
    len(students)
    print(len(students))
student_f1()

def create_dict():
    student = {
        "name": "Bob",
        "age": 21,
        "hobby": "gooning"
    }
    print("pupil details", student)
    print("Name:", student["name"])
    print("age:", student.get("age"))

create_dict()

#
def funcA(n):
    if n > 0:
        print("A:", n)
        funcB(n - 1)

def funcB(n):
    if n > 0:
        print("B:", n)
        funcA(n-1)

funcA(3)
funcB(3)

def head_count(n):
    if n == 0:
        return
    head_count(n-1)
    print(n)
#the call is happening before the recursion
head_count(3)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
#two calls at the same time
print(fibonacci(5))

#recursion may have more readablilty
#stack , head recurssion, store local variables and passing parameters
#last in first out principle
#once D is called it goes back to C and back to B
#stack stays in your ram, once your device is switched off the data goes
#Push
#when stack is likely to exceed 1000
#large inpit but small opertaions is ayt: ie
#stack overflow: when there are too many function calls in  memory
#use the correct base case
#convert to Iteration
#


def bob_the_great():
    Students = {
        "name": "Bob",
        "age": 21,

    }

    Broski = ("chopped", "clapped", "mogged")

    Broski.count("chopped")

bob_the_great()

def recursion(n:int):
    if n < 0:
        return n
    #this is the base case

    print(n)
    return recursion(n-1)
#tail recursion because its being called at the very end
#it is direct recursionn because its calling itself within itself

recursion(5)

#indirect recursion
def a(n):
#    if n > 0:
#        print(f"Inside a {n}")
#        return b(n-1)

    if n > 1:
        return n
    else:
        print(f"Inside a{n}")
        return b(n-1)

def b(n):
    if n > 0:
        print(f"Inside b {n}")
        return a(n-1)

a(5)












