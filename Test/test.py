#First Python Program
print("My name is Nestah")

#Show String Type
print("My name is Nestah")
print(type("My name is Nestah"))

#Print String Type
first_name = "Nestah"
print(first_name)

#Print using F-Strings
first_name = "Nestah"
food_name = "Pizza"
print(f"My name is {first_name} and I love {food_name}")

#Input and Output in Python
name = input("What is your name? ")
print("Hello " + name + ", how are you doing today?")

#Print variable in a string
s="Nestah"
print(s)

#Print the first three characters of a string
s="Nestah"
print(s[0:3]) #prints the first three characters of the string

#s="Nestah"
#print(s[0:6]) #prints the first six characters of the string

#print muiltiple items in a string
Name = "Nestah"
Age = 24
Area = "Nairobi"
print("My name is " + Name + ", I am " + str(Age) + " years old and I live in " + Area)

#print muiltiple variables in a string
Name = "Nestah"
Age = 24
Area = "Nairobi"
print(Name, Age, Area)

#Print muiltiple variables in a single line
x , y , z = "Nestah", 24, "Nairobi"
print(x, y, z)

#print default string type to any other type
i = int(input("what is your age? "))
f = float(input("what is your height? "))
print(i,f)

i = int(input("what is your age? "))
f = float(input("what is your height? "))
print("My age is " + str(i) + " and my height is " + str(f))

#variables
a = 24
name = "Nestah"
print(a)
print(name)

#Valide variable names
age = 24
_colour = "red"
approximate_height = 65
print(f"Age is {age}, colour is {_colour}, and height is {approximate_height}")

#Invalid variable names - confrimed errors shown -didn't run
#1age = 24
#class = 6
#person-name = "Nestah"
#print(f"Age is {1age}, class is {class}, and name is {person-name}")


# Basic Assignment where Variables are assigned values using the = operator.
x = 5
y = 3.14
z = "Hi"
print(x, y, z)

#Dynamic Typing
x = 5
x = "hello"
print(x)  # Output: hello

#Assigning Same Value
x = y = z = 10
print(x, y, z)  # Output: 10 10 10

#Assigning Different Values
x, y, z = 25, 2.5, "Nestah"
print(x, y, z)

##Arithmetic Operators

a = 21
b = 9

print("Addition:", a + b)

print("Subtraction:", a - b)

print("Multiplication:", a * b)

print("Division:", a / b)

