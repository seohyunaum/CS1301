import math
import calendar
import starbucks


"""
Georgia Institute of Technology - CS1301
HW05 - Lists, Tuples, and Modules
"""

#########################################

"""
Function Name: dinnerParty()
Parameters: list of names and availabilities (list), day (str)
Returns: list of friends (list)
"""
def dinnerParty(availabilities, day):
    resultList = []
    for name, dayList in availabilities:
        if day in dayList:
            resultList += [name]
    return resultList

#########################################

"""
Function Name: whatShouldIWear()
Parameters: list of temperatures (list), list of recommendations (list)
Returns: list of tuples (list)
"""
def whatShouldIWear(temps, reccs):
    resultList = []
    for i in range(len(temps)):
        formTuple = (temps[i], reccs[i])
        resultList.append(formTuple)
    return resultList

    
#########################################

"""
Function Name: cheapMeals()
Parameters: list of strings (list) and budget (float)
Returns: tuple containing menu items (tuple)
"""
def cheapMeals(menuStringList, budget):
    resultTuple = ()
    resultList = []
    
    def returnTempTuple(item):
        dollarIndex = item.index("$")
        dashIndex = item.index("-")
        menuName = item[:dashIndex - 1]
        price = float(item[dollarIndex+1:])
        return (price, menuName)
    
    for i in range(len(menuStringList)):
        tempTup = returnTempTuple(menuStringList[i])
        if tempTup[0] <= budget:
            resultList.append(tempTup)

    newResultList = sorted(resultList)
    
    for price, name in newResultList:
        resultTuple += (name,)

    return resultTuple
        
#########################################

"""
Function Name: wednesdays()
Parameters: list of tuples with dates and holidays (list)
Returns: list of holidays (list)
"""
def wednesdays(datesList):
    resultList = []
    for holiday, day, month, year in datesList:
        dayOfWeek = calendar.weekday(year, month, day)
        if dayOfWeek == 2:
            resultList.append(holiday)
    return resultList

#########################################

"""
Function Name: starbucksFanatic()
Parameters: list of starbucks menu items (list)
Returns: list of tuples containing menu item name and price (list)
"""
def starbucksFanatic(menuItems):
    resultList = []
    tempTup = ()
    total = 0
    for menuName in menuItems:
        price = starbucks.menu(menuName)
        total += price
        if price != 0:
            tempTup = (menuName, price)
            resultList.append(tempTup)
    resultList.append(round(total, 2))
    return resultList






















