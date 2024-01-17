#sets is a collection of items like list and tuples
# a set only use imutable  objects like string , tuples and numbers
# a set cannot have mutable objects like list and dictionaries
# Items in a set are not in any particular order and so do not have indexes
# no duplicate items are allowed

# Creating a set
#  a set is inside a curly bracket, seperated by commers.

#Example: No particular order
# Animals = {"Dog", "Cat", "Rabbit"}
# print(Animals)  # outcome in a different order = {'Rabbit', 'Cat', 'Dog'}

#Example: No duplication allowed
# Animals = {"Dog", "Cat","Cat", "Rabbit"}
# print(Animals)  # outcome with no duplication ={'Rabbit', 'Cat', 'Dog'}

# Creating an empty set
#You cannot ues empty curly braces for this else it will create an empty dictionary instead
# so you have to define the set
#example

# animals = set()
# print (animals)  # outcome is = set ()

#Convert a list,dictionaries and strings (iterables) to a set : Using the empty set function
#example

#ADDING/Removing  ITEMS TO A SET
#Sets are mutable , meaning we can add or remove items from a set

#use ADD/REMOVE/DISCARD Method
# Animals = {"Dog", "Cat", "Rabbit"}
# Animals.add("monkey")
# print(Animals)  # outcome is = {'monkey', 'Cat', 'Rabbit', 'Dog'}

# Animals = {'monkey', 'Cat', 'Rabbit', 'Dog'}
# Animals.discard("boy")
# print(Animals) # out put is = {'monkey', 'Rabbit', 'Dog'}

# #To empty a set use the clear method
# Animals = {'monkey', 'Cat', 'Rabbit', 'Dog'}
# Animals.clear()
# print(Animals)  # outcome is set()

# How to find amn Item in the set using the "IN"
# Animals = {'monkey', 'Cat', 'Rabbit', 'Dog'}
# print ("tiger " in Animals)  #False
# print("monkey" in Animals) #True

#Loop in sets
# Animals = {'monkey', 'Cat', 'Rabbit', 'Dog'}
# for animal in Animals:
#     print(animal)

# PYTHON SET OPERATIONS
#Unions Method or | of two sets
# domestic_animals = {"dogs", "cat", "elephant"}
# wild_animals = {"Lion", "Tiger", "elephant"}
# animals = domestic_animals.union(wild_animals)
# print(animals)  #outcome ={'elephant', 'Tiger', 'dogs', 'Lion', 'cat'}

# Intersection of two Sets
# use intersection method or bitwise AND (&)
# domestic_animals = {"dogs", "cat", "elephant"}
# wild_animals = {"Lion", "Tiger", "elephant"}
# animals = domestic_animals.intersection(wild_animals)
# print(animals)  #outcome ={'elephant'}
#
# domestic_animals = {"dogs", "cat", "elephant"}
# wild_animals = {"Lion", "Tiger", "elephant"}
# animals = domestic_animals & (wild_animals)
# print(animals)  #outcome ={'elephant'}





#Note discard and remove works the same but remove will throw and error mesahe if the item to be
#removed is not in the set while discard will not show any error.


# ADDING A LIST INTO A SET USING THE UPDATE METHOD
# animals = {'monkey', 'Cat', 'Rabbit', 'leopard'}
# wild_animals = ["tiger", "leopard", "Bear"]
# animals.update(wild_animals)
# print(animals)  #outcome {'Rabbit', 'leopard', 'Bear', 'monkey', 'Cat', 'tiger'}
# animals.update(wild_animals, {"ducks"})
# print(animals) #outcome is {'tiger','Cat','leopard','Bear','monkey','Rabbit', 'ducks'}no duplicate
# animals.update(wild_animals, {"Name":"Ben"})
# print(animals)#={'monkey', 'Cat', 'tiger', 'ducks', 'Name', 'Bear', 'leopard', 'Rabbit'}
