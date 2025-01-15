
introduce ="Hello world!"

introduce =introduce.upper() #String methods
print(introduce)

def say_hi(f_name, last_name):
    name = f_name + " " + last_name
    return f"Hello {name}!"


print(say_hi("Calvin", "mokolo".capitalize())) #Function call
print(say_hi("Toure".upper(), "Bonaberi".lower()))


def add(a,b):
    return a+b

x =12.5
y = 14.8
print(f"The sum of {x} and {y} is {add(x,y)}")

def divide(a,b):
    if b>0:
        if a==0:
            return "Zero divided by any number is zero"
        return a/b
    else:
        return "Division by zero is not allowed"

def divide2(a,b):
    result = a/b if b>0 else "Division by Zero is not allowed"
    return result

def is_float(num, name):
    if (type(num)==float) or name=="Joel":
        return True
    return False

print(abs(round(divide2(-4,58), 3)))

print(is_float(divide2(9,2), "Brice"))


students_names =["Calvin", "Jules", "Joel"]
students_ages =[23, 45, 56, 76, 89]

for index, first_name in enumerate(students_names):
    age =students_ages[index]
    print(f"{first_name} is {age} years old")


cities =[{"Douala": "Littoral", "Yaounde": "Centre"}, {"Johannesburg": "Gauteng", "Cape Town": "Western Cape"},
{"Nairobi": "Nairobi", "Mombasa": "Mombasa"}]
cities2 = {"Douala": "Littoral", "Yaounde": "Centre", "Bafoussam": "West",
        "Bamenda": "North West", "Buea": "South West", "Garoua": "North",
        "Maroua": "Far North", "Ngaoundere": "Adamawa", "Ebolowa": "South", "Kribi": "South", "Limbe": "South West"}
# print(cities[0]["Douala"])
# print(city["Douala"])

for key in cities2:
    print(key)

for region in cities2.values():
    print(region)

for key, region in cities2.items():
    print(f"{key}: {region}")

students = {"calvin":[12,15,17,20], "jules":[10,15,18,19], "joel":[8,12,15,20]}


for name, mark in students.items():
    print(f"{name} has the following marks: {mark}")
    print(mark[0])

for key in students:
    print(key)

for marks in students.values():
    print(marks[:3])
