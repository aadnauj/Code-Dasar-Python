'''
List
A list in Python is a mutable, ordered collection of items. It is a versatile data structure that can hold elements of different data types. Lists are defined by enclosing elements in square brackets ([]) and separating them with commas.
- Lists can contain any type of data, such as integers, floats, strings, or even other lists.
- Being ordered means that the elements in a list have a specific order, and they can be accessed by their index.
- Mutability allows adding, removing, or modifying elements in a list after its creation
'''

# Contoh List
# List of fruit names
fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango', 'pineapple']
print(fruits)
print(type(fruits))


# Using Lists for Different Data Types
# List with different data types
mixed_list = [1, 2.5, "apple", True, [3, 4, 5]]

# Accessing elements
print("Element at index 2:", mixed_list[2])  # Accessing a string
print("Element at index 4:", mixed_list[4])  # Accessing a nested list

# Modifying the list
mixed_list[1] = 10.5  # Modifying a float to an integer
mixed_list.append("orange")  # Adding a string to the end
print("Modified list:", mixed_list)

# Determining the Length of a List
# List with elements
fruits = ["apple", "banana", "orange", "grape"]

# Displaying the length of the list
length_of_fruits = len(fruits)
print("Length of the list:", length_of_fruits)

# Manipulating Elements in a List
'''
Adding Elements:
- Elements can be added to the end of a list using the append() method.
- Multiple elements can be added at once using the extend() method or the + operator.

Removing Elements:
- Elements can be removed by specifying the value using the remove() method.
- The pop() method removes and returns the element at a specific index.
- The del statement can be used to remove elements or slices based on index.
'''

# List for manipulation
fruits = ["apple", "banana", "orange", "grape"]

# Adding elements
fruits.append("kiwi")                 # Adding a single element
fruits.extend(["melon", "pineapple"])  # Adding multiple elements
fruits += ["peach", "mango"]           # Another way to add multiple elements

# Displaying the modified list
print("List after adding elements:", fruits)

# Removing elements
fruits.remove("banana")        # Removing a specific element
removed_element = fruits.pop(2) # Removing and returning element at index 2
del fruits[0]                   # Removing element at index 0

# Displaying the modified list
print("List after removing elements:", fruits)
print("Removed element:", removed_element)

# Nested Lists in Python
# Nested lists
outer_list = [1, 2, [3, 4, 5], "apple", ["orange", "banana"]]

# Accessing elements
print("Element at index 2:", outer_list[2])  # Accessing a nested list
print("Element at index 4:", outer_list[4][1])  # Accessing an element in a nested list

# Modifying the list
outer_list[0] = 10  # Modifying an integer in the outer list
outer_list[2][1] = 8  # Modifying an element in the nested list
outer_list.append(["grape", "kiwi"])  # Adding a new nested list
print("Modified list:", outer_list)

# Manipulating Matrices with Nested Lists
# Matrix represented using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print("Element at row 2, column 3:", matrix[1][2])

# Modifying the matrix
matrix[0][1] = 10  # Modifying an element in the matrix
matrix[2].append(10)  # Adding a new element to the end of the third row
print("Modified matrix:", matrix)

# Checking Elements in a List
'''
Using in and not in Operators:

- The in operator checks if an element exists in a list.
- The not in operator checks if an element does not exist in a list.
- Both operators return a boolean value.
'''

# List for element checks
colors = ["red", "blue", "green", "yellow", "orange"]

# Using 'in' operator
print("Is 'blue' in the list?", 'blue' in colors)
print("Is 'purple' in the list?", 'purple' in colors)

# Using 'not in' operator
print("Is 'green' not in the list?", 'green' not in colors)
print("Is 'yellow' not in the list?", 'yellow' not in colors)

# Unpacking a List

# List for unpacking
student_info = ["John Doe", 20, "Computer Science"]

# Unpacking the list into variables
name, age, major = student_info

# Displaying the unpacked values
print("Name:", name)
print("Age:", age)
print("Major:", major)

# Searching for Elements in a List
# List for searching
numbers = [10, 20, 30, 40, 50, 20, 60]

# Using 'index()' function
index_of_30 = numbers.index(30)
print("Index of 30:", index_of_30)

