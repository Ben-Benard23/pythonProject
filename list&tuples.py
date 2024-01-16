# A list is a sequence of items in an order
# A list is created by pacing the items in square brackets separated by commers

# # a list of intergers
#
# numbers = [1,2,3,4,5] # outcome is [1,2,3,4,5]
# print(numbers)
#
# # mixed list
# random_list = [2.5, 3, "Ben", -5]
# print(random_list)
#
# #emty list
# list = []
# print (list)    #outcome is []

#ACCESSING LIST ELEMENTS

# INDEX
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# print(movies)    # outcome will be ['blackman', 'Titanic', 'ironman', 'Blackpanther']
#
# # to access individual item in the list you use index.
#                 [ "blackman", "Titanic", "ironman", "Blackpanther"]
#     index            0           1          2           3

# to choose "Titanic"  you have to  run print(movies[index of Titanic])
#example:
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# print(movies[2])   = ironman

# NEGATIVE INDEXING
# negative index gives the last item from the list

#                 [ "blackman", "Titanic", "ironman", "Blackpanther"]
# negative index      -4          -3         -2           -1
#Example
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# print(movies[-4])  = blackman

#SLICING A LIST(access a whole section of a list)

# #example access the first three items in the list
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# print(movies[0:3])   =['blackman', 'Titanic', 'ironman']  # note here index o is inclusive and index 3 is exclusive
#OR print(movies{:3})  means include the first item

# access the second to the last item on the list will be
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# print(movies[1:4])  = ['Titanic', 'ironman', 'Blackpanther']
#OR print(movies{[1:]) = ['Titanic', 'ironman', 'Blackpanther'] meaning include the last item

#NEGATIVE INDEXE SLICING
#Example
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# print(movies[-3:-1])   = ['Titanic', 'ironman']

#CHANGE ITEMS OF A LIST(change, add, delete items) that is a mutable odject
#example
#change second item from Titanic to Whaterman
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# movies[1] = "Whateman"
# print(movies)   = ['blackman', 'Whateman', 'ironman', 'Blackpanther']

#example 2 change Titanic and ironman in one go
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# movies[1:2] = ["Whateman","Blackman"]
# print(movies)      = ['blackman', 'Whateman', 'Blackman', 'ironman', 'Blackpanther']

#ITERATING THE LIST
#Check if there is an item in the list or not using the "in"
#example
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# print("ironman " in movies)  =false
# print("Whatenam" in movies)  = true

#The for loop:
#it iterates the list one by one until the end of the list
#example
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# for movies in movies:
#     print(movies)
#     outcome will be:
# blackman
# Titanic
# ironman
# Blackpanther

#LIST METHODS
#To add an item to the list use the append method to do so.
#example
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# movies.append("JamesBonn")
# print(movies)  = ['blackman', 'Titanic', 'ironman', 'Blackpanther', 'JamesBonn']

#To insert an item at the second position
#example
# movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
# movies.insert(1,"Boy")
# print(movies)  # =['blackman', 'Boy', 'Titanic', 'ironman', 'Blackpanther']

#To remove an item at the second position
#example
movies = [ "blackman", "Titanic", "ironman", "Blackpanther"]
movies.remove("ironman")
print(movies)  =['blackman', 'Titanic', 'Blackpanther']

