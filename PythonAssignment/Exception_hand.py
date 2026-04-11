""" 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
"""

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    c = a/b
    print(c)
except ZeroDivisionError:
    print("Error! cannot divide by zero")


""" 2. Write a Python program that prompts the user to input an integer and raises
    a ValueError exception if the input is not a valid integer"""

try:
    usr = int(input("Enter a number: "))
    print("your value is: ",usr)
except ValueError:
    print("Error")


""" 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
"""

try:
    filename = input("Enter a filename: ")
    with open(filename,'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error")


"""4. Write a Python program that prompts the user to input two numbers and 
   raises a TypeError exception if the inputs are not numerical."""

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print("Sum of two numbers: ",a+b)

except ValueError:
    raise TypeError("Error")


""" 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
"""

try:
    filenm = input("Enter a filename: ")
    with open(filenm,'r') as file:
        content = file.read()
        print(content)

except PermissionError:
    print("Error! You do not have permission to access the file")

except FileNotFoundError:
    print("Error")


""" 6. Write a Python program that executes an operation on a list and
    handles an IndexError exception if the index is out of range"""
try:
    l = [1,2,3,4,5,6]
    index = int(input("Enter a number: "))
    print(f"value present at index {index} is: ",l[index])
except IndexError:
    print("Index out of range")

""" 7. Write a Python program that executes division and handles an ArithmeticError exception 
    if there is an arithmetic error."""

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a/b
    print(c)
except ArithmeticError:
    print("Error! cannot divide by zero")