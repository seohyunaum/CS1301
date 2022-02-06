"""
Georgia Institute of Technology - CS1301
HW03 - Loops and Iteration
"""

#########################################

"""
Function Name: userReplace()
Parameters: startingString (str), username (str)
Returns: replacedString (string)
"""
def userReplace(startingString, username):
    replacedString = ""
    char = ""
    for i in range(len(startingString)):
        char = startingString[i: i+1]
        if char != "$":
            replacedString += char
        elif char == "$":
            replacedString += username
    return replacedString
                                            
    

#########################################

"""
Function Name: specialChar()
Parameters: characterString (str)
Returns: sumOfIndices (int)
"""
def specialChar(characterString):
    sumOfIndices = 0
    char = ""
    for i in range(len(characterString)):
        char = characterString[i: i+1]
        if char in "!@#$%^&*":
            sumOfIndices += i
    return sumOfIndices

#########################################

"""
Function Name: footballGame()
Parameters: score1 (str), score2 (str), team1 (str), team2 (str)
Returns: winningTeam (string)
"""
def footballGame(score1, score2, team1, team2):
    team1score = 0
    team2score = 0
    for i in range(len(score1)):
        if score1[i: i+1] in "0123456789":
            team1score += int(score1[i: i+1])
    for i in range(len(score2)):
        if score2[i: i+1] in "0123456789":
            team2score += int(score2[i: i+1])
    if team1score > team2score:
        return team1
    elif team2score > team1score:
        return team2
    elif team1score == team2score:
        return "It's a tie!"
    

#########################################

"""
Function Name: buyTheDip()
Parameters: currentPrice (float), finalPrice (float), growth (float)
Returns: days (int)
"""
def buyTheDip(currentPrice, finalPrice, growth):
    rate = (100+growth)/100
    days = 0
    while currentPrice > finalPrice:
        currentPrice = currentPrice*rate
        days += 1
    return days


#########################################

"""
Function Name: questionMaker()
Parameters: questions (str), subQuestions (str)
Returns: combinedQuestions (str)
"""
def questionMaker(questions, subQuestions):
    combinedQuestions = ""
    for i in range(len(questions)):
        for j in range(len(subQuestions)):
            combinedQuestions = combinedQuestions + questions[i:i+1] + subQuestions[j: j+1]
    return combinedQuestions



