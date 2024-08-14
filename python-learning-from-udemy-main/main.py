
# 1. Variables and Multiple Assignment
name = "Avi"
name , age = "Bahodir" , 23 

print(name, age)

# 2. Arithmetic Operators and Strings

firstInt, SecondInt = 1 , 2

# Arithmetic operators:
# + - * / %

print(firstInt % SecondInt)

# String

sent1 = "Today is a summer"
print(sent1)

firstName = "Avi"
lastName = "Hello"
print(firstName + " " + lastName)

print((lastName + " ") * 10)

sent = "Bahodir"
# from 0 to 2 ( without 3 )
print(sent[0:3])


# 3. Placeholders in Strings

# %s is for strings

name = "Jack"
print(name + " is 15 y.o.")

sentence = "%s is 15 years old "

print(sentence % name)


sentence = "%s %s is 15 years old "

print(sentence % ("Barack", "Obama"))

# %d is for integers

number = "%d hello"

print(number % 23)

description = "%s is %d years old"

print(description % ("Bahodir", 16))

# format strings

print(f'Hello {name}')


# 4. H/W 1



# 5. Introduction to Lists

subjectsList = ['math', 'PI', 'English']

# index-0 or zero index

print(subjectsList[0])

# indexes

print(subjectsList[0])


subjectsList = ['math', 'PI', 'English']

print(subjectsList[0:2])


# adding to list

subjectsList.append('German')

print(subjectsList)

subjectsList[0] = "Geometry"

print(subjectsList)

# deleting to list

del subjectsList[3]

print(subjectsList)

print(len(subjectsList))

# adding one list to another

subjectsList2 = ['math', 'PI', 'English']

#multypling
result = subjectsList2 * 2

print(subjectsList + subjectsList2)
print(result)

# max and min

list_num = [1,2,3,4,5,6]

print(max(list_num))
print(min(list_num))

# Introduction to Dictionaries

# How it would be in lists
students = ["bob", 12, "rachel" , 13, "emily", 15]
print(students[3])

print(students)


# How it would be in dictionaries

students = {'bob': 12, 'rachel': 13}
print(students['rachel'])

students['rachel'] = 14

# delete key from dictionary
del students['rachel']

print(students)

# Introduction to Tuples
# tuples are like lists, however we cannot change or modify
# Since tuples are immutable, they guarantee that the data they hold will remain unchanged.
# Safety is important in tuples
tup = ('orange', 'apple', 'banana')
tup2 = (2,3,4)
tup3 = tup+tup2


print(tup[0])
print(tup[0:2])
print(tup3)



# Conditional Statements

if 3 > 3:
	print('hello')
else:
	print('condition was not true')

# relational operators
# > < >= <= == !=

# elif
# and / or
if age == 15:
	print("passed")
elif age == 14 and age == 11:
	print("not passed")
else :
	print("maybe, passed")


if 5 > 3 or 2 < 1:
	print('hi')


# For Loops

list1 = ['apple', 'banana', 'cherries']
tup2 = (2,3,4,5)

for item in list1:
	print(item)


for i in range(0,10):
	print(i)

for i in range(5,51,15):
	print(i)

for i in range(0,5):
	for j in range (0,3):
		print(i * j)

# While Loops

c = 0
while  c < 5:
	c += 1
	print(c)

# control statements - break, continue, pass

while c < 10:
	c += 1
	if c == 5:
		break
	print(c)

# break is to stop
# continue is to skip
# pass is to simply if we have no functions in certain condition


while c < 10:
	c += 1
	if c == 5:
		continue
	print(c)



while c < 10:
	c += 1
	if c == 5:
		pass
	print(c)



# Try and Except
# useful in situations when exceptions may be raised

name = 5

try:
	if name > 3:
		print("hello")
except:
	print("An error was detected")


# Functions 

def hello_world(name):
	print(f"Hello {name}")

hello_world("Mary")

def sum(num1,num2):
	return num1 + num2

def mul(num1,num2):
	return num1 * num2


print(mul(sum(1,2) , sum(4,3)))

# Built-in Python Functions

# absolute value
print(abs(7), abs(-7))

# bool function
print(bool(0), bool(None), bool(1))

# dir function
print(dir("hello"))

# help function
print(help("hello".upper))

# eval
sent = 'print("hi")'
eval(sent)

# exec - eval, but multiply lines

# str , int , float
print(int('432')+23)


# Object-Oriented Programming
# Classes and Objects



class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getName(self):
		return self.name


	def getAge(self):
		return self.age
	

p = person("Bryan", 16)
print(p.getName() , p.getAge())


# OOP - Class Inheritance

# Base model - engine , wheels, etc
# Sports Model - powerful


class Car(object):
	def __init__(self):
		self.wheels = 4
		self.seats = 5

	def drive(self):
		print("Driving a car...")
		

class SportsCar(Car):
	def __init__(self):
		super().__init__()
		self.engine_power = " 5000 hp "
		self.seats = 1

	# def drive(self):
	# 	print("Driving a sports car...")


myCar = Car()
myCar.drive()

mySportsCar = SportsCar()
mySportsCar.drive()