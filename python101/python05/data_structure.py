#List
employees_names =["Jules", "Calvin", "Joel", "Steve", "Mathias", "John", "Peter", "Paul", "James", "Luke", "Mark", "Matthew", "Simon"]

#For loop
for name in employees_names:
    #if condition
    if(name == "Jules"):
        print(f"Hello {name}, get well soon!")
    elif(name=="Calvin"):
        print(f"Hello {name}, you are rocking!")
    elif(name=="Joel"):
        print(f"Hello {name}, you are doing great!")
    else:
        print("Hello", name)

#Dictionary and list
employees ={"Jules":[3000, "Data Scientist", "Germany"],
            "Calvin": [30000, "Data Engineer", "USA"],
            "Joel":[3000, "Machine Learning Engineer", "Cameroon"],}

print(employees["Jules"])

for name, employee_info in employees.items():
    print(f"Name: {name}")
    print(f"Salary: {employee_info[0]}")
    print(f"Role: {employee_info[1]}")
    print(f"Country: {employee_info[2]}")

    for info in employee_info:
        print(info)
