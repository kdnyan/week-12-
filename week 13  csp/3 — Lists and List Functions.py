# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

#collections are used to store multiple items in a single variable
#lists are ordered collections of items
#lists are mutable, meaning you can change their content
#lists are created using square brackets []

list_of_fruits = ["apple", "banana","cherry","date"]
print(list_of_fruits) 
print (type(list_of_fruits))
print(list_of_fruits[0])
print(list_of_fruits[1])
print(list_of_fruits[-1])
print(list_of_fruits[1:3])
list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1])
list_of_fruits.append("elderberry") #add stuff to the end
list_of_fruits.append("mango")
list_of_fruits.append("pineapple")
print(list_of_fruits)
list_of_fruits.extend (["fig","grape","honeydew"])
print(list_of_fruits)
list_of_fruits.reverse()
print(list_of_fruits)
popped_item = list_of_fruits.pop() #pop removes the last one
print(popped_item)
print(list_of_fruits)
list_of_fruits.insert(1, "blueberry")
print(list_of_fruits)
#removing a specific item by value
list_of_fruits.remove("banana")
print(list_of_fruits)
list_of_fruits.insert(3,"smub")
print(list_of_fruits)
list_of_fruits.sort() #sorts the list in ascending order
print(list_of_fruits)

#why use lists instead of individual variables
#imagien u have 100 iteems to manage
list_of_items = list(range(1,1001)) # creates a list of numbers
print(list_of_items)
print(len(list_of_items)) # 1000
popped_item = list_of_items.pop()
print(list_of_items)
list_of_items.extend (range(1001,2001))
print(list_of_items)

#why use a list
#instead of creating seperate variabkes
#for each item, we can store them in a list
#this makes our job easier
# this makes managing the complexticyt of our code easier
#when we need to manage multiple items
# performance task answer 
#sets and tuples 
# sets and tuples are also part of the collections
#family in python 
#sets examples:
set1 = {1,2,3,4,5}
set2 = ("apple","banana","cherry")
print(set1) 
print(set2)
print(type(set1))
set_with_duplicates= {1,2,3,4,4,5}
print(set_with_duplicates) 
print(3 in set1)
print(6 in set1)
tuple1 = (1,2,3,4,5)
tuple2 = ("apple","banana","cherry")
print(type(tuple))
#why use tuple instead of lists, tuples are immutable, meaning they cannot be changed after creation. 
# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
list_of_food = ["burger", "wings", "boneless_wings", "fries", "soda"]
# Print the second and last item.
print(list_of_food[-1])
# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.