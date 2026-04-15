""" 1.addition of two numbers from given list is 11"""

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