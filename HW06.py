"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries and Try/Except
"""

#########################################

"""
Function Name: possibleMovies()
Parameters: movies(dict), time (str)
Returns: list of movie names (list)
"""
def possibleMovies(movies, time):
    resultList = []
    for movName in movies:
        for times in movies[movName]:
            if times == time:
                resultList += [movName]
    finalResultList = sorted(resultList)
    return finalResultList

#########################################

"""
Function Name: gameSelector()
Parameters: gameList (list), filterType (str)
Returns: dictionary of games mapped to a boolean value (dict)
"""
def gameSelector(gamesList, filterType):
    resultDict = {}
    for item in gamesList:
        returning = False
        val = ""
        if len(item)%2 == 0:
            val = "even"
        else:
            val = "odd"
        if val == filterType:
            returning = True
        if len(item) == 0:
            resultDict[item] = False
            continue
        resultDict[item] = returning
    return resultDict
        

    
#########################################

"""
Function Name: foodDecoder()
Parameters: secretList1 (list), secretList2 (list)
Returns: list of combined strings and the number of errors (list)
"""
def foodDecoder(lista, listb):
    resultList = []
    count = 0
    for i in range(len(lista)):
        try:
            tempstr = lista[i] + listb[i]
            resultList += [tempstr]
        except TypeError:
            count += 1
    resultList += [count]
    return resultList
    
        

#########################################

"""
Function Name: cheapestLocations()
Parameters: activities (dict)
Returns: dictionary mapping each activity to a location (dict)
"""
def cheapestLocations(activities):
    resultDict = {}
    for event in activities:
        tempdict = activities[event]
        minimum = 100000
        finalLocation = ""
        for locations in tempdict:
            if tempdict[locations] < minimum:
                minimum = tempdict[locations]
                finalLocation = locations
        if minimum != 100000:
            resultDict[event] = finalLocation
    return resultDict
                
            

#########################################

"""
Function Name: sportSuggestions()
Parameters: friends mapped to their suggested sports (dict)
Returns: dictionary mapping each sport to the list of friends who selected these sports (dict).
"""
def sportSuggestions(friends):
    resultDict = {}
    for name in friends:
        sportsList = friends[name]
        for sport in sportsList:
            if sport not in resultDict:
                resultDict[sport] = [name]
            else:
                resultDict[sport].append(name)
        for sport in resultDict:
            newitem = sorted(resultDict[sport])
            resultDict[sport] = newitem
    return resultDict



