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


""" 14.Write a program that uses datetime module within a class. Enter manufacturing date and 
    expiry date of the product.
    The program must display the years, months and days that are left for expiry."""

from datetime import datetime
class Product:
    def __init__(self,mfg_date,exp_date):
        self.mfg_date = datetime.strptime(mfg_date,"%d-%m-%Y")
        self.exp_date = datetime.strptime(exp_date,"%d-%m-%Y")

    def time_left(self):
        today = datetime.today()

        if self.exp_date < today:
            print("Product is already expired!")
            return

        diff = self.exp_date - today
        total_days = diff.days

        years = total_days //  365 # floor division
        remaining_days = total_days % 365
        months = remaining_days // 30
        days = remaining_days % 30

        print("years: ",years)
        print("months: ",months)
        print("days: ",days)

mfg =input("Enter mfg date : ")
exp =input("Enter exp date : ")

p = Product(mfg,exp)
p.time_left()


""" 15.A university wants to automate their admission process. Students are admitted based on the 
    marks scored in the qualifying exam. A student is identified by student id, age and 
    marks in qualifying exam. Data are valid, if:

	Age is greater than 20
	Marks is between 0 and 100 (both inclusive)
	A student qualifies for admission, if

	Age and marks are valid and
	Marks is 65 or more
	Write a python program to represent the students seeking admission in the university"""

class Student:
    def __init__(self,s_id,age,marks):
        self.s_id = s_id
        self.age = age
        self.marks = marks
    def is_valid(self):
        if self.age >= 20 and 0 <= self.marks <= 100:
            return True
        return False
    def is_eligible(self):
        if self.is_valid() and self.marks >= 65:
            return True
        return False

    def display(self):
        print("Student ID : ",self.s_id)
        print("Age : ",self.age)
        print("Marks : ",self.marks)

        if not self.is_valid():
            print("Invalid Data")
        elif self.is_eligible():
            print("Eligible")
        else:
            print("Not Eligible")

sid = input("Enter student ID : ")
age = int(input("Enter student age : "))
marks = int(input("Enter student marks : "))

s = Student(sid,age,marks)
s.display()


""" 16.Ice-Cream Scoops and Bowl shop
	Create a class Scoop which has one public property flavor and one private proptery price.
	Take flavor values during object creation.
	Create a class Bowl with private prperty scoop_list which will have list of scoopd object.
	Create a method add_scoops in Bowl class which will add any no of Scoop objects given as parameter 
	and store it in scoops_list.
	Make getter and setter method for price property.
	Make a method display to display flavour and price of each Scoop in scoop_list and 
	print total price of the bowl by adding all flavour scoops prices.
	Make a method sold in both Scoop class and Bowl class to print no of quantity sold."""

