"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
"""

#########################################

"""
Function Name: clubPoints()
Parameters: N/A
Returns: None
"""
def clubPoints():
    clubsJoined = int(input("How many clubs have you joined? "))
    friendsInvited = int(input("How many friends have you gotten to join clubs? "))
    totalPoints = clubsJoined * 30 + friendsInvited * 50
    print("You have won a total of {} points!!".format(totalPoints))

#########################################

"""
Function Name: moveIn()
Parameters: N/A
Returns: None
"""
def moveIn():
    freshmen = int(input("How many freshmen do you plan to assist? "))
    sophomores = int(input("How many sophomores do you plan to assist? "))
    juniors = int(input("How many juniors do you plan to assist? "))
    totalStudents = freshmen + sophomores + juniors
    totalMins = freshmen*35 + sophomores*20 + juniors*15
    hours = totalMins//60
    remainingMins = totalMins%60
    print("It will take {} hours and {} minutes to help {} students with move-in today.".format(hours, remainingMins, totalStudents))


#########################################

"""
Function Name: tireArea()
Parameters: N/A
Returns: None
"""
def tireArea():
    radius = float(input("What is the radius of the tire? "))
    area = 3.14*(radius**2)
    area = round(area, 2)
    print("The area of the tire is {}.".format(area))


#########################################

"""
Function Name: dining()
Parameters: N/A
Returns: None
"""
def dining():
    panda = int(input("How many meals do you want to order from Panda Express? "))
    roll = int(input("How many meals do you want to order from Rising Roll? "))
    chick = int(input("How many meals do you want to order from Chick-fil-A? "))
    totalPrice = panda*6 + roll*8 + chick*9
    tip = float(input("What percent would you like to tip? "))
    tip = tip/100
    tipAmount = round(totalPrice*tip,2)
    priceWithTip = round(totalPrice*(1+tip), 2)
    print("You paid ${} and tipped ${}.".format(priceWithTip, tipAmount)) 
    

#########################################

"""
Function Name: weeklyBudget()
Parameters: N/A
Returns: None
"""
def weeklyBudget():
    budget = int(input("How much is your budget this week? "))
    saving = float(input("What percentage do you want to save? "))
    budget = round(budget*(1-saving/100),2)
    savingAfterSpends = budget - 13.5 - 21.4
    print("You have ${} left after savings and fees.".format(savingAfterSpends))


















