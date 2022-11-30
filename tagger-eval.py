#Program Name: Tagger Eval
#Author: Victor Paul LaBrie
#Date: November 28th, 2022
#Problem: You will write a program to learn 
# and apply a part of speech taggerl, and 
# another to evaluate your tagger.
import sys
import re

testFileArg= sys.argv[1]
keyFileArg = sys.argv[2]
testFile = open(testFileArg)
keyFile = open(keyFileArg)

#Construct dicts for both files
testDict = {}
keyDict = {}
for line in testFile.readlines():
    wordTagList = line[::-1].split("/")
    word, tag = "".join(wordTagList[1:])[::-1], re.sub(r"\n", r"", wordTagList[0][::-1])
    testDict[word]=tag
testFile.close()
for line in keyFile.readlines():
    wordTagList = line[::-1].split("/")
    word, tag = "".join(wordTagList[1:])[::-1], re.sub(r"\n", r"", wordTagList[0][::-1])
    keyDict[word]=tag

#Use another dict to keep track of comparisons
#Format: {tuple(predictTag,keyTag): count}
comparisonDict = {}
for word in testDict:
    thisTuple = (testDict[word], keyDict[word])
    if thisTuple in comparisonDict:
        comparisonDict[thisTuple] += 1
    else:
        comparisonDict[thisTuple] = 1

#Sort in ascending order of predicted tags then key tags
sortedCompDict = {}
sortedKeys = sorted(comparisonDict.keys())
for key in sortedKeys:
    sortedCompDict[key]=comparisonDict[key]

#Confusion matrix
correctPredictions = 0
totalPredictions = 0
for item in sortedCompDict:
    totalPredictions += sortedCompDict[item]
    if item[0]==item[1]:
        print(item, sortedCompDict[item])
        correctPredictions += sortedCompDict[item]
    
    #print(item[0] + "\t" + item[1] + ":\t" + str(sortedCompDict[item]))
print(correctPredictions)
print("Accuracy:\t" + str(correctPredictions/totalPredictions))

# #accuracy
# accuracy = (truePositives+trueNegatives)/(trueNegatives+truePositives+falseNegatives+falsePositives)
# #precision
# precision = truePositives/(truePositives+falsePositives)
# #recall
# recall = truePositives/(truePositives+falseNegatives)
