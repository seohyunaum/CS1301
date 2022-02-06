#### HOMEWORK PROBLEM 4

"""
Function Name: watchGhibli()
Parameters: options (list), fileName (str)
Returns: None
"""

#### SOLUTION CODE:
import requests
def watchGhibli(options, fileName):
    data = requests.get("https://ghibliapi.herokuapp.com/films").json()
    resultFile = open(fileName, "w")
    for option in options:
        resultFile.write(option + "\n")
        resultFile.write("Description: ")
        for film in data:
            if option == film["title"]:
                resultFile.write(film["description"])
                resultFile.write("\n")
                resultFile.write("Rating: ")
                resultFile.write(film["rt_score"])
        resultFile.write("\n\n")
    if len(options) == 0:
        resultFile.write("Let me know if you are interested in any Ghibli movies!!")
    resultFile.close()


#### TEST CASE(S):
watchGhibli(["Castle in the Sky","Grave of the Fireflies", "Whisper of the Heart"], "ghibliFile.txt")

"""
In a txt file named "ghibliFile.txt", the program should write:
Castle in the Sky
Description: The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.
rating: 95

Grave of the Fireflies
Description: In the latter part of World War II, a boy and his sister, orphaned when their mother is killed in the firebombing of Tokyo, are left to survive on their own in what remains of civilian life in Japan. The plot follows this boy and his sister as they do their best to survive in the Japanese countryside, battling hunger, prejudice, and pride in their own quiet, personal battle.
rating: 97

Whisper of the Heart
Description: Shizuku lives a simple life, dominated by her love for stories and writing. One day she notices that all the library books she has have been previously checked out by the same person: 'Seiji Amasawa'. Curious as to who he is, Shizuku meets a boy her age whom she finds infuriating, but discovers to her shock that he is her 'Prince of Books'. As she grows closer to him, she realises that he merely read all those books to bring himself closer to her. The boy Seiji aspires to be a violin maker in Italy, and it is his dreams that make Shizuku realise that she has no clear path for her life. Knowing that her strength lies in writing, she tests her talents by writing a story about Baron, a cat statuette belonging to Seiji's grandfather.
rating: 91


"""


