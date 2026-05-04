""" 1.addition of two numbers from given list is 11"""
import ast

l = [1,2,3,4,5,6,7,8,9,10]
result = []
for i in range (len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == 11:
            result.append((l[i],l[j]))
print(result)

""" 2.list of prime numbers"""

l = list(range(1,11))
prime = []
for num in l:
     if num > 1:
         for i in range(2,num):
             if num % i == 0:
                 break
         else:
            prime.append(num)

print(prime)


""" 3.Write a program to find the sum of all elements in a list."""

l = [1,2,3,4,5,6,7,8,9,10]

total = 0
for num in l:
    total += num
print(total)


""" 4.Find the maximum and minimum element in a list."""

l = [3,5,3,58,34,87,21,7,1,77]

print(max(l))
print(min(l))

""" 5.Reverse a list without using built-in functions."""

l = [3,5,3,58,34,87,21,7,1,77]

print(l[::-1])

l = [3,5,3,58,34,87,21,7,1,77]
rev =[]

for i in range(len(l)-1,-1,-1):
    rev.append(l[i])
print(rev)


""" 6.Count how many times an element appears in a list."""

l = [2,4,5,6,4,3,2,5,9,8,1,3,1,7]

a ={}

for item in l:
    if item in a:
        a[item] += 1
    else:
        a[item] = 1
print(a)

""" 7.Remove duplicate elements from a list."""

l = [2,4,5,6,4,3,2,5,9,8,1,3,1,7]

new_list = []

for item in l:
    if item not in new_list:
        new_list.append(item)
print(new_list)


""" 8.Find the second largest number in a list."""

l = [2,4,5,7,9,22,45,65,1,34,6]

l.sort()

print(l[-2])


""" 9.Merge two lists without using +."""
l = [1,2,3,4,5]
l1 = [6,7,8,9,10]

l.extend(l1)
print(l)


""" 10.Find all even numbers from a list."""

l = [1,2,3,4,5,6,7,8,9,10]
even = []
for num in l:
    if num % 2 == 0:
       even.append(num)
print(even)


l = [1,2,3,4,5,6,7,8,9,10]
even = [num for num in l if num % 2 == 0]
print(even)


""" 11.Flatten a nested list
Example: [1, [2, 3], [4, [5]]] → [1,2,3,4,5]"""

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

l = [1, [2, 3], [4, [5]]]
print(flatten(l))


""" 12.Rotate a list by k positions."""
#right rotation
l = [1,2,3,4,5]
k = 2

k = k % len(l)

rotate = l[-k:] + l[:-k]
print(rotate)

#left rotation
l = [1,2,3,4,5]
k = 2

k = k % len(l)
rotate = l[k:] + l[:k]
print(rotate)


""" 13.Find the intersection of two lists."""
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

result = list(set(l1) & set(l2))
print(result)

l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
result = []
for item in l1:
    if item in l2 and item not in result:
        result.append(item)
print(result)


""" 14.Swap two variables using tuple unpacking."""
t = (1,3)

a,b = t
print(a)
print(b)

a,b = b,a
print(a)
print(b)


""" 15.Count occurrences of an element in a tuple."""
t = (1,2,4,3,1,3,5,6,2)
print(t.count(3))

t = (1,2,4,3,1,3,1,5,6,2)
count = 0
for item in t:
    if item == 1:
        count += 1
print(count)


""" 16.Convert tuple of tuples into a dictionary."""

t = (("a", 1), ("b", 2), ("c", 3))

d = {}
for key,value in t:
    d[key] = value
print(d)

t = (("a", 1), ("b", 2), ("c", 3))
d = dict(t)
print(d)

# dictionary comprehension
t = (("a", 1), ("b", 2), ("c", 3))
d = {k : v for k,v in t}
print(d)


""" 17.Access a value safely using get()."""
D = {"a":1,"b":2}
print(D.get("b"))
print(D.get("c",4))


""" 18.Count frequency of characters in a string using dictionary."""

s = "frequent frequency"

freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)


""" 19.Merge two dictionaries."""

d1 = {"a":1,"b":2}
d2 = {"c":3,"d":4,"e":5}
d1.update(d2)
print(d1)

d1 = {"a":1,"b":2}
d2 = {"c":3,"d":4,"e":5}
print(d1 | d2)

d1 = {"a":1,"b":2}
d2 = {"c":3,"d":4,"e":5}
d = d1.copy()

