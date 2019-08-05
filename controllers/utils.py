# Returns all repeated characters in a string
def checkMultipleValuesPresentInString(companyName):
    listOfChar = list(companyName)
    repeatedCharacters = []
    for tempChar in listOfChar:
        if companyName.count(tempChar)>1 and tempChar not in repeatedCharacters and tempChar!= " " :
            repeatedCharacters.append(tempChar)

    return repeatedCharacters

# Returns string sorted with ASCII values
def checkAsciForOrder(companyName, repeatedCharactersArray):
    sortedString = ""
    companyList = list(companyName)
    uniqueCharList = [tempCount for tempCount in companyList if tempCount not in repeatedCharactersArray]
    uniqueNameString = "".join(uniqueCharList)
    if len(repeatedCharactersArray) == 2:
        sortedString = checkForCountOfChar(1,repeatedCharactersArray,uniqueNameString)
    elif len(repeatedCharactersArray) == 1:
        sortedString = checkForCountOfChar(2,repeatedCharactersArray,uniqueNameString)
    elif len(repeatedCharactersArray) == 0:
        sortedString = checkForCountOfChar(3,repeatedCharactersArray,uniqueNameString)
    return sortedString

# To check whether char string is greater than character list and then concatenate it
def checkForCountOfChar(requiredCount,repeatedCharactersArray,companyName):
    
    companyNameString = "".join(companyName)
    sortedFinalString = ""
    sortedName = sorted(companyNameString)
    if len(companyName)>requiredCount:
        for tempCount in range(requiredCount):
            sortedFinalString = sortedFinalString+ sortedName[tempCount]
    else :
        for tempCountTwo in range(len(companyName)):
            sortedFinalString = sortedFinalString+ sortedName[tempCountTwo]

    stringOfRepeatedChar = "".join(repeatedCharactersArray)
    return stringOfRepeatedChar+sortedFinalString


# To prepare the final logostring
def prepareFinalOutputString(givenString):
    logoString = ""
    logoString = list(givenString)
    if len(logoString)>3:
        reducedOutput = logoString[:3]
        return reducedOutput
    else:
        return logoString

