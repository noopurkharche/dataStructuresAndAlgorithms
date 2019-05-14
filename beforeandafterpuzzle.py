array = ["mission statement",
    "a quick bite to eat",
    "a chip off the old block",
    "chocolate bar",
    "mission impossible",
    "a man on a mission",
    "block party",
    "eat my words",
    "bar of soap"]

# this stores the first word and sentence
firstDict = {}
# this stores the last word and sentence
lastDict = {}


# this loop creates the two dictionary
for sentence in array:

    # split by space
    wordsList = sentence.split(" ")

    # get the last word
    lastWord = wordsList[-1] #mission

    # get the first word
    firstWord = wordsList[0]
    
    # if not present in dictionary    
    if firstWord not in firstDict:
        firstDict[firstWord] = [sentence]
    else:
        firstDict[firstWord].append(sentence)
        

    # if not present in dictionary
    if lastWord not in lastDict:
        lastDict[lastWord] = sentence
#print(firstDict)

for sentence in array:
    wordsList = sentence.split(" ")
    firstWord = wordsList[0]
    lastWord = wordsList[-1] #mission
    #print('----------------------')
    #print(firstDict)
    #print('----------------------')
    if firstWord in lastDict:
        if firstDict[firstWord][0] != 1:
            #print(firstDict[firstWord][0])
            print(lastDict[firstWord] + firstDict[firstWord][0][len(firstWord):])
            firstDict[firstWord][0] = 1
        else:
            index = firstDict[firstWord][0]
            print(lastDict[firstWord] + firstDict[firstWord][index][len(firstWord):])
            index = index + 1