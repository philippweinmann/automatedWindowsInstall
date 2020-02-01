import subprocess
import re

def extractTerminalOutput():
    result = subprocess.run(['choco', 'list', '--local-only'], stdout=subprocess.PIPE, shell=True);
    stringResult = result.stdout.decode('utf-8');
    return stringResult

def removeAmountOfPackagesInstalled(chocoListString):
    patternAmountOfPackagesInstalled = "(\s)*(\d)*(\s)packages"
    splitString = re.split(patternAmountOfPackagesInstalled, chocoListString)
    return splitString[0];

def removeVersionNumbers(chocoListStringWithOutAmountOfPackagesInstalled):
    pattern = "[\s]+"
    splitString = re.split(pattern, chocoListStringWithOutAmountOfPackagesInstalled)
    chocoOnlyPackageNameString = []
    counter = 0
    while counter < len(splitString):
        # print(counter, ": ", splitString[counter])
        # if(counter + 1 < len(splitString)):
        #    print(counter + 1, ": ", splitString[counter + 1])
        chocoOnlyPackageNameString.append(splitString[counter])
        counter += 2
    return chocoOnlyPackageNameString

def extractPackageNames():
    terminalOutput = extractTerminalOutput()
    outputWithoutAmountOfPackagesInstalled = removeAmountOfPackagesInstalled(terminalOutput)
    listOfOnlyPackageNames = removeVersionNumbers(outputWithoutAmountOfPackagesInstalled)
    return listOfOnlyPackageNames


