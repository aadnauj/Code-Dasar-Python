#Dictionary
'''
A dictionary in Python is a collection of key-value pairs, where each key must be unique. Dictionaries are defined using curly braces {} and consist of comma-separated key-value pairs.

Key Characteristics of Dictionaries:

- Unordered: Elements in a dictionary have no specific order.
- Mutable: Elements of a dictionary can be added, modified, or removed after the dictionary is created.
- Key-Value Pairs: Each element in a dictionary is a key-value pair.
'''

# Creating a dictionary
fruit_prices = {"apple": 1.00, "orange": 0.80, "banana": 0.50}

# Displaying the dictionary
print("Fruit Prices:", fruit_prices)

#Common Dictionary Operations
'''
Accessing values: dictionary[key]
Adding a new key-value pair: dictionary[key] = value
Modifying a value: dictionary[key] = new_value
Removing a key-value pair: del dictionary[key]
Checking key existence: key in dictionary
'''

# Dictionary operations
student_info = {"name": "John",
                "age": 20,
                "grade": "A"}

# Adding a new key-value pair
student_info["city"] = "Bintaro"
print(student_info)

# Modifying a value
student_info["age"] = 21
print(student_info)

# Removing a key-value pair
del student_info["grade"]
print(student_info)

# Checking key existence
has_grade = "grade" in student_info
print("Has grade key?", has_grade)

# Displaying the updated dictionary
print("Updated Student Info:", student_info)

#Dictionary with Homogeneous Data

# Dictionary with homogeneous data (mixed types)
person_info = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zipcode": "12345"
    },
    "contacts": {
        "email": "john@example.com",
        "phone": {
            "home": "555-1234",
            "work": "555-5678"
        }
    },
    "is_student": False
}

# Displaying the complex dictionary with homogeneous data
print("Person Information:")
print("Name:", person_info["name"])
print("Age:", person_info["age"])
print("Address:", person_info["address"])
print("Email:", person_info["contacts"]["email"])
print("Home Phone:", person_info["contacts"]["phone"]["home"])
print("Is Student?", person_info["is_student"])


#Accessing Dictionary Values
# Sample dictionary
fruit_prices = {"apple": 1.00, "orange": 0.80, "banana": 0.50, "kiwi": 1.20}

# Using in to check if a key exists
has_banana = "banana" in fruit_prices
print("Has Banana Key?", has_banana)

# Using not in to check if a key doesn't exist
has_grape = "grape" not in fruit_prices
print("Has Grape Key?", has_grape)

# Using in to check if a value exists
has_price_80 = 0.80 in fruit_prices.values()
print("Has Price 0.80?", has_price_80)

# Using not in to check if a value doesn't exist
has_price_1 = 1.00 not in fruit_prices.values()
print("Has Price 1.00?", has_price_1)


#Using keys(), values(), and items() Functions in a Dictionary
'''
Using keys(), values(), and items() Functions in a Dictionary:

To examine data within a dictionary, we can use the functions keys(), values(), and items().

- keys(): Used to retrieve all keys in the dictionary.
- values(): Used to retrieve all values (items) in the dictionary.
- items(): Used to retrieve all key-value pairs in the dictionary.
'''


# Sample dictionary
person_info = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zipcode": "12345"
    },
    "contacts": {
        "email": "john@example.com",
        "phone": {
            "home": "555-1234",
            "work": "555-5678"
        }
    },
    "is_student": False
}

# Using keys() to get all keys
keys_list = person_info.keys()
print("Keys:", keys_list)

# Using values() to get all values
values_list = person_info.values()
print("Values:", values_list)

# Using items() to get all key-value pairs
items_list = person_info.items()
print("Items:", items_list)

#Accessing Dictionary Values by Key
'''
Similar to lists, accessing values (items) in a dictionary can be done using an index. However, dictionaries use keys as indices.

To access a value in a dictionary, simply mention the key within square brackets [].
'''

# Sample dictionary
fruit_prices = {"apple": 1.00, "orange": 0.80, "banana": 0.50, "kiwi": 1.20}
# Accessing values by key
apple_price = fruit_prices["apple"]
banana_price = fruit_prices["banana"]
# Displaying the accessed values
print("Price of Apple:", apple_price)
print("Price of Banana:", banana_price)

#Manipulating Data in a Dictionary
'''
Data in a dictionary can be added by providing new key-value pairs to the dictionary.

There are three methods that can be used to remove specific data from the dictionary:

1. del: Used to delete an element based on the key.
2. pop(): Used to delete an element based on the key and returns the deleted value.
3. clear(): Used to delete all elements in the dictionary.
'''

# Sample dictionary
student_info = {"name": "Alice", "age": 25, "grade": "B", "is_student": True}

# Adding a new key-value pair
student_info["city"] = "Wonderland"
print(student_info)

# Deleting an element using del
del student_info["grade"]
print("After Deletion (del):", student_info)

# Deleting and returning a value using pop()
removed_age = student_info.pop("age")
print("Removed Age (pop()):", removed_age)
print("After Deletion (pop()):", student_info)

# Clearing all elements using clear()
student_info.clear()
print("After Clearing (clear()):", student_info)






