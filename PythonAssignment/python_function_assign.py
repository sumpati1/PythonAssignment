# 1.Write a Python function to find the maximum of three numbers.

def maximum(*args):
    return max(args)
print(maximum(34,45,7))


""" 2.Write a Python function to sum all the numbers in a list.
	Sample List : (8, 2, 3, 0, 7)
	Expected Output : 20"""

def sumNum(numbers):
    return sum(numbers)
print(sumNum([8, 2, 3, 0, 7]))

def sumnum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sumnum([8, 2, 3, 0, 7]))


""" 3. Write a Python function to multiply all the numbers in a list.
	Sample List : (8, 2, 3, -1, 7)
	Expected Output : -336"""

def multiply(*args):      # *args takes separate arguments,not list
    total = 1
    for num in args:
        total *= num
    return total
print(multiply(8, 2, 3, -1, 7))

def Multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
print(Multiply([8, 2, 3, -1, 7]))


""" 4.Write a Python function to reverse a string. 
	Sample String : "1234abcd"
	Expected Output : "dcba4321" """

def reverseString(s):
    return s[::-1]
print(reverseString("1234abcd"))

# using loop
def revString(s):
    st = ""
    for char in s:
        st = char + st   # st = st + char --> stays same ,no reversal happens.
    return st
print(revString("1234abcd"))


""" 5.Write a Python function to check whether a number falls within a given range.
"""

def checkRange(num,start,end):
    if start <= num <= end:
        return True
    else:
        return False
print(checkRange(111,1,20))

# Using range function
def Range(num,start,end):
    if num in range(start,end+1):
        return True
    else:
        return False
print(Range(2,1,20))

""" 6.Write a Python function that accepts a string and counts the number of upper and lower case letters.
	Sample String : 'The quick Brow Fox'
	Expected Output :
	No. of Upper case characters : 3
	No. of Lower case Characters : 12"""

