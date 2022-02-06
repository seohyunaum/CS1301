#### HOMEWORK PROBLEM 2

"""
Function Name: crossTheBridge()
Parameters: None
Returns: solutionStr (str)
"""
import random
#### SOLUTION CODE:
def crossTheBridge():
    solutionList = []
    isAlive = True
    num = 0
    for i in range(10):
        randInt = random.randrange(1,3)
        solutionList.append(randInt)
    while isAlive == True:
        if num == 10:
            print("Congratulations! You made it alive!")
            break
        response = input("Which way are you going? ")
        if response.lower() == "right":
            if solutionList[num] == 1:
                num += 1
                continue
            else:
                print("You are dead!")
                isAlive = False
        if response.lower() == "left":
            if solutionList[num] == 2:
                num += 1
                continue
            else:
                print("You are dead!")
                isAlive = False
    solutionstr = "solutuon: "
    for i in range(len(solutionList)):
        if solutionList[i] == 1:
            solutionstr += "right "
        else:
            solutionstr += "left "
    print(solutionstr)
    return solutionstr


#### TEST CASE(S):

crossTheBridge()

"""
Where are you going? Right
Where are you going? left
Where are you going? Left
You are dead!
solution: right left right right left right left right left left
"""