print("Floor Division:", a // b)

print("Modulus:", a % b)

print("Exponentiation:", a ** b)


#Comparison Operators
a = 9
b = 24

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Logical Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Bitwise Operators
a = 15
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#Assignment Operators
a = 50
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

#Membership Operators
x = 25
y = 10
List = [10, 20, 30, 40, 50]
print(x in List)  # Output: False
print(y in List)  # Output: True
print(x not in List)  # Output: True
print(y not in List)  # Output: False

x = 31
y = 40
my_list = [10, 20, 30, 40, 50]
if (x in my_list):
    print("x is present in the list")
else:
    print("x is not present in the list")
if (y not in my_list):
    print("y is not present in the list")
else:
    print("y is present in the list")

#Ternary Operator
#Minimum of two numbers using ternary operator
a, b = 10, 20
min_val = a if a < b else b
print(min_val)  # Output: 10
print ("10")
print(type(min_val))  # Output: <class 'int'>

age = 17
status = "adult" if age >= 18 else "child"
print(status)  # Output: child

#Precedence and Associativity of Operators
#Precedence of Operators

a // 10
print(a)  # Output: 2

print((5 > 3) and (2 < 4))

x = 5
y = 3
print(x & y)

#Conditional statements
#if statement
age =34
if age >= 18:
    print("Eligible to vote.")

#if-else statement
age = 34

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

#Nested if-else Statement
age = 10
is_registered = True

if age >= 18:
    if is_registered:
        print("Eligible to vote.")
    else:
        print("Please register to vote.")
else:
    print("Not eligible to vote.")

#Conditional Expression (Ternary Operator)
age = 24
Nestah = "Adult" if age >= 18 else "Minor"
print(Nestah)

#Match case statement
number = 9
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case 3 | 4:
        print( "Three or Four")
    case _:
        print("Other number")

#
x = 8
if x > 5:
  print("Greater than 5")
elif x > 8:
  print("Greater than 8")
else:
  print("Less than or equal to 5")

#   Loops in Python
n = 4
for h in range(0, n):
    print(h)

#Iterating by Index of Sequences
n = ["nestah", "loves", "python", "and", "he", "is", "a", "developer"]
for idx in range(len(n)): #this will iterate through the index of the list n
    print(n[idx]) #assessing the elements of the list using the index

#While Loop
count = 0
while count < 5:
    count = count + 1  # Increment count by 1
    print("Nestah")

#Infinite While Loop
#while True:
    #print("nestah") #runs forever.

#nested loop
for n in range(1, 9):
    for j in range(n):
        print(n, end=' ')
    print()

#
x = "GFG"
for i in range(len(x)): #If lens(x) is not used it will throw an error because the string is not iterable.
    print(i)

#
n = [10, 20]
li = ["Chair", "Table"]

for x in n:
    for y in li:
        print(x, y)

# 
var = 10
for i in range(10):
    for j in range(2,10,1):
        if var % 2 == 0:
            continue
        else:
            var += 1
print(var)

#STAGE TWO FUNCTIONS
# STAGE TWO FUNCTIONS
# Python functions - Reusable code blocks used to perform tasks by organizing programs into smaller tasks
# Define a function using a key word
def func():
    print("My name is Nestah a function")

func()            #output: My name is Nestah a function
#Function arguments - values passed to a function when called(function receive input data)
#even odd number example
def evenOdd(x):
    if (x % 2 == 0):
        return "even"
    else:
        return "odd"

print(evenOdd(5))
print(evenOdd(20))    #output:  odd and even
# default arguments - use predefined value when no value is passed
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

def greet(name="Guest"):
    print("Hello, " + name)

greet()
greet("Manoti")         #output: Hello, Guest and Hello, Manoti  and Hello, Nestah
greet(name)   #how did in return my name? 'nestah'

#Keyword arguments - here they pass values using parameter name and arguments order doesnt matter
def drinks(water, juice):
    print(water, juice)

drinks(water='dasani' , juice='soda')
drinks(water='Tap Water' , juice='fanta')   #output: dasani soda  and Tap Water fanta

#Position arguments - patterns assigned based on there order to a the parameters
def nameGrade(name, grade):
    print("The top student in class is " , name)
    print("he's score is " , grade)

print("first example in postion arguments")
nameGrade("Ness" , 24)
print("second example in postion arguments")
nameGrade(24 ,"ness")              #output: first example in postion arguments The top student in class is  Ness  he's score is  24 and second example in postion arguments  The top student in class is  24  he's score is  ness


#Arbitrary arguments - allowers functions to accept multiple values using special symbols (*args, **kwargs)

   ## Have to revisit on a fresh mind in the morning.
######################################################################################################################
#Function within Functions - used to organize related logic n access variables from the other functions
#inner function/nested function
def hobbies():
    h = "I love playing basketball"
    def second_hobbie():
        print (h)

    second_hobbie()
hobbies()             #output: I love playing basketball

#Return Function - ends a function and ends a value back to the caller
#I think it is related to 'break' both are nested loops

def power_values(num):
    return num ** 2

print(power_values(3))
print(power_values(-9))   #output: 9 and 81


#Pass by Reference and Pass by Value - valiables refers to object while function behavior depends on where the object mutable/ immutable

def coins(x):
    x[1]=10     #modifies second element in the string which is mutable- so changes take place

b = [3, 5, 7, 9]
coins(b)
print(b)       #output: [3, 10, 7, 9]

def coins2(x):
    x = 2     #assigns new value to x which is an int(mutable) and remains unchange

d = 30
coins2(d)
print(d)      #output: 30

#Python pass Statement
#Python pass Statement - a placehold that does nothing when executed
 #In functions

def fun():
    pass

fun() # Call the function     output: no output since nothing was called without any error


#In Conditional Statements
x = 10

if x > 5:
    pass  # Placeholder for future logic
else:                               # the block is skipped
    print("x is 5 or less")

#in loops
for i in range(5):
    if i == 3:
        pass  # Does nothing when i is 3
    else:
        print(i)     #output: 0 1 2 4

#In classses - helps in defining methods/classes until a functionalty is added

class EmptyClass:
    pass                    #missing methods

class Person:
    def __init__(person, name, age):
        person.name = name
        person.age = age

    def greet(person):
        pass  # Placeholder for greet method

p = Person("Nestah", 24)

# Global and Local Variables
# local variable - defined inside a function and exixst only during execution
def greet():                  #creating and accessing a local variable inside a function
    msg = "hello, I enjoyed the coffee"
    print(msg)
greet()

#Global function  - ddeclared outside all function and can be declared anywhere
msg = "normalize learning a programming language without using AI"

def display():
    print("inside function:", msg)
display()
print("outside function:", msg)

#  Both local and global variable
def fun():
    s = "ME TOO"
    print(s)
s = "I love the new spider man movie"
fun()
print(s)

#Recursion - a function call its self before directly or indirectly to solve a problem


#recursive function to calculate nth Fibonacci number
def fibonacciTest(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciTest(n-1) + fibonacciTest(n-2)

print(fibonacciTest(10))      #output:55

#recursive function to calculate factorial of a number
def factorialTest(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorialTest(n - 1)

print(factorialTest(5))

#Recrusion Tail types -  Tail and non-tail
          #Tail - recursive call happens last by the function
          #non-tail - Functions does more work after recursive call
#First Class functions in Python
def msg(name):
    return f"Hello, {name}"
f = msg    #assigning the function
print(f(Nestah))  #calling the function.  #Output: Hello, Adult

#2. Passing Functions as Arguments
def msg(name):
    return f"Hello, {name}"
def fun1(fun2, name):
    return fun2(name)
print(fun1(msg, Nestah))  #output: Hello, Adult

 #3. Returning Functions from Other Functions
def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2
func = fun1("Hello, World!")  # Getting the inner function
print(func())

#Storying Functions In data structures

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
                     # Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}
                    # Calling functions from the dictionary
print(d["add"](5, 3))
print(d["subtract"](5, 3))   #output: 8    2


#Python Lambda Functions - Small anonymous function that don't have a defined name
a = 'NestahPythonClasses'
upper = lambda x: x.upper()
print(upper(a))    #Output: NESTAHPYTHONCLASSES

#Contidtion checking - use if-else condition statement to return diffrent results based on the condition
check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))
print(check(-3))
print(check(0))    #OUTPUT: Positive   Negative  Zero

#List comprehension
func = [lambda arg=x: arg * 10 for x in range(1, 6)]
for i in func:
    print(i())    #Output: 10   20   30   40  50
#Run multiple results - return Multiple results by combining them into tuples
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)     #output: (7, 12)   #Lamba performs both addition and mutiplication and submit a tuple eith both results

#Filter - usse lamba to select elements from a list to satisfy a given condition.

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))    #output: [2, 4, 6]
#Map -applies lamba expression to each element and return a map object
a = [1, 2, 3, 4]
double = map(lambda x: x * 2, a)
print(list(double))   #output:[2, 4, 6, 8]  #lamba function double the function and map applies the transformation.

#Reduce - Uses lamba expression to elements in a list to combine them into a single results
from functools import reduce
a = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, a)
print(mul)     #output: 24



nums = [1, 2, 3]
res = list(map(lambda x: x * 2, nums))
print(res)   #Output:[2, 4, 6]