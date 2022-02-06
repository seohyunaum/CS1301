"""
Georgia Institute of Technology - CS1301
HW04 - Strings, indexing and lists
"""

#########################################

"""
Function Name: fixTickets()
Parameters: ticketNumber (str)
Returns: fixedTicket (str)
"""
def fixTickets(ticketNumber):
    result = ""
    for char in ticketNumber:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        elif char.isdigit():
            result += char
    return result
    


#########################################

"""
Function Name: secret()
Parameters: message (str)
Returns: secret message (str)
"""
def secret(message):
    result = ""
    tempWord = ""
    alist = message.split()
    for word in alist:
        tempWord += word[::-1]
        result += tempWord + " "
        tempWord = ""
    result = result[:-1]
    return result
    

#########################################

"""
Function Name: countTickets()
Parameters: aList (list)
Returns: total (int) or error message (str)
"""
def countTickets(aList):
    tickets = 0
    for a in range(len(aList)):
        if type(aList[a]) == str:
            if aList[a+1] > 3:
                return "Sorry {}, but you can only get a maximum of three tickets per person.".format(aList[a])
        if type(aList[a]) == int:
                tickets += aList[a]       
    return tickets


#########################################

"""
Function Name: fieldTripRoster()
Parameters: friendList (list)
Returns: nameList (list)
"""
def fieldTripRoster(friendList):
    nameList = []
    for aList in friendList:
        for item in aList:
            if type(item) == str and item not in nameList:
                nameList.append(item)
    nameList.sort()
    return nameList


#########################################

"""
Function Name: isSublist()
Parameters: myList (list), otherList (list)
Returns: True or False (bool)
"""
def isSublist(myList, otherList):
    temporary = []
    for item in myList:
        if item in otherList:
            temporary.append(item)
    if temporary == otherList:
        return True
    return False