def countCase(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Uppercase letters : ",upper)
    print("Lowercase letters : ",lower)
print(countCase("The quick Brow Fox"))


""" 7.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
	Sample List : [1,2,3,3,3,3,4,5]
	Unique List : [1, 2, 3, 4, 5]"""

def distinct(l):
    unique = []
    for num in l:
        if num not in unique:
            unique.append(num)
    return unique
print(distinct([1,2,3,3,3,4,5]))

# using set
def dist(l):
    return list(set(l))
print(dist([1,2,3,3,3,4,5]))


""" 8.Write a Python function that checks whether a passed string is a palindrome or not.
	Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
	e.g., madam or nurses run."""

def palindrome(s):
    return s == s[::-1]   # using slicing
print(palindrome("madam"))
print(palindrome("nurses"))

# using loop
def palindr(s):
    reverse = ""
    for char in s:
        reverse =  char +reverse
    return True if reverse == s else False
print(palindr("madam"))
print(palindr("nurses"))


""" 9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints 
    the words in a hyphen-separated sequence after sorting them alphabetically.
	Sample Items : green-red-yellow-black-white
	Expected Result : black-green-red-white-yellow"""

def sort_words(s):
    words = s.split('-')      # split into list
    words.sort()              # sort alphabetically
    return '-'.join(words)    # join with hyphen

# Taking input from user
input_str = input("Enter hyphen-separated words: ")

result = sort_words(input_str)
print("Sorted sequence:", result)


""" 10.10. Write a Python program to detect the number of local variables declared in a function.
"""

def variableLocal():
    a = 1
    b = 2
    c = 0
    z = a * b + c
    return z
print("No. of local variables : ",variableLocal.__code__.co_nlocals)
print("Variable names : ",variableLocal.__code__.co_varnames)


""" 11.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
    also create a lambda function that multiplies argument x with argument y and prints the result."""

def add():
    return lambda y:y+15
result = add()   # get lambda func
print(result(2))  # Pass value to lambda function

def multiply():
    return lambda x,y:x*y
result = multiply()
print(result(2,3))


""" 12.Write a Python program to create a function that takes one argument, and that argument will be 
    multiplied with an unknown given number.
	Sample Output:
	Double the number of 15 = 30
	Triple the number of 15 = 45
	Quadruple the number of 15 = 60
	Quintuple the number 15 = 75"""


""" 13.Write a Python program to sort a list of tuples using Lambda.
	Original list of tuples:
	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	Sorting the List of Tuples:
	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""

l = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(l,key = lambda x: x[1])   # key tells python how to start
                                               # without key,python sorts by default(first element of tuple)
print(sorted_list)


""" 14.Write a Python program to sort a list of dictionaries using Lambda.
	Original list of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
	{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
	Sorting the List of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, 
	{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""

l1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
	{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sortedList = sorted(l1,key = lambda x:x['color'])
print(sortedList)


""" 15.Write a Python program to filter a list of integers using Lambda.
	Original list of integers:
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	Even numbers from the said list:
	[2, 4, 6, 8, 10]
	Odd numbers from the said list:
	[1, 3, 5, 7, 9]"""

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = list(filter(lambda x:x%2 == 0,L))
odd_num = list(filter(lambda x:x%2 == 1,L))
print(even_num)
print(odd_num)


""" 16.Write a Python program to square and cube every number in a given list of integers using Lambda.

	Original list of integers:
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	Square every number of the said list:
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	Cube every number of the said list:
	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]"""

def sq_cube(num):
    square = list(map(lambda x: x**2,num))
    cube = list(map(lambda x: x**3,num))
    return square,cube

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s,c = sq_cube(L)
print("square:",s)
print("cube:",c)


""" 18.Write a Python program to find if a given string starts with a given character using Lambda.
"""

def check_start():
    check = lambda s,char: s.startswith(char)
    string = input("Enter a string: ")
    ch = input("Enter a character: ")

    if check(string,ch):
        print("Yes")
    else:
        print("No")

check_start()


""" 19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
    Original arrays:
	[-1, 2, -3, 5, 7, 8, 9, -10]
	Rearrange positive and negative numbers of the said array:
	[2, 5, 7, 8, 9, -10, -3, -1]"""


def rearrange(nums):
    pos = list(filter(lambda x: x >= 0, nums))
    neg = list(filter(lambda x: x < 0, nums))
    return pos + neg[::-1]

arr = [-1, 2, -3, 5, 7, 8, 9, -10]
print(rearrange(arr))


""" 20.Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
	Original arrays:
	[1, 2, 3, 5, 7, 8, 9, 10]
	Number of even numbers in the above array: 3
	Number of odd numbers in the above array: 5"""

def count_even_odd(num):
    even = len(list(filter(lambda x: x%2 == 0,num)))
    odd = len(list(filter(lambda x: x%2 == 1,num)))
    return even,odd

L = [1, 2, 3, 5, 7, 8, 9, 10]

e,o = count_even_odd(L)   # Unpacking

print("count of even: ",e)
print("count of odd: ",o)


""" 21.Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
	Original list:
	[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
	Numbers of the above list divisible by nineteen or thirteen:
	[19, 65, 57, 39, 152, 190]"""

def check_divisible(numbers):
    return list(filter(lambda x: x % 19 == 0 or x % 13 == 0,numbers))

L = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

result = check_divisible(L)
print(result)


""" 22.Write a Python program to check whether a given string contains a capital letter, 
    a lower case letter, a number and a minimum length using lambda."""

def check_string(s):
    has_upper = lambda s: any(c.isupper() for c in s)
    has_lower = lambda s: any(c.islower() for c in s)
    has_digit = lambda s: any(c.isdigit() for c in s)
    min_length = lambda s: len(s) >= 8   # you can change length

    if has_upper(s) and has_lower(s) and has_digit(s) and min_length(s):
        return "Valid String"
    else:
        return "Invalid String"

# User input
text = input("Enter a string: ")

print(check_string(text))