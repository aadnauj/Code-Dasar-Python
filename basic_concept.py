"""
Variables
- Name to certain values
- The values can be any data type
- The process of storing a value inside a variable is called an assignment.
- Can only be made up of letters, numbers, and underscore.
- Can't be Python reserved keywords.
"""

greeting = 'Hello, World!'
print(greeting)

greeting = "hallo!"
print(greeting)

# Don't use the reserved keyword for the name of your variable

# def = 'Function'
# class = 'Class'
# print(and)
# print(or)

# Berlaku untuk nama file --> disarankan ga boleh sama dengan reserve keyword


'''
Operator
Python menyediakan berbagai operator yang digunakan untuk melakukan operasi pada variabel dan nilai.

Operator dibagi menjadi beberapa kategori:

- Operator Aritmatika: + - * / // % **
- Operator Perbandingan: == != > < >= <=
- Operator Logika: and or not
- Operator Assignment: = += -= *= /= %= //= **=
- Operator Membership: in, not in
- Operator Identity: is, is not
'''

# Contoh semua operator Python

# 1. Aritmatika
a, b = 10, 3
print("Aritmatika:")
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

# 2. Perbandingan
print("\nPerbandingan:")
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 3. Logika
x, y = True, False
print("\nLogika:")
print(x and y, x or y, not x)

# 4. Assignment
n = 5
n += 2; n *= 3
print("\nAssignment:")
print("n =", n)
n = n + 2

# 5. Membership
print("\nMembership:")
print('p' in "python", 'z' not in "python")

# 6. Identity
lst1 = [1,2]; lst2 = lst1; lst3 = [1,2]
print("\nIdentity:")
print(lst1 is lst2, lst1 is lst3, lst1 == lst3)

'''
Data Types
- String (str): text.
- Integer (int): numbers, without fraction.
- Float: numbers with fraction.
- Boolean (bool): data type which only has 2 values
We can convert from one data type to others by committing to implicit conversion or defining an explicit conversion.
'''
# Convert String to Integer
phone = "895444333558"
print(type(phone))

phone = int(phone)
print(type(phone))

# String (str)
color = "red"
print(type(color))

# Integer (int)
length = 10
print(type(length))

# Float
width = 2.0
print(type(width))

print(type(int(width)))

print(width)

def greeting(name):
  return 'Hello, ' + name

print(greeting("Dicoding 2025"))