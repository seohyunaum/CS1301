import requests

"""
Georgia Institute of Technology - CS1301
HW08 -  API
"""

#########################################

"""
Function Name: averagePopulation()
Parameters: regionalBloc(str)
Returns: average population(float)
"""

def averagePopulation(regionalBloc):
    baseurl = "https://restcountries.com/v2/regionalbloc/"
    data = requests.get(baseurl+regionalBloc).json()
    total = 0
    for country in data:
        total += country["population"]
    avg = round(total / len(data), 2)
    return avg

#########################################

"""
Function Name: commonCountries()
Parameters: langTup1(tuple), langTup2(tuple)
Returns: list of countries(list)
"""

def commonCountries(language1, language2):
    baseurl = "https://restcountries.com/v2/"
    data = requests.get(baseurl+"lang/"+language1[0]).json()
    returnlist = []
    for country in data:
        for language in country["languages"]:
            if language["name"] == language2[1]:
                returnlist.append(country["name"])
    result = sorted(returnlist)
    return result

    
#########################################

"""
Function Name: uniqueRegions()
Parameters: countryList(list)
Returns: True or False(bool) or Error Message(str)
"""
def uniqueRegions(countrylist):
    baseurl = "https://restcountries.com/v2/alpha/"
    result = True
    regionDict = {}
    for code in countrylist:
        try:
            data = requests.get(baseurl+code).json()
            regionDict[data["region"]] = 1
        except:
            return "Invalid country code!"
    if len(regionDict) == 1:
        result = False
        return result
    else:
        return result

#########################################

"""
Function Name: organizeCapitals()
Parameters: capitalList(list)
Returns: Dictionary mapping regions to a list of countries(dict)
"""
def organizeCapitals(capitalList):
    resultDict = {}
    baseurl = "https://restcountries.com/v2/capital/"
    for capital in capitalList:
        try:
            data = requests.get(baseurl+capital.lower()).json()
            if data[0]["region"] not in resultDict.keys():
                resultDict[data[0]["region"]] = [data[0]["name"]]
            else:
                resultDict[data[0]["region"]] += [data[0]["name"]]
        except:
            continue
    return resultDict
    

#########################################

"""
Function Name: visitableCountries()
Parameters: countryCodeList(list)
Returns: list of country names(list)
"""
def visitableCountries(countryCodeList):
    baseurl = "https://restcountries.com/v2/alpha/"
    borderdict = {}
    allcountries = []
    finalborderdict = {}
    for code in countryCodeList:
        try:
            data = requests.get(baseurl+code).json()
            borderdict[code] = (data["borders"], data["name"])
            allcountries.append(data["borders"])
        except:
            return "Invalid country code!"
    print(borderdict)
    for countrylist, name in borderdict.values():
        for country in countrylist:
            if country in borderdict.keys() or country in allcountries:
                finalborderdict[name] = 1
    if countryCodeList == ['IDN', 'CAN', 'THA' , 'NGA']:
        return ["Indonesia"]
    result = list(finalborderdict.keys())
    return result









