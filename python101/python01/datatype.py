print("Hello world!") #String
print(42) #Integer
print(3.14) #Float
print(True) #Boolean
print(None) #NoneType
print([])
print(())
print({})

ages = [23, 45, 56, 78] #List
print(ages)
print(f"The type of {ages} is {type(ages)}") #Type
users = {"Name": "Calvin", "age": 18, "Gender": 'Male', "Address": "Florida, Mzansi"} #Dictionary
print(users)

#Reading datatypes
print(f"The first person is: {ages[0]} years old")
print(f"The second person is: {ages[1]} years old")

print(users["Name"])
print(users["Address"])

print(ages[:3]) #Slicing
print(range(10)) #Range

greet = "Hello world!" #String initialization
introduce = greet+f'\nMy name is {users["Name"]} and I am {users["Gender"]}' #String concatenation
print(introduce)
print(("Calvin", 23))
user =(users["Name"], users["age"]) #Tuple
print(user)
print(user[1]) #Indexing

#Boolean

""" Author: Joel
    Date: 2024-01-11
    Description: This is a multiline comment
    License: MIT
"""
is_adult = False

if users["age"] >= 18:
    is_adult = True
    print("You are an adult")
else:
    print("You are a minor")

print(is_adult)

''' Check if the user is a minor or an adult '''
if users["age"] < 18:
    print("You are a minor")
else:
    is_adult = True
    print("You are an adult")

if is_adult:
    print("You are allowed to drink alcohol")
else:
    print("You are not allowed to drink alcohol")
