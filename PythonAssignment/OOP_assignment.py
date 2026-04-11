""" 1. Write a Python program to create a class representing a Circle.
    Include methods to calculate its area and perimeter."""
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius

r = float(input("Enter the radius of the circle: "))
c = Circle(r)
print("Area : ",c.area())
print("Perimeter",c.perimeter())


""" 2. Write a Python program to create a person class. Include attributes like name, country and date of birth.
    Implement a method to determine the person's age."""
from datetime import date
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

        year,month,day  = map(int,date_of_birth.split("-"))
        self.date_of_birth = date(year,month,day)

    def calculate_age(self):
        today = date.today()

        age = today.year - self.date_of_birth.year

        if (today.month ,today.day) < (self.date_of_birth.month,self.date_of_birth.day):
             age -= 1
        return age

p = Person("Sumit","India","2002-06-01")
print("Age : ",p.calculate_age())


"""3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations."""

class Calculator:
    def add(self,*numbers):
        return sum(numbers)
    def subtract(self,*numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result
    def multiply(self,*numbers):
        result = 1
        for num in numbers:
            result *= num
        return result
    def divide(self,*numbers):
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Error")
            else:
                result /= num
        return result

cal = Calculator()
print("Addition : ",cal.add(1,2,38))
print("Subtraction : ",cal.subtract(1,2,38))
print("Multiplication : ",cal.multiply(10,2,2))
print("Division : ",cal.divide(10,2))


""" 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area 
and perimeter.Implement subclasses for different shapes like circle, triangle, and square."""

from abc import ABC,abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self ):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * self.radius * self.radius
    def perimeter(self):
        return 2 * pi * self.radius

class Triangle(Shape):
    def __init__(self,l,b,h):
        self.l = l
        self.b = b
        self.h = h
    def area(self):
        return  0.5 * self.b * self.h
    def perimeter(self):
        return self.l + self.b + self.h

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2 *(self.l + self.w)

c = Circle(2)
print("Area : ",c.area())
print("Perimeter : ",c.perimeter())

r = Rectangle(2,3)
print("Area : ",r.area())
print("Perimeter : ",r.perimeter())

t = Triangle(3,4,5)
print("Area : ",t.area())
print("Perimeter : ",t.perimeter())


""" 8. Write a Python program to create a class representing a shopping cart.
    Include methods for adding and removing items, and calculating the total price."""

products = {
    'PS5' : [50000,10],
    'Asus_laptop' : [150000,5],
    'Mouse': [500,200],
    'Keyboard' :[500,200],
    'TUF Gaming VG28UQL1A' :[50000,5]
}

class Shopping_Cart:
    def __init__(self,items):
        self.items = items

    def add_items(self,name,price):
        if name in self.items :
            print(f'{name} already present')
        else:
            qty = int(input("Enter a quantity : "))
            self.items[name] = [price,qty]
            print(f'"{name}" added - Rs.{price} X {qty}')

    def remove_items(self,name):
        if name in self.items:
            del self.items[name]
            print(f"{name} is removed")
        else:
            print(f"{name} not found")

    def total_price(self):
        total = 0
        for price,qty in self.items.values():
            total += price*qty
        return total

    def show_cart(self):
        if not self.items:
            print("Cart is empty")
        else:
            print("---- your cart -----")
            for name,(price,qty) in self.items.items():
                print(f"{name} : Rs.{price} X {qty} = Rs.{price*qty}")
            print(f"total : Rs.{self.total_price()}")


cart = Shopping_Cart(products)
cart.show_cart()


""" 11. Write a Python program to create a class representing a bank. Include methods 
    for managing customer accounts and transactions.
	Create a Python class called BankAccount which represents a bank account, having as attributes:
	accountNumber (numeric type), name (name of the account owner as string type), balance.
	Create a constructor with parameters: accountNumber, name, balance.
	Create a Deposit() method which manages the deposit actions.
	Create a Withdrawal() method which manages withdrawals actions.
	Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
	Create a display() method to display account details. Give the complete code for the BankAccount class."""

