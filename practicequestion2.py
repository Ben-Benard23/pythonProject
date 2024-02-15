Here are practicing questions specifically focused on Lists, Dictionaries, Sets, Tuples, and Conditional Statements in Python:
1. Lists:
a) Create a list of your favorite movies and print it.
movies = ["Ironman", "BlackPanther", "Titanic"]
print(movies)  #outcome is ['Ironman', 'BlackPanther', 'Titanic']
# b) Append a new movie to the list and print the updated list.
movies = ["Ironman", "BlackPanther", "Titanic"]
movies.append("CaptainAmerica")
print(movies)  #output is ['Ironman', 'BlackPanther', 'Titanic', 'CaptainAmerica']

2. Dictionaries:
a) Build a dictionary representing a car with keys like ‘brand’, ‘model’, and ‘year’.
cars = {"brand":"Toyota", "model":"highlander", "year":2025}

b) Add a new key-value pair to the dictionary and print the updated dictionary.
cars = {"brand":"Toyota", "model":"highlander", "year":2025}
cars["fuel"] = "diesel"
print(cars)


3. Set:
a) Create two sets of numbers and find their union and intersection.
Union method
odd_numbers = {1,3,5,7,9}
square_numbers ={4,9,16,25}
numbers = odd_numbers.union(square_numbers)
print(numbers) #outcome is {1, 3, 4, 5, 7, 9, 16, 25}

Intersection method
odd_numbers = {1,3,5,7,9}
square_numbers ={4,9,16,25}
numbers = odd_numbers.intersection(square_numbers)
print(numbers) #outcome is {9}

# b) Check if one set is a subset of another.
odd_numbers = {1,3,5,7,9}
square_numbers ={4,9,16,25}
print("sqare_numbers" in odd_numbers)  # outcome is False



4. Tuple:
a) Create a tuple of three elements and print each element.
elements = ("Book", "Pen", "Pencil")
for elements in elements:
    print(elements)
b) Try to modify one element of the tuple and observe the result.
elements = ("Book", "Pen", "Pencil")
elements.remove("Book")  #tuples are imutable
print(elements)

5. Conditions (if, elif, else):
a) Implement a program that checks if a number is positive, negative, or zero using if-elif-else.
number = int(input("please provide a number: "))
if number > 0:
    print("number is positive")
elif number ==0:
    print("number is zero")
else:
    print("number is negative")

b) Write a program to determine if a student’s grade falls into categories: ‘A’, ‘B’, ‘C’, ‘D’, ‘F’.
score = int(input("please provide your score :"))
if score >= 85:
    print("you have an A grade")
elif score >= 70 and score < 85:
    print('you have a B grade')
elif score >= 50 and score < 70:
    print("you have a C grade")
elif score >=30 and score < 50 :
    print("you have a D grade")
else:
    print("you have an F grade")




c) Using a list, check if a given item is present, and print a corresponding message.
elements = ("Book", "Pen", "Pencil")
print("Bag" in elements)  #output is Flase
print("Book" in elements)  #output is True