#### HOMEWORK PROBLEM 1 

"""
Function Name: insertEmoji()
Parameters: message (str), emojiDict()
Returns: convertedMessage (str)
"""

#### SOLUTION CODE:

def insertEmoji(message, emojiDict):
    messageList = message.split()
    convertedMessage = ""
    for word in messageList:
        if word[0] == "*":
            if word[1:] in emojiDict.keys():
                convertedMessage += emojiDict[word[1:]] + " "
        else:
            convertedMessage += word + " "
    return convertedMessage


#### TEST CASE(S):

emojiDict = {
    "happy": "٩(＾◡＾)۶",
    "sad": "(T . T)",
    "angry":"( ˘︹˘ )",
    "love":"♡＾▽＾♡",
    "surprised" : "(；☉_☉)"
    }

insertEmoji("I am so happy *happy", emojiDict)
#I am so happy ٩(＾◡＾)۶

insertEmoji("I love you so much *love", emojiDict)
#I love you so much ♡＾▽＾♡

insertEmoji("Why are you so mean *angry", emojiDict)
#Why are you so mean ( ˘︹˘ )