for key,value in d2.items():
    d[key] = value
print(d)


""" 20.Sort a dictionary by keys or values."""
# by keys
d2 = {"z":8,"d":4,"e":5}
sorted_dict = dict(sorted(d2.items()))
print(sorted_dict)

d =  {"c":8,"d":4,"e":5}
sorted_dict = dict(sorted(d.items(),reverse = True))
print(sorted_dict)


# by values
d2 = {"c":8,"d":4,"e":5}
sorted_dict = dict(sorted(d2.items(),key = lambda x : x[1]))
print(sorted_dict)


""" 21.Invert a dictionary (swap keys and values)."""
d = {"a":1,"b":2}
inv_d ={}
for key,value in d.items():
    inv_d[value] = key
print(inv_d)


d = {"a":1,"b":2}
inv_d = {v:k for k,v in d.items()}
print(inv_d)


""" 22.Find the key with maximum value."""
d1 = {"a":1,"b":2,"c":3,"d":4,"e":5}
max_key = max(d1,key = d1.get)
print(max_key)


d1 = {"a":1,"b":2,"c":3,"d":4,"e":5}
max_key = None
max_value = float("-inf")

for key,value in d1.items():
    if value > max_value:
        value = max_value
        max_key = key

print(max_key,max_value)


""" 23.Sort the by using second element of tuple"""
l =[("raj",20),("amar",22),("dhiraj",25),("samir",19)]

d = {}
for key,value in l:
    d[key] = value
print(d)
Sort_by = sorted(d.items(),key = lambda x: x[1])
print(Sort_by)


l =[("raj",20),("amar",22),("dhiraj",25),("samir",19)]
sorting = sorted(l,key = lambda x: x[1])
print(sorting)


""" 24.Remove duplicates using filter and sort it"""
l = [2,4,5,2,6,7,8,2,4,5,0,4,1]

seen = set()
result = list(filter(lambda x: x not in seen and not seen.add(x), l))
l1 = sorted(result)
print(l1)


""" 25.Group elements by frequency"""

from collections import Counter
l =[1,2,2,3,3,3,4,4]

freq = Counter(l)

grp = {}
for key,value in freq.items():
    grp.setdefault(key,[]).append(key)

print(grp)


""" 26.Check if string is palindrome"""
Str = input("Enter a string: ")
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome(Str))


""" 27.Count vowels and consonants."""

a = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_cnt = 0
c_cnt = 0

for ch in a:
    if ch in vowels:
        v_cnt += 1
    else:
        c_cnt += 1

print("vowels:",v_cnt)
print("consonants:",c_cnt)


""" 28.Reverse a string."""
a = input("Enter a string: ")

def reverse(s):
    return s[::-1]

print(reverse(a))


""" 29.Count number of words in a string."""
st = input("Enter a string: ")

count = 0
for w in st.split():
    count += 1

print("Number of words:",count)


""" 30.Find the first non-repeating character."""

from collections import Counter
St = "programmer"
freq = Counter(St)

for ch in St:
    if freq[ch] == 1:
        print(ch)
        break


""" 31.Remove all duplicates from a string."""

s = "helloharry"
result = ""
for ch in s:
    if ch not in result:
        result += ch

print(result)


""" 32.Check if two strings are anagrams."""

s1 = input("Enter a string: ")
s2 = input("Enter another string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagram")
else:
    print("Not Anagram")


from collections import Counter
s1 = input("Enter a string: ")
s2 = input("Enter another string: ")

if Counter(s1.lower()) == Counter(s2.lower()):
    print("Anagram")
else:
    print("Not Anagram")


""" 33.Find duplicate elements in a list."""

l = [1,2,3,2,3,4,2,5,6,4,5]

seen = []
duplicates = []

for item in l:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    else:
        seen.append(item)

print(duplicates)


""" 34.Find common elements in two lists."""

l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
r = list(set(l1) & set(l2))
print(r)


l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
r = []
for item in l1:
    if item in l2:
        r.append(item)
print(r)


""" 35.Convert string to dictionary with character frequency."""

s = "hello harry"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq)


from collections import Counter
s = input("Enter a string: ")
freq = Counter(s)
print(freq)

""" 36.Find the most frequent word in a sentence."""

