""" 1. Write a Python program to read an entire text file.
"""

file = open("code.txt","r")
a = file.read()
print(a)
file.close()


""" 2. Write a Python program to read first n lines of a file.
"""

filename = input("Enter the file name: ")
n = int(input("Enter the number of lines: "))

try:
    with open (filename,"r") as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line,end=' ')
except FileNotFoundError:
    print("File not found")


filenm = input("Enter the file name: ")
n = int(input("Enter the number of lines: "))

try:
    with open(filenm,"r") as file:
        line = file.readlines()
        print(''.join(line[:n]))

except FileNotFoundError:
    print("File not found")


""" 3. Write a Python program to append text to a file and display the text.
"""
filename = input("Enter the file name: ")


with open(filename,"a") as file:
    txt = input("Enter text to be appended: ")
    file.write(txt)

with open(filename,"r") as file:
    txt = file.read()
    print(txt)


""" 4. Write a Python program to read last n lines of a file.
"""

filenm = input("Enter file name: ")
n = int(input("Enter the number of lines: "))
with open(filenm,"r") as file:
    lines = file.readlines()
    print(' '.join(lines[-n:]))


""" 5. Write a Python program to read a file line by line and store it into a list.
"""

filename = input("Enter the file name: ")

try:
    with open(filename,"r") as file:
        lst = []

        for line in file:
            lst.append(line.strip())
            print(lst)

except FileNotFoundError:
    print("File not found")


""" 6. Write a Python program to read a file line by line store it into a variable.
"""

filenm = input("Enter the file name: ")

with open(filenm,"r") as file:
    for line in file:
        print(line)


""" 7. Write a python program to find the longest words.
"""

filenm = input("Enter the file name: ")

try:
    with open(filenm,"r") as file:
        words = file.read().split()

        maxLen = max(len(word) for word in words)
        longestWord = [word for word in words if maxLen == len(word)]

        print("The longest words are: ",longestWord)
        print(maxLen)

except:
    print("File not found")


""" 8. Write a Python program to count the number of lines in a text file.
"""

filenm = input("Enter the file name: ")

try:
    with open(filenm,"r") as file:
        count = 0
        for line in file:
            count += 1
        print(count)
except:
    print("File not found")


""" 9. Write a Python program to count the frequency of words in a file.
"""

filenm = input("Enter the file name: ")

try:
    with open(filenm,"r") as file:
        txt = file.read().lower()
        words = txt.split()

        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

    for word,count in freq.items():
        print(word,":",count)

except:
    print("File not found")


""" 10. Write a Python program to get the file size of a plain file.
"""

import os

def file_size(filename):
    try:
        size = os.path.getsize(filename)
        return size
    except FileNotFoundError:
        return "File not found"

print(file_size("code.txt"))


""" 11. Write a Python program to write a list to a file.
"""
l = ["name","of","the","class"]
filename = input("Enter the file name: ")

with open(filename,"w") as file:
    for i in l:
        file.write(i + "\n")

with open(filename,"r") as file:
    x = file.read()
    print(x)


""" 12. Write a Python program to copy the contents of a file to another file .
"""

source = input("Enter source file name: ")
dest = input("Enter destination file name: ")
with open(source,"r") as src, open(dest,"w") as dst:
    txt = src.read()
    dst.write(txt)
    print("file copied")


""" 13. Write a Python program to read a random line from a file.
"""

import random
file = input("Enter the file name: ")
with open(file,"r") as file:
    line = file.readlines()

    random_line = random.choice(line)
    print(random_line)


""" 14. Write a Python program to assess if a file is closed or not.
"""

filename = input("Enter the file name: ")

file = open(filename,"r")

print("Is file closed?",file.closed)
file.close()
print("Is file closed?",file.closed)


""" 15.Write a Python program that takes a text file as input and 
    returns the number of words of a given text file."""

filename = input("Enter the file name: ")
with open(filename,"r") as file:
    txt = file.read()
    words = txt.split()
    cnt = len(words)
    print("Count of words in file is :",cnt)