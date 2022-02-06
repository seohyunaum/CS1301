"""
Georgia Institute of Technology - CS1301
HW07 -  File I/O & CSV
"""
import csv

#########################################

"""
Function Name: sortByArtist()
Parameters: filename (str), artist (str)
Returns: list of songs (list)
"""
def sortByArtist(filename, artist):
  resultList = []
  file = open(filename, "r")
  templist = file.readlines()
  templist.remove("Music data\n")
  newlist = []
  songDict = {}
  for item in templist:
    if item == "\n":
      continue
    newlist.append(item.strip("\n"))
  for i in range(0, len(newlist), 3):
    songDict[newlist[i]] = (newlist[i+1], newlist[i+2])
  for title in songDict:
    if songDict[title][1] == artist:
      resultList.append(title)
  file.close()
  return resultList

#########################################

"""
Function Name: genreFilter()
Parameters: filename (str)
Returns: mapping of songs to lists of genres of that song (dict)
"""
def genreFilter(filename):
    file = open(filename, "r")
    templist = file.readlines()
    templist.remove("Music data\n")
    newlist = []
    songDict = {}
    resultDict = {}
    for item in templist:
        if item == "\n":
            continue
        newlist.append(item.strip("\n"))
    for i in range(0, len(newlist), 3):
        songDict[newlist[i]] = (newlist[i+1], newlist[i+2])
    for key in songDict:
        if songDict[key][0] not in resultDict:
            resultDict[songDict[key][0]] = [key]
        else:
            resultDict[songDict[key][0]] += [key]
    file.close()
    return resultDict


    
#########################################

"""
Function Name: sortByGenre()
Parameters: filename (str), genre (str), output filename (str)
Returns: None (NoneType)
"""
def sortByGenre(filename, genre, outputfile):
    file = open(filename, "r")
    fileb = open(outputfile, "w")
    templist = file.readlines()
    templist.remove("Music data\n")
    newlist = []
    newlist2 = []
    genrelist = []
    songDict = {}
    resultDict = {}
    a = 1
    
    for item in templist:
      if item == "\n":
          continue
      newlist.append(item.strip("\n"))
      
      
    for i in range(0, len(newlist), 3):
      songDict[newlist[i]] = (newlist[i+1], newlist[i+2])

    for song in songDict:
      genrelist.append(songDict[song][0])
                       
    for key in songDict:
      if songDict[key][0] == genre:
        newlist2.append((key, songDict[key][1]))
        
    newlist3 = sorted(newlist2, key = lambda x: x[0])
    
    if genre not in genrelist:
      fileb.write(genre+ "\n")
      fileb.close()
      pass
    else:
      fileb.write(genre + "\n"+"\n")
    
    for i in range(len(newlist3)):
        song = newlist3[i]
        fileb.write('{}. {} - {}'.format(a, song[0], song[1]))
        if i == len(newlist3)-1:
          continue
        fileb.write('\n')
        a += 1
      
    fileb.close()

#########################################

"""
Function Name: biggestSuccess()
Parameters: filename (str), artists (list)
Returns: artist and percentage (tuple)
"""
def biggestSuccess(fileName, artists):
    file = open(fileName)
    csvreader = csv.reader(file)
    rows = []
    artistDict = {}
    tempList = []
    maxim = 0
    resultTup = ()
    for row in csvreader:
      rows.append(row)
    file.close()
    for artistList in rows:
      artistDict[artistList[0]] = [artistList[1], artistList[2], artistList[3]]
    for artist in artists:
      try:
        ratio = float(artistDict[artist][2]) /  float(artistDict[artist][0])
      except:
        ratio = -1
      tempList.append((artist, ratio))
    for artist, ratio in tempList:
      if ratio > maxim:
        maxim = ratio
        resultTup = (artist, round(ratio*100, 2))
    return resultTup
    

#########################################

"""
Function Name: grammyAwards()
Parameters: filename (str), artists (list)
Returns: potential artist choices (tuple)
"""
def grammyAwards(fileName, artists):
    #define empty things
    file = open(fileName)
    csvreader = csv.reader(file)
    artistDict = {}
    rows = []
    alllist = []
    
    #make a list for each row
    for row in csvreader:
      rows.append(row)

    for item in rows:
      alllist.append(item[0])
      alllist.append(item[1])
      alllist.append(item[2])
      alllist.append(item[3])

    #closefile
    file.close()

    #define resulting dictionary
    resultDict = {
      "A-List": [],
      "B-List": [],
      "C-List": []
    }

    #add stuff to dictionary
    for artistList in rows:
      artistDict[artistList[0]] = [artistList[1], artistList[2], artistList[3]]

    #find items in artists and compare values to store in resultDict
    for artist in artists:
      if artist not in artistDict.keys():
        continue
      bill = float(artistDict[artist][2])
      thirty = .3*float(artistDict[artist][0])
      seventy = .7*float(artistDict[artist][0])
      if  bill <= thirty:
        resultDict["C-List"].append(artist)
      elif bill > thirty and bill <= seventy:
        resultDict["B-List"].append(artist)
      elif bill > seventy:
        resultDict["A-List"].append(artist)
        
    for abclists in resultDict:
      if len(resultDict[abclists])>1:
        resultDict[abclists] = sorted(resultDict[abclists], key = lambda x: alllist.index(x))

    return resultDict