s= input("Enter a string: ")
words = s.split()   # sentence to list
max_freq = {}
for word in words:
    max_freq[word] = max_freq.get(word,0)+1
max_word = max(max_freq.values())
result = [k for k,v in max_freq.items() if v == max_word]
print("Most frequent words:",result)



l = [1]
t = (1,)
print(type(t))
t1 =1,2,3
print(type(t1))
a,b,c = t1
print(a)
print(type(a))


# Generator

def count_up_to(n):
    i = 1
    while i <= n:
        yield  i
        i += 1

for number in count_up_to(5):
    print(number)


""" 37.Create a class Person with attributes name and age. Print the details"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("amar",18)
print(p.name,":",p.age)


""" 38.Create a class Student with:
    attributes: name, marks
    method: display() to print details"""

class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"\tstudent name is {self.name}\n\t marks are {self.marks}")

st = input("Enter student name: ")
m = int(input("Enter marks: "))
s = Student(st,m)
s.display()


""" 39.Write a class Calculator with methods:
    add(), subtract(), multiply(), divide()"""

class Calculator:
    def add(self,*args):
        return print("Addition of numbers is:",sum(args))
    def subtract(self,*args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return  result
    def multiply(self,*args):
        res = 1
        for n in args:
            res *= n
        return res
    def divide(self,*args):
        result = args[0]
        for x in args[1:]:
            if x == 0:
                print("division by zero is not allowed")
            result /= x
        return result


a = Calculator()
print(a.add(1,2,3,4,5,6,7,8,9,10))
print(a.subtract(1,2,3,4,5,6,7,8,9,10))
print(a.multiply(1,2,3,4,5,6,7,8,9,10))
print(a.divide(1,2,3,4,5,6,7,8,9,10))


""" 40.👉 Create a class Student with attributes name and marks. Print student details."""

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"\tstudent name is {self.name}\n\t marks are {self.marks}")
        if self.marks >= 35:
            print("Pass")
        else:
            print("Fail")


nm = input("Enter student name: ")
m = int(input("Enter marks: "))
s = Student(nm,m)
s.display()


""" 41.👉 Create a class Car with default speed = 0 and method to update speed."""
class Car:
    def __init__(self,speed = 0):
        self.speed = speed

    def update(self,a):
        self.speed = a
        print(f"the speed id {self.speed}")

a = int(input("Enter a car speed: "))
c = Car()
c.update(a)


""" 42.👉 Count how many objects are created using a class variable."""

class Abc:
    count = 0
    def __init__(self):
        Abc.count += 1

a1 = Abc()
a2 = Abc()
a3 = Abc()

print("No. of objects created: ",Abc.count)


""" 43.👉 Write a class with: instance method , class method and static method"""

class Car:
    total_cars = 0   # class variable

    def __init__(self, brand, speed):
        self.brand = brand      # instance variable
        self.speed = speed
        Car.total_cars += 1

    # 1️⃣ Instance Method
    def display(self):
        print(f"Car: {self.brand}, Speed: {self.speed}")

    # 2️⃣ Class Method
    @classmethod
    def show_total_cars(cls):
        print(f"Total cars created: {cls.total_cars}")

    # 3️⃣ Static Method
    @staticmethod
    def is_fast(speed):
        return speed > 100


# Example usage
c1 = Car("BMW", 120)
c2 = Car("Audi", 80)

c1.display()                 # Instance method
Car.show_total_cars()        # Class method

print(Car.is_fast(120))      # Static method → True
print(Car.is_fast(70))       # Static method → False


""" 44.Sort list of tuples using second value."""
l1 = [(1, 3), (2, 1), (4, 2)]
l1.sort(key=lambda x:x[1])
print(l1)

l2 = [(1, 3), (2, 1), (4, 2)]
a = sorted(l2,key = lambda x:x[1])
print(a)

""" 45.Sort dictionary by values."""
d = {'a': 3, 'b': 1, 'c': 2}
sorted_d = sorted(d.items(),key = lambda x:x[1])
print(sorted_d)

""" 46.Lambda inside list comprehension - Multiply each element by two"""
num = [1,2,3]
result = [(lambda x :x*2)(x) for x in num]
print(result)


""" 47.Nested lambda - Add """

nest = lambda x: lambda y: x + y
print(nest(3)(6))


""" 48.Conditional logic - Check if even or odd"""
check = lambda x :"Even"if x%2 == 0 else "Odd"
print(check(8))

l = [1,2,3,4,5,6,7,8,9,10]
check = list(map(lambda x:"Even" if x%2 == 0 else "Odd",l))
print(check)


""" 49.Sort strings by length"""
wrds = ["apple","add","subtract","Given","useful","helplessness"]
st = sorted(wrds,key = lambda x:len(x),reverse = True)
print(st)


""" 50.Combine map + filter - square only even numbers"""
l = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x:x**2,filter(lambda x:x%2 == 0,l)))
print(result)


""" 51.Find highest salary"""
employees = [
    {"name": "A", "salary": 5000},
    {"name": "B", "salary": 8000},
    {"name": "C", "salary": 6000}
]
highest = max(employees,key = lambda x:x["salary"])
print(highest)


""" 52.Encapsulation
👉 Create a class BankAccount:
private balance
deposit()
withdraw()
getter method"""

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return print(self.__balance)
    def deposit(self,amount):
        self.__balance += amount
        print("The balance is: ",self.__balance)
    def withdraw(self,amount):
        self.__balance -= amount
        print("The balance is: ",self.__balance)

a = BankAccount(1000)
print(a.deposit(100))
a.get_balance()


""" 53.Inheritance
👉 Create:
Animal class → method sound()
Dog and Cat classes override sound"""

class Animal:
    def sound(self):
        print("The animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("Meow Meow!!")

d = Dog()
d.sound()
c = Cat()
c.sound()


""" 54.Multiple Inheritance
👉 Create two classes:
Father → skills
Mother → skills
Child inherits both"""

class Father:
    def Skills(self):
        print("Father's skills: Driving")

class Mother:
    def Skills(self):
        print("Mother's skills: Cooking")

class Child(Father, Mother):
    def Skills(self):
        print("Child skills: ")
        Father.Skills(self)
        Mother.Skills(self)

c = Child()
c.Skills()


""" 55.Abstraction
👉 Use abc module:
Abstract class Shape
Abstract method area()
Implement in Circle and Rectangle"""

from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

c = Circle(3)
print(c.area())
t = Rectangle(3,4)
print(t.area())


""" 56.Use lambda with filter() to extract numbers greater than 50 from list."""

l = [2,3,51,56,90,5,67]

updated_list =list(filter(lambda x : x > 50,l))
print(updated_list)


""" 57.Use lambda with map() to multiply each element of list by 5."""

l1 = [1,2,3,4,5,6,7,8,9,10]

up_list = list(map(lambda x : x*5,l1))
print(up_list)


""" 58.Use lambda with sorted() to sort list of tuples based on second value."""
l = [('a',4),('b',1),('d',3),('c',2)]
sorted_list = list(sorted(l,key = lambda x : x[1]))
print(sorted_list)


""" 59.Use lambda to sort dictionary by values."""

d = {"maths":98,"english":76,"physics":88,"chemistry":45,"biology":73}

sorted_d = dict(sorted(d.items(),key = lambda x : x[1]))
print(sorted_d)


""" 60.Use lambda to sort dictionary by keys."""

d = {"maths":98,"english":76,"physics":88,"chemistry":45,"biology":73}

sort_d = dict(sorted(d.items(),key = lambda x : x[0]))
print(sort_d)


""" 61.Write a program to handle ZeroDivisionError using try-except."""

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Error! cannot divide by zero")


""" 62.Write a program to handle ValueError when user enters invalid integer input."""

def add(a,b):
    try:
        print("sum :",int(a) + int(b))
    except ValueError:
        print("Incorrect input")

add(2,"eij")


""" 63.Write a program to handle ValueError and ZeroDivisionError"""

def divide():

    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print("Division : ", a / b)

    except ValueError:
        print("Incorrect input")
    except ZeroDivisionError:
        print("Error! cannot divide by zero")
divide()


""" 64.Write a program to take tuple of numbers from keyboard and print its sum and average."""
t =eval(input("Enter a tuple: "))
l = len(t)
total = 0
for i in t:
    total += i
print("Sum : ",total)
print("Average : ",total/l)


""" 65.Write a program to print different vowels present in the given word"""
import ast    # Abstract Syntax Tree
w = ast.literal_eval(input("Enter a word: ")).lower()
s = set(w)
v = {'a','e','i','o','u'}
a = s.intersection(v)
print(f"Different vowels present in {w} are :",a)

