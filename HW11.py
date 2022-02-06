"""
Georgia Institute of Technology - CS1301
HW11
"""

#########################################

"""
Function Name: potluck()
Parameters: food list (list)
Returns: food types (dict)
"""
def potluck(foodList):
    resultDict = {}
    for food, type in foodList:
        if type not in resultDict.keys():
            resultDict[type] = [food]
        else:
            resultDict[type].append(food)
    return resultDict

#########################################

"""
Function Name: insertEmoji()
Parameters: message (str), emojis (dict)
Returns: final message (str)
"""
def insertEmoji(message, emojiDict):
    messageList = message.split()
    convertedMessage = ""
    for word in messageList:
        if word[0] == "*":
            if word[1:] in emojiDict.keys():
                convertedMessage += emojiDict[word[1:]] + " "
        else:
            convertedMessage += word + " "
    convertedMessage = convertedMessage.strip()
    return convertedMessage
    
#########################################

"""
Function Name: buyTickets()
Parameters: ticket prices (dict)
Returns: best website and time to buy (str)
"""
def buyTickets(tickets):
    site = ""
    atime = ""
    minprice = 1000
    for website in tickets:
        for time, price in tickets[website]:
            if price <= minprice:
                minprice = price
                site = website
                atime = time
    return "Buy tickets from {} at {}pm.".format(site, atime)

#########################################

"""
Function Name: dinnerLocation()
Parameters: preferred locations (dict), location (str)
Returns: whether majority of people favor that certain time (bool)
"""
def dinnerLocation(preferredLocations, location):
    places = {}
    for person in preferredLocations:
        for place in preferredLocations[person]:
            if place not in places:
                places[place] = 1
            else:
                places[place] += 1
    max = [0, ""]
    for place in places:
        if places[place] > max[0]:
            max[0] = places[place]
            max[1] = place
    if location == max[1] and max[0] > len(preferredLocations)/2:
        return True
    else:
        return False

#########################################

"""
Function Name: sumNestedList()
Parameters: nested list (list)
Returns: sum of all integers (int)
"""
def sumNestedList(alist):
    if len(alist) == 0:
        return 0
    else:
        if type(alist[0]) == list:
            return sumNestedList(alist[0]) + sumNestedList(alist[1:])
        else:
            return alist[0] + sumNestedList(alist[1:])




