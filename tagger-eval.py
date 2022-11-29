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

print(testDict, keyDict)


# #accuracy
# accuracy = (truePositives+trueNegatives)/(trueNegatives+truePositives+falseNegatives+falsePositives)
# #precision
# precision = truePositives/(truePositives+falsePositives)
# #recall
# recall = truePositives/(truePositives+falseNegatives)
