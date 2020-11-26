sampleDict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Tim', 'salary': 6500}
    }

while 1:
    answer = input("Do you want to add or remove an employee? Select q to quit (a/r/q) ")
    newlist = list(sampleDict.keys())
    if answer == 'a':
        name = input("Please enter the name ")
        salary = int(input("Please enter the salary "))
        value = newlist[-1]
        newID=(int(value[-1]) + 1)
        employeeID = "emp" + str(newID)
        sampleDict[employeeID] = {'name': name, 'salary': salary}
        print(str(sampleDict))
        print("Employee sucessfully added to database")
    if answer == 'r':
        empID = input("Please enter the employee ID (ex: emp45) ")
        if empID in newlist:
            print("Employee found")
            del sampleDict[empID]
            print("Employee removed from database")
        else:
            print("Employee not found")
    if answer == 'q':
        break
print("Thank you for using our system!")


