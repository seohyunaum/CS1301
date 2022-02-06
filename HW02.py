"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: intramuralGames()
Parameters: gameName (str), numFriends (int)
Returns: None (NoneType)
"""
def intramuralGames(gameName, numFriends):
    quarter = int(7*.25)
    threeQuarters = int(7*.75)
    if numFriends <= quarter:
        print("Let's choose something else.")
    elif numFriends > quarter and numFriends <= threeQuarters:
        print("We will try out {} for a little bit!".format(gameName))
    elif numFriends > threeQuarters:
        print("Let's register for {}!!!".format(gameName))

#########################################

"""
Function Name: goShopping()
Parameters: item (str), quantity (int), budget (float)
Returns: moneyLeft (float) or error message (str)
"""
def goShopping(item, quantity, budget):
    spending = 0.0
    if item == "Shorts":
        spending = quantity*13.0
        if spending <= budget:
            return budget-spending
        elif spending > budget:
            return "Not enough money!"
    elif item == "T-Shirts and Tanks":
        spending = quantity*9.75
        if spending <= budget:
            return budget-spending
        elif spending > budget:
            return "Not enough money!"
    elif item == "Swimwear":
        spending = quantity*20.0
        if spending <= budget:
            return budget-spending
        elif spending > budget:
            return "Not enough money!"
    elif item == "Sunglasses":
        spending = quantity*7.5
        if spending <= budget:
            return budget-spending
        elif spending > budget:
            return "Not enough money!"
    elif item == "Slides":
        spending = quantity*15.5
        if spending <= budget:
            return budget-spending
        elif spending > budget:
            return "Not enough money!"
    

#########################################

"""
Function Name: getDinner()
Parameters: budget (float), diningOption (str)
Returns: restaurantName (str)
"""
def getDinner(budget, diningOption):
    if budget <10.0:
        if diningOption == "Takeout" or diningOption == "Delivery":
            return "Chick Fil A"
        elif diningOption == "Indoor" or diningOption == "Outdoor":
            return "Moe's"
    elif budget>10.0 and budget<= 20.0:
        if diningOption == "Indoor" or diningOption == "Takeout":
            return "Tin Drum"
        elif diningOption == "Outdoor" or diningOption == "Takeout":
            return "Umma's"
    elif budget > 20.0 and budget <= 30.0:
        if diningOption == "Indoor" or diningOption == "Outdoor" or diningOption == "Takeout":
            return "Yeah Burger"
        elif diningOption == "Delivery":
            return "Flip Burger"
    elif budget > 30.0 and budget <= 40.0:
        if diningOption == "Indoor":
            return "Two Urban Licks"
        elif diningOption == "Takeout" or diningOption == "Delivery" or diningOption == "Outdoor":
            return "Gypsy Kitchen"
    


#########################################

"""
Function Name: backupRestaurant()
Parameters: budget (float), diningOption (str), backup (str)
Returns: decision (str)
"""
def backupRestaurant(budget, diningOption, backup):
    ideal = getDinner(budget, diningOption)
    decision = ""
    if ideal == "Chick Fil A" or ideal == "Umma's" or ideal == "Gypsy Kitchen" or ideal == "Flip Burger":
        decision = "Yay, you can get dinner at your first choice, "+ideal+"."
        return decision
    else:
        decision = "You'll have to get dinner at "+backup+" instead."
        return decision
        
        

#########################################

"""
Function Name: rideShare()
Parameters: number of riders (int), miles(int), rideShareOptionaA (str), rideShareOptionaB (str)
Returns: rideShareOption (str)
"""
def rideShare(numRiders, miles, optionA, optionB):
    moreThanThree = numRiders > 3
    moreThanTwo = numRiders > 2
    discount = moreThanTwo or moreThanThree
    optionAPrice = 0.0
    optionBPrice = 0.0
    #option A Prices
    if optionA == "Uber":
        optionAPrice = 5 + miles*5.5
        if discount:
            optionAPrice -= 5
    elif optionA == "Lyft":
        optionAPrice = 10 + 1.5*miles
    elif optionA == "Hitch":
        optionAPrice = 7.5*miles
        if discount:
            optionAPrice = optionAPrice - numRiders*10
    elif optionA == "Taxi":
        optionAPrice = 18*miles

    #option B Prices
    if optionB == "Uber":
        optionBPrice = 5 + miles*5.5
        if discount:
            optionBPrice -= 5
    elif optionB == "Lyft":
        optionBPrice = 10 + 1.5*miles
    elif optionB == "Hitch":
        optionBPrice = 7.5*miles
        if discount:
            optionBPrice = optionBPrice - numRiders*10
    elif optionB == "Taxi":
        optionBPrice = 18*miles

    #comparison
    if optionAPrice < optionBPrice:
        return optionA
    elif optionBPrice < optionAPrice:
        return optionB
    elif optionAPrice == optionBPrice:
        return optionA
    
    

