class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Your account balance is {self.balance} and amount deposited is {amount}")
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.balance -= amount
            print(f"Your account balance is {self.balance} and amount deposited is {amount}")

    def bankFees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print(f"Bank fees applied : {fees}")

    def display(self):
        print("\n Account Details")
        print("account number : ",self.accountNumber)
        print("account name : ",self.name)
        print("account balance : ",self.balance)

account1 = BankAccount(1,"ABC",50000)

account1.display()
account1.withdraw(1000)
account1.deposit(5000)
account1.bankFees()
account1.display()


""" 12. Build a flashcard using class in python. A flashcard is a card having information on both sides, 
    which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer 
    on the other.
	Example 1:
	Approach:
	Create a class named FlashCard.
	Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value.
	E.g., {"Banana": "yellow", "Strawberries": "pink"}
	Now randomly choose a pair from fruits by using random module and store the key in variable fruit and 
	value in variable color.
	Now prompt the user to answer the color of the randomly chosen fruit.
	If correct print correct else print wrong.
	Output:

	welcome to fruit quiz
	What is the color of Strawberries
	pink
	Correct answer
	Enter 0, if you want to play again: 0
	What is the color of watermelon
	green
	Correct answer
	Enter 0, if you want to play again: 1"""

import random
class flashcard:
    def __init__(self):
        self.fruits ={"Banana": "yellow",
            "Strawberries": "pink",
            "Watermelon": "green",
            "Mango": "orange",
            "Grapes": "purple"}

    def quiz(self):
        print("Welcome to fruits quiz")

        while True:
            fruit,color = random.choice(list(self.fruits.items()))
            rs = input(f"What is color of {fruit} : ")
            if rs.lower() == color.lower():
                print("Correct answer")
            else:
                print("Incorrect answer")
                print(f"the correct color is {color}")
            choice = int(input("Enter 1, If you want to play again: "))
            if choice != 1:
                break

f = flashcard()
f.quiz()


""" 13. TechWorld, a technology training center, wants to allocate courses for instructors. An instructor
    is identified by name, technology skills, experience and average feedback. An instructor is allocated a course,
    if he/she satisfies the below two conditions:
	eligibility criteria:
	if experience is more than 3 years, average feedback should be 4.5 or more
	if experience is 3 years or less, average feedback should be 4 or more
	he/she should posses the technology skill for the course
	Identify the class name and attributes to represent instructors. Write a Python program to implement 
	the class chosen with its attributes and methods.
	Note:
	Consider all instance variables to be private and methods to be public.
	An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
	check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
	allocate_course(technology): Return true if the course which requires the given technology can be allocated 
	to the instructor. Else, return false.
	Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate
	methods and test your program.
	
"""

class TechWorld:
    def __init__(self):
        self.__name = None
        self.__skills =[]
        self.__exp = 0
        self.__avg_feedback = 0.0
    # setters
    def set_name(self,name):
        self.__name = name
    def set_skill(self,skill):
        self.__skills = skill
    def set_experience(self,exp):
        self.__exp = exp
    def set_avg_feedback(self,ab):
        self.__avg_feedback = ab

    # getters
    def get_name(self):
        return self.__name
    def get_skill(self):
        return self.__skills
    def get_experience(self):
        return self.__exp
    def get_avg_feedback(self):
        return self.__avg_feedback

    # actual methods
    def check_eligiblity(self):
        if self.__exp > 3:
            return self.__avg_feedback >=4.5
        else:
            return self.__avg_feedback >= 4

    def allocate_course(self,tech):
        if self.check_eligiblity() and tech in self.__skills:
            return True
        return False
a = TechWorld()
a.set_name("Amar Pal")
a.set_skill(['Python','java','ML','LLM'])
a.set_experience(5)
a.set_avg_feedback(4.7)

print(f"{a.get_name()} - LLM : {a.allocate_course('ML')}")

