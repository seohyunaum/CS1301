"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""

#########################################

"""
Function Name: add()
Parameters: list of ints (list)
Returns: total (int)
"""
def add(alist):
    if len(alist) == 0:
        return 0
    else:
        num = alist[0]
        total = num + add(alist[1:])
        return total

#########################################

"""
Function Name: decoder()
Parameters: encryption (str)
Returns: codeword (str)
"""
def decoder(astr):
    if len(astr) == 0:
        return ""
    else:
        if astr[0].isalpha():
            result = astr[0] + decoder(astr[1:])
        else:
            result = decoder(astr[1:])
        return result

    
#########################################

"""
Function Name: pirateTreasure()
Parameters: directions (list)
Returns: distance_to_treasure (int)
"""
def pirateTreasure(directions):
    if len(directions) == 0:
        return 0
    else:
        if directions[0] == "up":
            total = 1+ pirateTreasure(directions[1:])
        elif directions[0] == "down":
            total = -1 + pirateTreasure(directions[1:])
        return total

#########################################

"""
Function Name: lengthDict()
Parameters: list of names (list)
Returns: dictionary mapping names to length (dict)
"""
def lengthDict(names):
    if len(names) == 0:
        return {}
    else:
        count = 0
        for char in names[0]:
            if char.lower() in 'bcdfghjklmnpqrstvwxyz':
                count += 1
        tempDict = lengthDict(names[1:])
        tempDict[names[0]] = count
        return tempDict
        

#########################################

"""
Function Name: balancedStr()
Parameters: string of characters (str)
Returns: isBalanced (bool)
"""
def balancedStr(astr):
    if len(astr) == 0:
        return True
    else:
        result = False
        first = astr[0].islower() and astr[-1].islower()
        second = astr[0].isupper() and astr[-1].isupper()
        if first or second:
            return balancedStr(astr[1:-1])
        else:
            return False
        
            



