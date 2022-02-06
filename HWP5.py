#### HOMEWORK PROBLEM 5

"""
Function Name: availability()
Parameters: name (str), availableDays (list)
Returns: None
"""

#### SOLUTION CODE:
import csv
def availability(name, availableDays):
    file = open("available.csv", "a")
    newDays = []
    appendingList = [name]
    daysDict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}
    for day in availableDays:
        newDays.append(daysDict[day])
    for i in range(5):
        if i in newDays:
            appendingList.append("True")
        else:
            appendingList.append("False")
    writer = csv.writer(file)
    writer.writerow(appendingList)
    file.close()


#### TEST CASE(S):
availability("Sindy", ["Monday", "Tuesday"])
availability("John", [])
"""
In the file, the program should print:
Name,Monday,Tuesday,Wednesday,Thursday,Friday
Sindy,True,True,False,False,False

(The first line, which is the header, is already in the designated file named available.csv)
"""
