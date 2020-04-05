import os
import clipboard as cp
import random

print("Looking for text files ...")
dataFolder = "./data/"

wordFiles = []
for fileName in os.listdir(dataFolder):
    if fileName.endswith(".txt"):
        print(fileName)
        wordFiles.append(fileName)


allWords = []
for fileName in wordFiles:
    wordFile = open(dataFolder + fileName, 'r', encoding="utf-16")
    for line in wordFile.readlines():
        allWords.append(line.strip())

print(str(len(allWords)) + " words in total.")
print("Filter out words with more than 30 characters...")

filteredWords = []
for word in allWords:
    if len(word) <= 30:
        filteredWords.append(word)

print(str(len(filteredWords)) + " words in total after filtering")
if len(filteredWords) >= 300:
    print("Selecting 300 words at random")
    selectedWords = random.sample(filteredWords, 300)
else:
    print("Only " + str(len(filteredWords)) + " words provided. Taking all of them.")
    selectedWords = filteredWords

scribblString = ""
for word in selectedWords:
    if scribblString == "":
        scribblString = word
    else:
        scribblString += ", " + word

cp.copy(scribblString)
print("Results have been copied to your clipboard")
