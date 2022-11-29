#Program Name: (!)POS Tagger
#Author: Victor Paul LaBrie
#Date: November 28th, 2022
#Problem: You will write a program to learn 
# and apply a part of speech taggerl, and 
# another to evaluate your tagger.

import sys
import math
import re

#First, we need to take in command line arguments.
#0=most frequent tag mode, 1 = most frequent ++
mode = sys.argv[1]
trainingFileArg = sys.argv[2]
testFileArg = sys.argv[3]

#Then, we need to open the training file. The test file
# will not be opened until later after the training model has been
# learned. 
trainingFile = open(trainingFileArg)

##
##TRAINING FUNCTION
##
def training():
    #Going to use 2 nested dictionaries here. {word:{tag:frequency}}
    #First is just tag frequency for every tag
    wordTagDict = {}
    #Second will the most frequent tags
    mostFrequentTagDict = {}


    #For every word/tag pair, get tag frequencies for that word.
    for wordAndTag in trainingFile.readlines():
        word, tag = splitWordAndTag(wordAndTag)
        if word in wordTagDict:
            if tag in wordTagDict[word]:
                wordTagDict[word][tag] += 1
            else:
                wordTagDict[word][tag] = 1
        else:
            subDict = {tag:1}
            wordTagDict[word]=subDict
    
    #Now, create a dictionary with most frequent tags
    for word in wordTagDict:
        #First, sort dictionary for each word by value
        sortedWordList = sorted(wordTagDict[word], key = wordTagDict[word].get, reverse=True)
        sortedWordDict = {}
        for y in sortedWordList:
            sortedWordDict[y]=wordTagDict[word][y]
        sortedKeys = list(sortedWordDict.keys())
        mostFrequentTagDict[word]=sortedKeys[0]
    #if occurences less than N, remove. do this for both positive and negative models
    print(mostFrequentTagDict)
    return mostFrequentTagDict

#Function to split word and tag
def splitWordAndTag(wordAndTag):
    #only slash we care about will always be the last one
    wordTagList = wordAndTag[::-1].split("/")
    return wordTagList[1][::-1], re.sub(r"\n", r"", wordTagList[0][::-1])
    
training()
trainingFile.close()
#Now we open the test file, and call the test function
testFile = open(testFileArg)
test()
testFile.close