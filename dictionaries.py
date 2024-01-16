#Recall Dictionaries just like list and tuples are compound data types
#Dictionaries store KEY-VALUE pairs
# synthax is inside kelle brackets seperated by commers as shown

#user1 = {"key1":"value1","key2":"value2"}
#print(user1)  # outcome is {'key1': 'value1', 'key2': 'value2'}
# the key can be any imutable object, they cannot be objects that can be modified like list
# secondly the keys must be unique for identification

#Accessing Dictionaries
#Recall that we used indexes in list and tuple sequences, here we type the key in the plave of index
#example
# user1 = {"accesskey":"Ben","Secretaccesskey":"Benard"}
# print(user1["accesskey"])     #output is Ben
# print(user1["Secretaccesskey"])  #Output is benard

#to check if key exist use the get method
#example
# user1 = {"accesskey":"Ben","Secretaccesskey":"Benard"}
# print(user1.get("accesskey"))  # =Ben
# print(user1.get("Name"))    #= None

#ADD AND CHANGE DICTIONARY ITEMS
# user2 = {"Name":"Ben", "age": 61}
# user2["Name"] = "John"
# print(user2)  #outcome is {'Name': 'John', 'age': 61}

# ADDING A NEW KEY AND VALUE if you add a key that does not exists it adds to the pair.
#example
# user2 = {"Name":"Ben", "age": 61}
# user2["movies"] = ["ironman", "Titanic"]
# print(user2)

#REMOVING ELEMENTS FROM THE DICTIONARY> use the pop mehtod
# user2 = {"Name":"Ben", "age": 61}
# user2.pop("Name")
# print(user2)  # outcome is  {'age': 61}

# Iteration Dictionaries
# user2 = {"Name":"Ben", "age": 61}
# for name in user2:
#     print(name)   # this prints the keys of the dictionary

# to print the key and value
user2 = {"Name":"Ben", "age": 61}
for name in user2:
    print(name)
    print(user2[name])  # this prints the key and value