# Trying to find the index of a non-existing element
try:
    index_of_70 = numbers.index(70)
    print("Index of 70:", index_of_70)
except ValueError:
    print("Element 70 not found in the list.")

# Deleting Elements from a List
'''
Using the del Statement:
- The del statement is used to remove elements from a list based on their index.
- It can also be used to delete the entire list or a slice of the list.

Using the remove() Method:
- The remove() method is used to remove a specific element from the list.
- If the element appears multiple times, only the first occurrence is removed.
- If the element is not found, it raises a ValueError.

Using the clear() Method:
- The clear() method is used to remove all elements from the list, making it empty.
'''
# List for deletion
colors = ["red", "green", "blue", "yellow", "green"]

# Using 'del' statement
del colors[2]  # Deleting element at index 2
print("List after 'del' statement:", colors)

# Using 'remove()' method
colors.remove("green")  # Removing the first occurrence of "green"
print("List after 'remove()' method:", colors)

# Using 'clear()' method
colors.clear()  # Removing all elements
print("List after 'clear()' method:", colors)

# List Indexing and Slicing
'''
Indexing:
- Indexing in Python lists starts from 0. Each element in the list has a unique index.
- Positive indexing refers to counting from the beginning of the list (starting with 0).
- Negative indexing refers to counting from the end of the list (starting with -1 for the last element).

Slicing:
- Slicing allows extracting a portion of a list, creating a new list.
- The syntax for slicing is list[start:stop:step], where start is the beginning index, stop is the ending index (exclusive), and step is the interval.
'''

# List for indexing and slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Indexing
print("Element at index 3:", numbers[3])       # Positive indexing
print("Element at index -2:", numbers[-2])     # Negative indexing

# Slicing
print("Sliced elements:", numbers[2:7])        # Elements from index 2 to 6
print("Sliced with step:", numbers[1:9:2])     # Elements from index 1 to 8 with a step of 2
print("Sliced in reverse:", numbers[::-1])     # All elements in reverse order

# Irregular Nested Lists
# Irregular nested list
irregular_list = [1, [2, 3], [4, 5, 6], "apple", ["orange", 8, 9]]

# Accessing elements
print("Element at index 2:", irregular_list[2])  # Accessing a nested list
print("Element at index 4, element 1:", irregular_list[4][0])  # Accessing an element in a nested list

# Modifying the list
irregular_list[0] = 10  # Modifying an integer
irregular_list[2][1] = 7  # Modifying an element in the nested list
irregular_list.append(["grape", 10, "kiwi"])  # Adding a new nested list
print("Modified list:", irregular_list)

# Sorting a List
'''
Using the sort() Method:
- The sort() method is used to sort a list in-place, meaning it modifies the original list.
- It arranges the elements in ascending order by default.
- The reverse parameter can be set to True to sort in descending order.

Using the sorted() Function:
- The sorted() function creates a new sorted list from the elements of the original list.
- It does not modify the original list.
- Like sort(), the reverse parameter can be used to sort in descending order.
'''
# List for sorting
numbers = [40, 10, 30, 20, 50]

# Using 'sort()' method
numbers.sort()
print("Sorted list using 'sort()':", numbers)

# Using 'sorted()' function
sorted_numbers = sorted(numbers, reverse=True)
print("Original list:", numbers)
print("Sorted list using 'sorted()':", sorted_numbers)


#Copying a List
'''
Using the Assignment Operator (=):
- The assignment operator (=) can be used to create a copy of a list.
- Changes made to the copy will affect the original list, and vice versa.

Using the copy() Method:
- The copy() method is specifically designed for creating a shallow copy of a list.
- The copy created using copy() is independent of the original list, meaning changes to one do not affect the other.
'''
# Original list
original_list = [1, 2, 3, 4, 5]

# Using assignment operator to create a copy
copied_list_1 = original_list

# Using 'copy()' method to create a copy
copied_list_2 = original_list.copy()

# Modifying the copied lists
copied_list_1[0] = 10
copied_list_2[1] = 20

# Displaying the results
print("Original list:", original_list)
print("List copied with assignment operator:", copied_list_1)
print("List copied with 'copy()' method:", copied_list_2)