class Scoop:
    count = 0
    def __init__(self,flavour,price):
        self.__price = price
        self.flavour = flavour
        # maintain count to how many scoops present
        Scoop.count += 1

    def set_price(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

    def sold(self):
        print(f"{Scoop.count}")

class Bowl:
    def __init__(self):
        self.__scoop_list=[]

    def add_scoop(self,*scoops):
        for scoop in scoops:
            if isinstance(scoop,Scoop):
                self.__scoop_list.append(scoop)

    def display(self):
        total = 0
        for x in self.__scoop_list:
            print(f"{x.flavour} flavour: Rs.{x.get_price()} ")
            total += x.get_price()
        print(f"Total Price of Bowl : Rs.{total}")

    def sold(self):
            print(f"sold scoop for one bowl : {len(self.__scoop_list)}")

s1 = Scoop("Mango",500)
s2 = Scoop("Chocolate",720)
s3 = Scoop("Vanilla",400)

b1 = Bowl()
b2 = Bowl()
b2.add_scoop(s2)
b1.add_scoop(s1,s2,s1,s3)
b1.display()
b1.sold()


""" 17.Create a Bus child class that inherits from the Vehicle class. The default fare charge of 
    any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare 
    as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% 
    of the total fare.
    Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
    You need to override the fare() method of a Vehicle class in Bus class.
"""

class Vehicle:
    def __init__(self,vsc =0):
        self.vsc = vsc

    def charges(self):
        return self.vsc *100

class Bus(Vehicle):
    def __init__(self,n):
        super().__init__(n)   #if we have to pass att of 2 parents we need p_class.__init__(self,args of both)

    def charges(self):
        fare = super().charges()
        maintenance = fare * 0.1
        return maintenance + fare

v1 = Vehicle()
b1 = Bus(50)
print(b1.charges())


""" 18.Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and
    emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
	Sample Employee Data:
	"ADAMS", "E7876", 50000, "ACCOUNTING"
	"JONES", "E7499", 45000, "RESEARCH"
	"MARTIN", "E7900", 50000, "SALES"
	"SMITH", "E7698", 55000, "OPERATIONS"

	Use 'assign_department' method to change the department of an employee.
	Use 'print_employee_details' method to print the details of an employee.
	Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is
	the number of hours worked by the employee. If the number of hours worked is more than 50,
	the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
	overtime = hours_worked - 50
	Overtime amount = (overtime * (salary / 50))"""

import random
class Employee:
    def __init__(self,emp_id,emp_name,emp_sal):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_sal = emp_sal
        self.emp_department = ""

    def assign_department(self):
        l = ["INFORMATION TECHNOLOGY","ACCOUNTING","HUMAN RESOURCES","FINANCE","RESEARCH","SALES" ]
        random.shuffle(l)
        self.emp_department = l[0]


    def calculate_emp_salary(self,salary,hr_worked):
        if hr_worked > 50:
            overtime = hr_worked - 50
            overtime_amount = (overtime * (salary / 50))
            total_salary = salary + overtime_amount
        else:
            total_salary = salary
        self.emp_sal = total_salary
        return f"total salary of employee is  : {self.emp_sal}"

    def print_employee_details(self):
        print("="*40)
        print("\t\tEmployee Details")
        print("="*40)
        print(f"""\tEmployee ID : {self.emp_id}\n\tEmployee Name : {self.emp_name}\n\tEmployee Salary : {self.emp_sal}\n\tEmployee Department : {self.emp_department}
                    """)
        print("="*40)
e1 = Employee("E101","Walter White",50000)
e1.assign_department()
e1.calculate_emp_salary(50000,100)
e1.print_employee_details()


""" 19.Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders,
    and methods like add_item_to_menu, book_tables, and customer_order.
	Perform the following tasks now:
	Now add items to the menu.
	Make table reservations.
	Take customer orders.
	Print the menu.
	Print table reservations.
	Print customer orders.
	Note: Use dictionaries and lists to store the data."""

class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.book_table = {}
        self.customer_order = {}

    def add_items_to_the_menu(self,item_name,price):
        items = {"name":item_name,"price":price}
        self.menu_items.append(items)
        print(f"{item_name} added to menu at Rs.{price}")

    def menu(self):
        print("="*40)
        print("      menu          ")
        print("="*40)
        for item in self.menu_items:
            print(f"{item['name']} - {item['price']}")
        print("="*40)

    def book_tables(self,table_no,cust_name):
        print("="*40)
        print("Select Table from given list")
        l=['T1','T2','T3','T4','T5']
        print(l)
        print("="*40)
        if table_no in self.book_table:
            print(f"{table_no} already booked .. !")
        else:
            self.book_table[table_no] = cust_name
            print(f"Thank You you booked {table_no} table successfully..!")
            self.menu()

    def customer_orders(self,table_no,order_name):
        for x in self.menu_items:
               if x["name"] == order_name:
                    if table_no not in self.customer_order:
                        self.customer_order[table_no] = []
                    self.customer_order[table_no].append(order_name)
                    print(f"{order_name} Order taken wait 15 min to eat delicious food...! ")
                    return

        print("Sorry for service inconvenience, selected item not present in menu")

c1 = Restaurant()
c1.add_items_to_the_menu("Bruschetta", 180)
c1.add_items_to_the_menu("Stuffed Mushrooms", 220)
c1.add_items_to_the_menu("Crispy Calamari", 350)

c1.book_tables("T1","James Bond")
c1.customer_orders("T1",'Bruschetta')


""" 20.Write a Python class BankAccount with attributes like account_number, balance, 
    date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance."""

class BankAccount:
    def __init__(self,account_number,customer_name,balance,date_of_opening):
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self,amt):
        if amt < 0:
            print("Enter valid amount Rs. ")
        else:
            self.balance += amt
            print('='*40)
            print(f"Rs.{amt} Deposited successfully")
        print(f"Available Balance : Rs.{self.balance}")
        print('='*40)

    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficient funds...!")
        else:
            self.balance -= amt
            print('='*40)
            print(f"Rs.{amt} withdrawal successfully")
        print(f"Available Balance is Rs..{self.balance}")
        print('='*40)

    def check_balance(self):
        print("="*40)
        print(f"Available Balance is Rs.{self.balance}")
        print("="*40)

    def acc_details(self):
        print('='*40)
        print(f"Account Number : {self.account_number}\nCustomer Name: Mr/Ms {self.customer_name}\nDate Of Account Opening : {self.date_of_opening}\nAvailable Balance : Rs.{self.balance}")
        print('='*40)

# c1 = BankAccount("SBIN4023565","Spidy",10000,date(2026,11,4))
# c1.acc_details()
# c1.deposit(7000)
# c1.withdraw(5000)
# c1.check_balance()

c2 = BankAccount("SBIN4023789","Ironman",10000,date(2025,12,5))
c2.acc_details()
c2.deposit(7078)
c2.withdraw(20000)
c2.check_balance()


""" 21. Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and 
    methods like add_item, update_item, and check_item_details."""

class Inventory:
    def __init__(self):
        self.items = []


    def add_item(self,item_id,item_name,stock_count,price):
       # check if item already present
        for x in self.items:
            if x["item_id"] == item_id:
                print(f"{item_name} Already present")
                return
        d = {
            'item_id' : item_id,
            'item_name' : item_name,
            'stock_count' : stock_count,
            'price' : price
            }
        self.items.append(d)
        print(f"Item : '{item_name}' added successfully to Inventory..!")


    def update_item(self,item_id,stock_count,price):
        for x in self.items:
            if x["item_id"] == item_id :
                x['stock_count']  = stock_count
                x['price'] = price
                print(f"Item {item_id} updated successfully..!")
                return
        print("Item not found")


    def check_item_details(self,item_id):
        for x in self.items:
            if x["item_id"] == item_id:
                print("="*40)
                print("Item Details")
                print("="*40)
                print(f"ID : {x['item_id']}\nName : {x['item_name']}\nStock : {x['stock_count']}\nPrice : {x['price']}")
                print("="*40)
                return
        print('not found')

e1= Inventory()
e1.add_item("E101","White Papers",500,2000)
e1.add_item("E102","Pen",100,500)
e1.update_item("E101",450,1950)
e1.check_item_details("E102")


