REMEMBER TO UNCOMMENT ALL BEFORE RUNNING ON YOUR PYCHARM.
synthax for print function
#print("")

# print("JJTech")
# print("Towerbatch")

# print("hello world")
# a = "Raphael"
# print(a)
# to know the type of python data type attributed to a variable

# a = "Raphael"
# print(a)
# print(type(a))
#
# number = "2"
# print(number)
# print(type(number))

# to know the length of the value of the variable
# number = "2222"
# print(number)
# print(type(number))
#
# print(len(number))

#empty value for variable
# empty = ""
# print(empty)
# print(len(empty))

#numbers
  #adding , dividing, multiplying and  subtraction intergers
# print(1+5)
# print(5-1)
# print(6/2)
# print(2*2)
#concatenating numbers
# print("1"+"5")    #anser is 15

#variables
# a= 20
# print(2+a)  #answer is 22(2+22)
# print(type(2+a))


# a= 20
# print("2"+"a")  #answer is 2a
# print(len("2"+"a"))
# print(type("2"+"a"))

#DATA STRUCTURE

#same thing with floats
#working with Booleans
# print(False)
# print(True)   #note that True or False prints without quotations

#print(avinash) >this will give you an error because it is waiting for a variable

# a= "avinash"
# print(a)

#examples of booleans
# print(10>1)   #answer is true
# print(10<1)   #answer is False


#VARIABLES
#Variables are used to store data values that can be used in other programs
a = 1
b = "JJTech"
c = 13.5
# # print(type("a"))
# # print(type("b"))
# # print(type("c"))
#
# print(a+c)
# #note that print("a"+ b) = aJJTech
# print("a"+b+"good") # = aJJTechgood note that you cannot mix strings and intergers
# note that you cannot use True, Str, or functions as a variable

#OPERATORS:
# ArithmeticError
# Assignment operators
# Comparism operators
# logical operators
# Special operators
# Bitwise operators

#READING VARIABLES
# A is a variable that holds the int value 5

#using arithmetic operations
# a=5
# b=3
# print("sum :" ,a+b)
# print("mul :" ,a*b)
# print("sub :" ,a-b)
# print("div :" ,a/b)
# print("sum :" ,a+b)
#
# #using floor division  a//b 1.66666, the decimal point is taken off or ignored
#
# print("floor division :" , a//b)    #answer is just 1
#
# #modulo is like a rememder, we print only the rememder
#
# print("Modulo " , a%b) #5/3 the rememder is 2
#
# #** is exponential
# print("Power to :" , a**b)  #answer is 125  5*5*5

#ASSIGNMENT OPERATORS
# = +=  -=  *=  /= %=  **=
# a= 10
# print(a)
#print(a +"b") # this will not work but
# print(a, "b")  # answer is 10b
#
# a = 10
# b = 5
# # c = a+b
# a= a+b
# print (c)  #answer is 15
# print(a)  #answer is 15 ( a is 10from 118 to 120, but changes to 10 + 5 on line 121
# a=10
# b=5
# print(a) #a=10
# a+=b # (a =a+b) #the value of a+b is stored in a
# print(a) #a=15
# a*=b #(a= a*b)
# print(a) do same with others


#COMPARISM OPERATORS
# a = 10
# b = 4
# print(a>b)  #answer is true
# print(a==b) # if a =b answer is false( equal sidn here is two to differentiate from assig var
# print(a!=b) #a not equal b  true
# print(a<b) #
# print(a<=b) # false
# print(a>=b)  #true

#Class of DEC 20/2023
#Logical Operators (and , or, not)
""" (AND)I want a biryani and coke , that is I want BOTH
I want a biryani or coke means , I want either ONE of them
I want a biryani not coke- here it is specific
"""
# a = 6
# b = 8
#     #false       true
# print(a>b) and (b<10)
#      #ture      true
# print(a<b) and (b<10)
#so true and ture = True
#  true and false = False
# False and True = False
# false and false = False
#example
#print(true and False)  False is the output

#(OR) any one of the statements have to be true
"""True or True = True
True or False = True
False or False = False
False or True = True"""
#example
#print(True or False) output is True

#(not)
#print( not True)  outcome is False

# Bitwise operators
#   &   |    ~           >>               <<
#  and or   tilde(not)   right and left shift

#special Operators ( is and is not)
# a = 10
# b = 10
#print(a is b) #output is true
#looping(print line after line to get what is requested)
#a=[1,2,3,4,5]
# for i in a:
#     if i is 4:
#      print("Tower") #it will print Tower if there is an i=4
# #OR
#     if i == 4:
#      print("Tower")
# a = ["instance1", "instance2", "instance3", "instanece4"]
# for i in a:
#     if i is "instance3":
#         print("Stop")
#     else:
#         print(i)


#KEY WORDS
#They cannot be used in temporal variables orvariable names. They are used for specific case only
#if, and, is, elif, False, True, else, except etc
#example
# True = ("Tower")
# print(True)  this will give you an error

#COMMENTS
#used to describe/understand your code
  #Tripple cquotations used to comment multiple lines

#TYPE CONVERSION or TYPE CASTING
#you cannot add an int and a string print (1 +"Tower")

# a = "Batch"
# print( a + "Tower") # if you do not know the type of variable, then you do type conversion
#
# a= 5
# print(str(a) + "Tower")  #output is 5Tower
# #You can only convert int to strings and not vice versa
#
# a= "BEN"
# print(a + "Tower") #String + string
#
# a= 5
# print(float(5)+10.5) #Outpot is 15.5

#Jan 3rd 2024

#Conditions Statements( if or if and else, elseif)
#You can use only if but you cannot use only else
# marks = 60
# if marks>=90:
#     print("A grade")
# print("JJTECH")   #output will be JJTECH because the if and second are on same level

# marks = 90
# if marks >=90:
#     print("A grade")
#     print("JJTecg-tower") # no output, the second code gets executed only if the first statement is true

# marks = 60
# if marks >=90:
#     print("A grade")
# else:
#     print("Fail")
# print("UFF Done")
# age = 20
# if age >=40:
#     print ("Any")
# elif age >= 30:
#     print("Average looking lady")
# elif age >= 20:
#     print("great looking lady")
# else:
#     print("Nothing")
# print("ufff Done")

#Loops
# a = [1,2]
# for i in a :   # i =  an iterator  a= a list
#     print(i)

# for i in[1,5,21,3,8,3]:
#     print(i)

# for i in range(10): # here only the end point is mentioned , so it starts at zero
#     print(i)

# # a =["petrollena", "Fred", "Benard"]
# # for y in a:
# #     print("JJTech")
# #     print(y)  #output will be JJTech Petrollena, JJTech Fred, and JJTech Benard

# ebs = ["project","p2", "p3", "p4"]
# for i in ebs:
#     print(i)

# a =["petrollena", "fred", "benard"]
# for y in a:
#     if y== "Fred"or y =="Benard":
#        print("JJTech")
#        print(y)  # you want to print Fred and Benard
#     else:
#         print(y)


a =["petrollena", "Fred", "Benard"]
for y in a:
    if y== "petrollena":
        pass
    else:
       print("JJTech")
       print(y)  # you want to print Fred and Benard
