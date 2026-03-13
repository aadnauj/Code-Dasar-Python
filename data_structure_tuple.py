#Tuple
'''
A tuple is created by providing identifiers and data, with each data separated by a comma (,). The tuple can be enclosed in parentheses () for readability, although it's not mandatory.

Key characteristics of tuples:

1. Immutable: Once a tuple is created, its elements cannot be changed or added.
2. Ordered: Elements in a tuple maintain the order of insertion.
3. Allows elements of different data types.
3. Can be nested, allowing the creation of more complex data structures.
Tuples are commonly used when you want to represent a collection of items that should remain constant throughout the program.
'''

# Creating tuples
fruits = 'apple', 'orange', 'banana', 'grape', 'apple'
numbers = 5, 10, 15, 20
decimal_numbers = (2.5, -1.8, 4.7, 0.3)
conditions = (False, True, True, False)

# Displaying tuples
print(fruits)
print(numbers)
print(decimal_numbers)
print(conditions)

# Checking the type of 'fruits'
type(fruits)

#Tuple with Heterogeneous Elements and Nested Tuple
# Tuple with heterogeneous elements
mixed_tuple = (1, "two", 3.0, True)

# Nested tuple
nested_tuple = ((1, 2), ("a", "b"))

# Displaying tuples
print("Mixed tuple:", mixed_tuple)
print("Nested tuple:", nested_tuple)

#Converting List to Tuple and Vice Versa
# Converting list to tuple
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = tuple(numbers_list)

# Converting tuple to list
fruits_tuple = ('apple', 'orange', 'banana', 'grape')
fruits_list = list(fruits_tuple)

# Displaying the results
print("List to Tuple:", numbers_tuple)
print("Tuple to List:", fruits_list)

#Tuple Indexing & Slicing
# Tuple for indexing and slicing
colors_tuple = ("red", "green", "blue", "yellow", "purple")

# Indexing
first_color = colors_tuple[0]
last_color = colors_tuple[-1]

# Slicing
selected_colors = colors_tuple[1:4]  # Elements at index 1, 2, 3

# Displaying the results
print("First color:", first_color)
print("Last color:", last_color)
print("Selected colors:", selected_colors)

#Tuple Manipulation
# Original tuple
colors_tuple = ("red", "green", "blue", "yellow", "purple")

# Attempting to modify an element (not possible, will raise a TypeError)
# colors_tuple[1] = "orange"  # Uncommenting this line will raise a TypeError

# Attempting to add an element (not possible, will raise a TypeError)
# colors_tuple += ("orange",)  # Uncommenting this line will raise a TypeError

# Attempting to delete an element (not possible, will raise a TypeError)
# del colors_tuple[2]  # Uncommenting this line will raise a TypeError

# Creating a new tuple with modifications
modified_colors_tuple = colors_tuple + ("orange", "pink")

# Displaying the results
print("Original tuple:", colors_tuple)
print("Modified tuple:", modified_colors_tuple)


