#### HOMEWORK PROBLEM 3

"""
Function Name: makeGrid()
Parameters: dimensions (tup), coordinate (tup)
Returns: resultStr (str)
"""

#### SOLUTION CODE:
def makeGrid(dimensions, coordinate):
    x_total = dimensions[0]
    y_total = dimensions[1]
    resultStr = "  "
    for i in range(x_total):
        resultStr += str(i)
    resultStr += "\n"
    for y in range(y_total):
        resultStr += str(y) + " "
        for x in range(x_total):
            if x == coordinate[0] and y == coordinate[1]:
                resultStr += "0"
            else:
                resultStr += "*"
        resultStr += "\n"
    return resultStr
                    
#### TEST CASE(S):

makeGrid((5,5), (1,2))
"""
if printed:

  01234
0 *****
1 *****
2 *0***
3 *****
4 *****


"""

makeGrid((10, 10), (5,5))
"""
if printed:

  0123456789
0 **********
1 **********
2 **********
3 **********
4 **********
5 *****0****
6 **********
7 **********
8 **********
9 **********


"""



