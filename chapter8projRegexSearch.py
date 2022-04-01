import re
import os

files = os.listdir('D:\\pythonSTUFF\\')
textFiles = []
for file in files:
    if file[-3:] == 'txt':
        textFiles.append(file)

print('Input the line to search for: ')
lineToLookFor = re.compile(str(input()))

for file in textFiles:
    openFile = open('D:\\pythonSTUFF\\'+file)
    fileContent = openFile.read()
    found = lineToLookFor.search(fileContent)
    if found is not None:
        print('Your line was found in '+file)
    else:
        print('Your line was not found in '+file)